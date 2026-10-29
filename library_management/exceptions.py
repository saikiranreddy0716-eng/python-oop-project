"""Custom exceptions used by the library application."""

class LibraryError(Exception):
    """Base exception for expected library errors."""

class ValidationError(LibraryError):
    """Raised when user input or model data is invalid."""

class NotFoundError(LibraryError):
    """Raised when a requested book, member, or issue does not exist."""

class DuplicateError(LibraryError):
    """Raised when an identifier already exists."""

class StorageError(LibraryError):
    """Raised when JSON storage cannot safely be read or written."""
