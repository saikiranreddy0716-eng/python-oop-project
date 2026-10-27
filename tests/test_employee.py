import pytest

from models.developer import Developer
from models.manager import Manager
from models.department import Department
from models.money import Money
from services.employee_service import EmployeeService


def test_developer_work() -> None:
    developer = Developer(101, "Sai", 60000, "Python")
    assert developer.work() == "Sai writes Python code."


def test_manager_work() -> None:
    manager = Manager(102, "Ravi", 80000, 5)
    assert manager.work() == "Ravi manages a team of 5."


def test_negative_salary_is_rejected() -> None:
    with pytest.raises(ValueError):
        Developer(101, "Sai", -1000, "Python")


def test_duplicate_employee_is_rejected() -> None:
    department = Department("Engineering")
    employee = Developer(101, "Sai", 60000, "Python")

    department.add_employee(employee)

    with pytest.raises(ValueError):
        department.add_employee(employee)


def test_employee_service_search() -> None:
    service = EmployeeService()
    employee = Developer(101, "Sai", 60000, "Python")

    service.add_employee(employee)

    assert service.get_employee(101) is employee


def test_missing_employee_is_rejected() -> None:
    service = EmployeeService()

    with pytest.raises(ValueError, match="Employee not found"):
        service.get_employee(999)


def test_department_payroll() -> None:
    department = Department("Engineering")
    department.add_employee(Developer(101, "Sai", 60000, "Python"))
    department.add_employee(Manager(102, "Ravi", 80000, 5))

    assert department.total_monthly_payroll() == 140000


def test_money_addition() -> None:
    result = Money(1000) + Money(2000)

    assert result == Money(3000)


def test_different_currencies_cannot_be_added() -> None:
    with pytest.raises(ValueError):
        Money(1000, "INR") + Money(20, "USD")