from models.employee import Employee


class Developer(Employee):
    """Represent a software developer."""

    def __init__(
        self,
        employee_id: int,
        name: str,
        salary: float,
        programming_language: str,
    ):
        super().__init__(employee_id, name, salary)

        if not programming_language.strip():
            raise ValueError("Programming language cannot be empty.")

        self.programming_language = programming_language

    def work(self) -> str:
        return (
            f"{self.name} writes "
            f"{self.programming_language} code."
        )