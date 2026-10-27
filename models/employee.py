from abc import ABC, abstractmethod


class Employee(ABC):
    """Base class for all employees."""

    def __init__(self, employee_id: int, name: str, salary: float):
        if employee_id <= 0:
            raise ValueError("Employee ID must be positive.")

        if not name.strip():
            raise ValueError("Employee name cannot be empty.")

        if salary < 0:
            raise ValueError("Salary cannot be negative.")

        self.employee_id = employee_id
        self.name = name
        self._salary = float(salary)

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        if value < 0:
            raise ValueError("Salary cannot be negative.")

        self._salary = float(value)

    def display_details(self) -> str:
        return (
            f"ID: {self.employee_id}, "
            f"Name: {self.name}, "
            f"Salary: ₹{self.salary:,.2f}"
        )

    @abstractmethod
    def work(self) -> str:
        """Describe the employee's work."""
        raise NotImplementedError