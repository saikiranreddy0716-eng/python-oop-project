"""Safe JSON storage helpers for the library records."""
import json
from pathlib import Path
from typing import Any
from .exceptions import StorageError


class JsonStorage:
    """Read and write JSON lists without silently replacing malformed data."""
    def __init__(self, data_dir: Path | None = None) -> None:
        self.data_dir = data_dir or (Path(__file__).resolve().parent / "data")
        self.data_dir.mkdir(parents=True, exist_ok=True)
        for filename in ("books.json", "members.json", "issues.json"):
            path = self.data_dir / filename
            if not path.exists():
                path.write_text("[]\n", encoding="utf-8")

    def load(self, filename: str) -> list[dict[str, Any]]:
        """Load a JSON list. Invalid JSON raises StorageError and is not overwritten."""
        path = self._path(filename)
        try:
            with path.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except json.JSONDecodeError as exc:
            raise StorageError(f"{filename} contains invalid JSON. Fix the file before continuing.") from exc
        except OSError as exc:
            raise StorageError(f"Could not read {filename}: {exc}") from exc
        if not isinstance(data, list) or any(not isinstance(item, dict) for item in data):
            raise StorageError(f"{filename} must contain a JSON list of objects.")
        return data

    def save(self, filename: str, records: list[dict[str, Any]]) -> None:
        """Save records as readable JSON."""
        path = self._path(filename)
        try:
            with path.open("w", encoding="utf-8") as file:
                json.dump(records, file, indent=4, ensure_ascii=False)
                file.write("\n")
        except OSError as exc:
            raise StorageError(f"Could not write {filename}: {exc}") from exc

    def _path(self, filename: str) -> Path:
        """Only allow the known data files to be accessed."""
        if filename not in {"books.json", "members.json", "issues.json"}:
            raise StorageError("Unsupported data filename.")
        return self.data_dir / filename
