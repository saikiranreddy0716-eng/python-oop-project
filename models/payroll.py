class Payroll:
    """Calculate employee salary amounts."""

    def calculate_monthly_pay(self, employee) -> float:
        return employee.salary

    def calculate_annual_pay(self, employee) -> float:
        return employee.salary * 12