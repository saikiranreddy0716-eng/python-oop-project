from models.employee import Employee


class Manager(Employee):
    """Represent a manager."""

    def __init__(
        self,
        employee_id: int,
        name: str,
        salary: float,
        team_size: int,
    ):
        super().__init__(employee_id, name, salary)

        if team_size < 0:
            raise ValueError("Team size cannot be negative.")

        self.team_size = team_size

    def work(self) -> str:
        return (
            f"{self.name} manages "
            f"a team of {self.team_size}."
        )