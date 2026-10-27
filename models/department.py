from models.employee import Employee
from models.payroll import Payroll


class Department:
    """Manage employees in a department."""

    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("Department name cannot be empty.")

        self.name = name
        self._employees: list[Employee] = []
        self._payroll = Payroll()

    def add_employee(self, employee: Employee) -> None:
        for existing in self._employees:
            if existing.employee_id == employee.employee_id:
                raise ValueError("Duplicate employee ID.")

        self._employees.append(employee)

    def list_employees(self) -> list[Employee]:
        return self._employees.copy()

    def total_monthly_payroll(self) -> float:
        return sum(
            self._payroll.calculate_monthly_pay(employee)
            for employee in self._employees
        )