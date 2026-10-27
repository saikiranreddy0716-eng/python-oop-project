from dataclasses import dataclass


@dataclass(frozen=True)
class Money:
    """Represent money in a specific currency."""

    amount: float
    currency: str = "INR"

    def __post_init__(self) -> None:
        if self.amount < 0:
            raise ValueError("Money amount cannot be negative.")

        if not self.currency.strip():
            raise ValueError("Currency cannot be empty.")

    def __add__(self, other: object) -> "Money":
        if not isinstance(other, Money):
            return NotImplemented

        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies.")

        return Money(
            self.amount + other.amount,
            self.currency,
        )

    def __str__(self) -> str:
        return f"{self.currency} {self.amount:,.2f}"