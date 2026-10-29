"""Book issue and return operations, including late fines."""
from dataclasses import dataclass
from datetime import date, timedelta
from .book import BookManager
from .exceptions import NotFoundError, ValidationError
from .member import MemberManager
from .storage import JsonStorage
from .validator import positive_int


@dataclass
class Issue:
    """Represent a book loan record."""
    issue_id: int
    book_id: int
    member_id: int
    issue_date: str
    due_date: str
    return_date: str | None = None
    fine: float = 0.0

    @property
    def returned(self) -> bool:
        """Return True when the book has been returned."""
        return self.return_date is not None

    def to_dict(self) -> dict:
        """Convert the issue record to a JSON-compatible dictionary."""
        return {"issue_id": self.issue_id, "book_id": self.book_id,
                "member_id": self.member_id, "issue_date": self.issue_date,
                "due_date": self.due_date, "return_date": self.return_date,
                "fine": self.fine}

    @classmethod
    def from_dict(cls, data: dict) -> "Issue":
        """Build an Issue from a stored dictionary."""
        return cls(**data)


class IssueManager:
    """Issue books, accept returns, and calculate late-return fines."""
    FILE = "issues.json"
    FINE_PER_DAY = 10.0  # ₹10 for each late day

    def __init__(self, storage: JsonStorage, books: BookManager, members: MemberManager) -> None:
        self.storage = storage
        self.books = books
        self.members = members

    def list_issues(self) -> list[Issue]:
        """Return all issue records."""
        return [Issue.from_dict(row) for row in self.storage.load(self.FILE)]

    def issue_book(self, issue_id: int, book_id: int, member_id: int, loan_days: int = 14) -> Issue:
        """Issue one available copy to an active member."""
        positive_int(issue_id, "Issue ID")
        positive_int(loan_days, "Loan days")
        issues = self.list_issues()
        if any(item.issue_id == issue_id for item in issues):
            raise ValidationError(f"Issue ID {issue_id} already exists.")
        book = self.books.get_book(book_id)
        if book.available_copies < 1:
            raise ValidationError("No copies of this book are currently available.")
        self.members.get_member(member_id)
        today = date.today()
        issue = Issue(issue_id, book_id, member_id, today.isoformat(),
                      (today + timedelta(days=loan_days)).isoformat())
        book_rows = self.books.list_books()
        for index, item in enumerate(book_rows):
            if item.book_id == book_id:
                book_rows[index].borrowed_copies += 1
                break
        self.books._save(book_rows)
        issues.append(issue)
        self.storage.save(self.FILE, [item.to_dict() for item in issues])
        return issue

    def return_book(self, issue_id: int, return_date: date | None = None) -> Issue:
        """Return an issued book and calculate any late fine."""
        issues = self.list_issues()
        for index, issue in enumerate(issues):
            if issue.issue_id == issue_id:
                if issue.returned:
                    raise ValidationError("This issue record has already been returned.")
                actual_date = return_date or date.today()
                due = date.fromisoformat(issue.due_date)
                if actual_date < date.fromisoformat(issue.issue_date):
                    raise ValidationError("Return date cannot be before issue date.")
                late_days = max((actual_date - due).days, 0)
                issue.return_date = actual_date.isoformat()
                issue.fine = late_days * self.FINE_PER_DAY
                book_rows = self.books.list_books()
                for book in book_rows:
                    if book.book_id == issue.book_id:
                        if book.borrowed_copies <= 0:
                            raise ValidationError("Book availability data is inconsistent.")
                        book.borrowed_copies -= 1
                        break
                else:
                    raise NotFoundError(f"Book ID {issue.book_id} was not found.")
                self.books._save(book_rows)
                issues[index] = issue
                self.storage.save(self.FILE, [item.to_dict() for item in issues])
                return issue
        raise NotFoundError(f"Issue ID {issue_id} was not found.")

    def active_issues_for_member(self, member_id: int) -> list[Issue]:
        """Return outstanding loans for a member."""
        return [issue for issue in self.list_issues()
                if issue.member_id == member_id and not issue.returned]
