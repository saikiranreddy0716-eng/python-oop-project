"""Reports for book availability, loans, borrowers, and fines."""
from .book import BookManager
from .issue import IssueManager


class ReportManager:
    """Generate summary reports using the book and issue managers."""
    def __init__(self, books: BookManager, issues: IssueManager) -> None:
        self.books = books
        self.issues = issues

    def available_books(self) -> list:
        """Return books with at least one available copy."""
        return [book for book in self.books.list_books() if book.available_copies > 0]

    def borrowed_books(self) -> list[tuple]:
        """Return each book that currently has borrowed copies."""
        return [(book, book.borrowed_copies) for book in self.books.list_books()
                if book.borrowed_copies > 0]

    def top_borrowers(self, limit: int = 5) -> list[tuple[int, int]]:
        """Return (member ID, number of loans) sorted from most to least."""
        counts: dict[int, int] = {}
        for issue in self.issues.list_issues():
            counts[issue.member_id] = counts.get(issue.member_id, 0) + 1
        return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:max(limit, 0)]

    def fine_report(self) -> list[tuple[int, float, str | None]]:
        """Return issue ID, fine amount, and return date for records with fines."""
        return [(issue.issue_id, issue.fine, issue.return_date)
                for issue in self.issues.list_issues() if issue.fine > 0]
