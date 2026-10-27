from models.employee import Employee


class EmployeeService:
    """Provide employee management operations."""

    def __init__(self) -> None:
        self._employees: dict[int, Employee] = {}

    def add_employee(self, employee: Employee) -> None:
        if employee.employee_id in self._employees:
            raise ValueError("Employee ID already exists.")

        self._employees[employee.employee_id] = employee

    def get_employee(self, employee_id: int) -> Employee:
        try:
            return self._employees[employee_id]
        except KeyError:
            raise ValueError("Employee not found.") from None

    def list_employees(self) -> list[Employee]:
        return list(self._employees.values())