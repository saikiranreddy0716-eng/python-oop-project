
"""
Story 3 - Magic Methods and Operator Overloading

This file demonstrates:
__str__, __repr__, __len__,
__eq__, __lt__, __gt__,
__add__, and __sub__.
"""


class Playlist:
    """A playlist containing a list of songs."""

    def __init__(self, name: str, songs: list[str]):
        self.name = name
        self.songs = songs.copy()

    # 1. __str__: User-friendly object display
    def __str__(self) -> str:
        return f"{self.name}: {len(self.songs)} songs"

    # 2. __repr__: Clear representation for debugging
    def __repr__(self) -> str:
        return f"Playlist(name={self.name!r}, songs={self.songs!r})"

    # 3. __len__: Makes len(playlist) work
    def __len__(self) -> int:
        return len(self.songs)

    # 4. __eq__: Compare two playlists for equality
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Playlist):
            return NotImplemented
        return self.songs == other.songs

    # 5. __lt__: Check whether this playlist has fewer songs
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Playlist):
            return NotImplemented
        return len(self) < len(other)

    # 6. __gt__: Check whether this playlist has more songs
    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Playlist):
            return NotImplemented
        return len(self) > len(other)

    # 7. __add__: Combine two playlists
    def __add__(self, other: object):
        if not isinstance(other, Playlist):
            return NotImplemented

        return Playlist(
            f"{self.name} + {other.name}",
            self.songs + other.songs,
        )

    # 8. __sub__: Remove songs present in another playlist
    def __sub__(self, other: object):
        if not isinstance(other, Playlist):
            return NotImplemented

        remaining_songs = [
            song for song in self.songs
            if song not in other.songs
        ]

        return Playlist(f"{self.name} - {other.name}", remaining_songs)


if __name__ == "__main__":
    playlist1 = Playlist("Favorites", ["Song A", "Song B", "Song C"])
    playlist2 = Playlist("Party", ["Song B", "Song D"])
    playlist3 = Playlist("Copy", ["Song A", "Song B", "Song C"])

    print("1. STRING REPRESENTATION")
    print(str(playlist1))

    print("\n2. OBJECT REPRESENTATION")
    print(repr(playlist1))

    print("\n3. LENGTH")
    print(len(playlist1))

    print("\n4. EQUALITY")
    print(playlist1 == playlist3)

    print("\n5. LESS THAN")
    print(playlist2 < playlist1)

    print("\n6. GREATER THAN")
    print(playlist1 > playlist2)

    print("\n7. ADDITION")
    combined = playlist1 + playlist2
    print(combined)
    print(combined.songs)

    print("\n8. SUBTRACTION")
    remaining = playlist1 - playlist2
    print(remaining)
    print(remaining.songs)
