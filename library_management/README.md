# Library Management System

A beginner-friendly, modular Python OOP project using JSON files for persistence.

## Features
- Add, update, delete, search, and list books.
- Track total, borrowed, and available copies.
- Register, update, delete, search (through manager methods), and validate members.
- Issue and return books; calculate fines at ₹10 per day after the due date.
- Report available/borrowed books, top borrowers, and fines.
- Custom exceptions, type hints, docstrings, and JSON storage.

## Requirements
- Python 3.10 or newer (uses modern type hints).
- No third-party packages are required.

## Run from the project root
Activate your virtual environment, then run:

```powershell
python -m library_management.app
```

Run the command from the folder that contains `library_management`.

## JSON data
The three JSON files are created automatically if missing. Do not replace malformed JSON with an empty list without checking it first; the app reports a storage error rather than silently discarding data.

## Fine policy
The sample project charges ₹10 for each day returned after the due date. The default loan period is 14 days. Change `FINE_PER_DAY` in `issue.py` if your assignment specifies a different amount.

## Example workflow
1. Add a book with ID `1`, title `Python Basics`, author `A. Writer`, and `2` copies.
2. Register a member with ID `101`, name `Ravi`, and email `ravi@example.com`.
3. Issue book ID `1` to member ID `101` with issue ID `1001`.
4. Return issue ID `1001` using the return menu option.
5. Choose Reports to see availability, borrowers, and fines.
