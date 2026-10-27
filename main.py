from models.developer import Developer
from models.manager import Manager
from models.department import Department
from models.money import Money
from models.payroll import Payroll


def main() -> None:
    department = Department("Engineering")

    developer = Developer(
        101,
        "Sai",
        60000,
        "Python",
    )

    manager = Manager(
        102,
        "Ravi",
        80000,
        5,
    )

    department.add_employee(developer)
    department.add_employee(manager)

    print(f"Department: {department.name}")
    print()

    for employee in department.list_employees():
        print(employee.display_details())
        print(employee.work())
        print()

    print(
        "Monthly payroll: "
        f"₹{department.total_monthly_payroll():,.2f}"
    )

    payroll = Payroll()
    print(
        "Developer annual salary: "
        f"₹{payroll.calculate_annual_pay(developer):,.2f}"
    )

    print()
    amount1 = Money(1000)
    amount2 = Money(2000)
    print(f"Combined money: {amount1 + amount2}")


if __name__ == "__main__":
    main()