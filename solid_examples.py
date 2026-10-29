
"""
SOLID Principles - Practical Python Examples

SOLID principles help us write code that is easier to maintain,
extend, test, and reuse.
"""


# 1. Single Responsibility Principle (SRP)
# A class should have one main responsibility.


class Invoice:
    def __init__(self, amount: float):
        self.amount = amount

    def calculate_total(self) -> float:
        """Calculate the invoice total."""
        return self.amount


class InvoicePrinter:
    def print_invoice(self, invoice: Invoice) -> None:
        """Display invoice details."""
        print(f"Invoice total: Rs. {invoice.calculate_total()}")


# 2. Open/Closed Principle (OCP)
# Code should be open for extension but closed for modification.


class Discount:
    def apply(self, amount: float) -> float:
        """Return the amount after discount."""
        return amount


class TenPercentDiscount(Discount):
    def apply(self, amount: float) -> float:
        return amount * 0.90


class TwentyPercentDiscount(Discount):
    def apply(self, amount: float) -> float:
        return amount * 0.80


# 3. Liskov Substitution Principle (LSP)
# A child class should be usable wherever its parent class is expected.


class Bird:
    def eat(self) -> str:
        return "Bird is eating"


class Sparrow(Bird):
    def eat(self) -> str:
        return "Sparrow is eating"


def feed_bird(bird: Bird) -> None:
    print(bird.eat())


# 4. Interface Segregation Principle (ISP)
# Classes should not be forced to implement methods they do not need.


class Printer:
    def print_document(self, document: str) -> str:
        return f"Printing: {document}"


class Scanner:
    def scan_document(self, document: str) -> str:
        return f"Scanning: {document}"


class MultiFunctionDevice(Printer, Scanner):
    """A device that supports both printing and scanning."""


# 5. Dependency Inversion Principle (DIP)
# High-level code should depend on an abstraction, not a specific implementation.


class MessageSender:
    def send(self, message: str) -> str:
        raise NotImplementedError


class EmailSender(MessageSender):
    def send(self, message: str) -> str:
        return f"Email sent: {message}"


class Notification:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, message: str) -> None:
        print(self.sender.send(message))


# Run all examples
if __name__ == "__main__":
    print("\n1. Single Responsibility Principle")
    invoice = Invoice(1000)
    printer = InvoicePrinter()
    printer.print_invoice(invoice)

    print("\n2. Open/Closed Principle")
    amount = 1000
    discount = TenPercentDiscount()
    print(f"Original amount: Rs. {amount}")
    print(f"After discount: Rs. {discount.apply(amount)}")

    print("\n3. Liskov Substitution Principle")
    sparrow = Sparrow()
    feed_bird(sparrow)

    print("\n4. Interface Segregation Principle")
    device = MultiFunctionDevice()
    print(device.print_document("Python notes"))
    print(device.scan_document("Python notes"))

    print("\n5. Dependency Inversion Principle")
    email_sender = EmailSender()
    notification = Notification(email_sender)
    notification.notify("Welcome to the Library!")
