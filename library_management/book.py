"""Book model and book-management operations."""
from dataclasses import dataclass
from .exceptions import DuplicateError, NotFoundError, ValidationError
from .storage import JsonStorage
from .validator import non_negative_int, positive_int, required_text


@dataclass
class Book:
    """Represent a book and the number of copies currently borrowed."""
    book_id: int
    title: str
    author: str
    total_copies: int = 1
    borrowed_copies: int = 0

    def __post_init__(self) -> None:
        positive_int(self.book_id, "Book ID")
        self.title = required_text(self.title, "Title")
        self.author = required_text(self.author, "Author")
        positive_int(self.total_copies, "Total copies")
        non_negative_int(self.borrowed_copies, "Borrowed copies")
        if self.borrowed_copies > self.total_copies:
            raise ValidationError("Borrowed copies cannot exceed total copies.")

    @property
    def available_copies(self) -> int:
        """Return the number of copies available to issue."""
        return self.total_copies - self.borrowed_copies

    def to_dict(self) -> dict:
        """Convert the book to a JSON-compatible dictionary."""
        return {"book_id": self.book_id, "title": self.title, "author": self.author,
                "total_copies": self.total_copies, "borrowed_copies": self.borrowed_copies}

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        """Build a Book from a stored dictionary."""
        return cls(**data)


class BookManager:
    """Create, update, delete, search, and list books."""
    FILE = "books.json"

    def __init__(self, storage: JsonStorage) -> None:
        self.storage = storage

    def list_books(self) -> list[Book]:
        """Return all saved books."""
        return [Book.from_dict(row) for row in self.storage.load(self.FILE)]

    def get_book(self, book_id: int) -> Book:
        """Find one book by its ID."""
        for book in self.list_books():
            if book.book_id == book_id:
                return book
        raise NotFoundError(f"Book ID {book_id} was not found.")

    def add_book(self, book: Book) -> None:
        """Add a new book, rejecting duplicate IDs."""
        books = self.list_books()
        if any(item.book_id == book.book_id for item in books):
            raise DuplicateError(f"Book ID {book.book_id} already exists.")
        books.append(book)
        self._save(books)

    def update_book(self, book_id: int, title: str, author: str, total_copies: int) -> Book:
        """Update a book's title, author, and total number of copies."""
        books = self.list_books()
        for index, book in enumerate(books):
            if book.book_id == book_id:
                updated = Book(book_id, title, author, total_copies, book.borrowed_copies)
                books[index] = updated
                self._save(books)
                return updated
        raise NotFoundError(f"Book ID {book_id} was not found.")

    def delete_book(self, book_id: int) -> None:
        """Delete a book only when no copies are currently borrowed."""
        books = self.list_books()
        for book in books:
            if book.book_id == book_id:
                if book.borrowed_copies:
                    raise ValidationError("Cannot delete a book while copies are borrowed.")
                self._save([item for item in books if item.book_id != book_id])
                return
        raise NotFoundError(f"Book ID {book_id} was not found.")

    def search_books(self, query: str) -> list[Book]:
        """Search titles and authors without case sensitivity."""
        term = required_text(query, "Search text").casefold()
        return [book for book in self.list_books()
                if term in book.title.casefold() or term in book.author.casefold()]

    def _save(self, books: list[Book]) -> None:
        self.storage.save(self.FILE, [book.to_dict() for book in books])
