"""Command-line entry point for the Library Management System."""
from .book import Book, BookManager
from .exceptions import LibraryError
from .issue import IssueManager
from .member import Member, MemberManager
from .reports import ReportManager
from .storage import JsonStorage


def read_int(prompt: str) -> int:
    """Read a whole number from the terminal."""
    raw = input(prompt).strip()
    try:
        return int(raw)
    except ValueError as exc:
        raise ValueError("Please enter a whole number.") from exc


def show_books(manager: BookManager) -> None:
    """Print all books and availability."""
    books = manager.list_books()
    if not books:
        print("No books found.")
        return
    for book in books:
        print(f"ID {book.book_id} | {book.title} | {book.author} | "
              f"Available: {book.available_copies}/{book.total_copies}")


def show_members(manager: MemberManager) -> None:
    """Print all registered members."""
    members = manager.list_members()
    if not members:
        print("No members found.")
        return
    for member in members:
        print(f"ID {member.member_id} | {member.name} | {member.email} | "
              f"Status: {'Active' if member.active else 'Inactive'}")


def run() -> None:
    """Run the interactive menu until the user chooses Exit."""
    storage = JsonStorage()
    books = BookManager(storage)
    members = MemberManager(storage)
    issues = IssueManager(storage, books, members)
    reports = ReportManager(books, issues)

    menu = """
=== LIBRARY MANAGEMENT SYSTEM ===
1. Add book
2. Update book
3. Delete book
4. Search books
5. List books
6. Register member
7. Update member
8. Delete member
9. List members
10. Issue book
11. Return book
12. Reports
0. Exit
"""
    while True:
        print(menu)
        try:
            choice = input("Choose an option: ").strip()
            if choice == "0":
                print("Goodbye!")
                break
            elif choice == "1":
                book = Book(read_int("Book ID: "), input("Title: "),
                            input("Author: "), read_int("Total copies: "))
                books.add_book(book)
                print("Book added successfully.")
            elif choice == "2":
                book_id = read_int("Book ID to update: ")
                updated = books.update_book(book_id, input("New title: "),
                                            input("New author: "), read_int("Total copies: "))
                print(f"Updated: {updated}")
            elif choice == "3":
                books.delete_book(read_int("Book ID to delete: "))
                print("Book deleted successfully.")
            elif choice == "4":
                results = books.search_books(input("Title or author to search: "))
                if results:
                    for book in results:
                        print(f"{book.book_id} | {book.title} | {book.author} | Available: {book.available_copies}")
                else:
                    print("No matching books found.")
            elif choice == "5":
                show_books(books)
            elif choice == "6":
                member = Member(read_int("Member ID: "), input("Name: "), input("Email: "))
                members.register_member(member)
                print("Member registered successfully.")
            elif choice == "7":
                member_id = read_int("Member ID to update: ")
                active_text = input("Active membership? (y/n): ").strip().lower()
                if active_text not in {"y", "n"}:
                    raise ValueError("Enter y or n for membership status.")
                updated = members.update_member(member_id, input("New name: "), input("New email: "), active_text == "y")
                print(f"Updated member: {updated.name}")
            elif choice == "8":
                member_id = read_int("Member ID to delete: ")
                if issues.active_issues_for_member(member_id):
                    raise ValueError("Cannot delete a member with books still borrowed.")
                members.delete_member(member_id)
                print("Member deleted successfully.")
            elif choice == "9":
                show_members(members)
            elif choice == "10":
                issue = issues.issue_book(read_int("New issue ID: "), read_int("Book ID: "), read_int("Member ID: "))
                print(f"Book issued. Due date: {issue.due_date}")
            elif choice == "11":
                issue = issues.return_book(read_int("Issue ID to return: "))
                print(f"Book returned. Fine: ₹{issue.fine:.2f}")
            elif choice == "12":
                print("\nAvailable books:")
                available = reports.available_books()
                if not available:
                    print("None")
                for book in available:
                    print(f"{book.title} (ID {book.book_id}): {book.available_copies} available")
                print("\nBorrowed books:")
                borrowed = reports.borrowed_books()
                if not borrowed:
                    print("None")
                for book, count in borrowed:
                    print(f"{book.title} (ID {book.book_id}): {count} borrowed")
                print("\nTop borrowers (member ID, loan count):")
                print(reports.top_borrowers())
                print("Fine report (issue ID, fine, return date):")
                print(reports.fine_report())
            else:
                print("Please choose a listed option.")
        except (LibraryError, ValueError) as exc:
            print(f"Error: {exc}")
        except KeyboardInterrupt:
            print("\nStopped by user. Goodbye!")
            break


if __name__ == "__main__":
    run()
