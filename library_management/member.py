"""Member model and membership-management operations."""
from dataclasses import dataclass
from .exceptions import DuplicateError, NotFoundError
from .storage import JsonStorage
from .validator import positive_int, required_text, valid_email


@dataclass
class Member:
    """Represent a registered library member."""
    member_id: int
    name: str
    email: str
    active: bool = True

    def __post_init__(self) -> None:
        positive_int(self.member_id, "Member ID")
        self.name = required_text(self.name, "Member name")
        self.email = valid_email(self.email)
        if not isinstance(self.active, bool):
            raise ValueError("Active status must be True or False.")

    def to_dict(self) -> dict:
        """Convert the member to a JSON-compatible dictionary."""
        return {"member_id": self.member_id, "name": self.name,
                "email": self.email, "active": self.active}

    @classmethod
    def from_dict(cls, data: dict) -> "Member":
        """Build a Member from a stored dictionary."""
        return cls(**data)


class MemberManager:
    """Register, update, delete, search, and list members."""
    FILE = "members.json"

    def __init__(self, storage: JsonStorage) -> None:
        self.storage = storage

    def list_members(self) -> list[Member]:
        """Return all saved members."""
        return [Member.from_dict(row) for row in self.storage.load(self.FILE)]

    def get_member(self, member_id: int) -> Member:
        """Find a member by ID and ensure the membership is active."""
        for member in self.list_members():
            if member.member_id == member_id:
                if not member.active:
                    raise NotFoundError(f"Membership for member {member_id} is inactive.")
                return member
        raise NotFoundError(f"Member ID {member_id} was not found.")

    def register_member(self, member: Member) -> None:
        """Register a new member, rejecting duplicate IDs."""
        members = self.list_members()
        if any(item.member_id == member.member_id for item in members):
            raise DuplicateError(f"Member ID {member.member_id} already exists.")
        members.append(member)
        self._save(members)

    def update_member(self, member_id: int, name: str, email: str, active: bool) -> Member:
        """Update member details and membership status."""
        members = self.list_members()
        for index, member in enumerate(members):
            if member.member_id == member_id:
                updated = Member(member_id, name, email, active)
                members[index] = updated
                self._save(members)
                return updated
        raise NotFoundError(f"Member ID {member_id} was not found.")

    def delete_member(self, member_id: int) -> None:
        """Delete a member by ID."""
        members = self.list_members()
        if not any(member.member_id == member_id for member in members):
            raise NotFoundError(f"Member ID {member_id} was not found.")
        self._save([member for member in members if member.member_id != member_id])

    def search_members(self, query: str) -> list[Member]:
        """Search members by name or email."""
        term = required_text(query, "Search text").casefold()
        return [member for member in self.list_members()
                if term in member.name.casefold() or term in member.email.casefold()]

    def _save(self, members: list[Member]) -> None:
        self.storage.save(self.FILE, [member.to_dict() for member in members])
