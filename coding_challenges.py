
"""
OOP Coding Challenges
Ten beginner-friendly Python examples using classes and objects.
"""


# 1. Student Class
class Student:
    def __init__(self, name: str, marks: float):
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100.")
        self.name = name
        self.marks = marks

    def display(self) -> None:
        print(f"Student: {self.name}, Marks: {self.marks}")

    def get_grade(self) -> str:
        if self.marks >= 90:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 40:
            return "C"
        return "Fail"


# 2. Bank Account Class
class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def display_balance(self) -> None:
        print(f"{self.owner}'s balance: Rs. {self.balance:.2f}")


# 3. Employee Management
class Employee:
    def __init__(self, employee_id: int, name: str, salary: float):
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def display(self) -> None:
        print(
            f"ID: {self.employee_id}, "
            f"Name: {self.name}, Salary: Rs. {self.salary:.2f}"
        )


class EmployeeManager:
    def __init__(self):
        self.employees: dict[int, Employee] = {}

    def add_employee(self, employee: Employee) -> None:
        if employee.employee_id in self.employees:
            raise ValueError("Employee ID already exists.")
        self.employees[employee.employee_id] = employee

    def find_employee(self, employee_id: int) -> Employee | None:
        return self.employees.get(employee_id)

    def list_employees(self) -> None:
        if not self.employees:
            print("No employees found.")
            return
        for employee in self.employees.values():
            employee.display()


# 4. Vehicle Inheritance
class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand

    def start(self) -> str:
        return f"{self.brand} vehicle is starting."


class Car(Vehicle):
    def start(self) -> str:
        return f"{self.brand} car is starting."


class Bike(Vehicle):
    def start(self) -> str:
        return f"{self.brand} bike is starting."


# 5. Shape Area Calculator
class Shape:
    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement area().")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive.")
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius**2


# 6. Shopping Cart
class ShoppingCart:
    def __init__(self):
        self.items: dict[str, float] = {}

    def add_item(self, name: str, price: float) -> None:
        if not name.strip():
            raise ValueError("Item name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.items[name] = self.items.get(name, 0) + price

    def remove_item(self, name: str) -> None:
        if name not in self.items:
            raise ValueError("Item not found.")
        del self.items[name]

    def total(self) -> float:
        return sum(self.items.values())

    def display(self) -> None:
        if not self.items:
            print("Shopping cart is empty.")
            return
        for name, price in self.items.items():
            print(f"{name}: Rs. {price:.2f}")
        print(f"Total: Rs. {self.total():.2f}")


# 7. Movie Rating System
class Movie:
    def __init__(self, title: str):
        self.title = title
        self.ratings: list[float] = []

    def add_rating(self, rating: float) -> None:
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5.")
        self.ratings.append(rating)

    def average_rating(self) -> float | None:
        if not self.ratings:
            return None
        return sum(self.ratings) / len(self.ratings)

    def display(self) -> None:
        average = self.average_rating()
        if average is None:
            print(f"{self.title}: No ratings yet.")
        else:
            print(f"{self.title}: Average rating {average:.1f}/5")


# 8. Hospital Patient Records
class Patient:
    def __init__(self, patient_id: int, name: str, age: int):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.patient_id = patient_id
        self.name = name
        self.age = age

    def display(self) -> None:
        print(
            f"Patient ID: {self.patient_id}, "
            f"Name: {self.name}, Age: {self.age}"
        )


class PatientManager:
    def __init__(self):
        self.patients: dict[int, Patient] = {}

    def add_patient(self, patient: Patient) -> None:
        if patient.patient_id in self.patients:
            raise ValueError("Patient ID already exists.")
        self.patients[patient.patient_id] = patient

    def find_patient(self, patient_id: int) -> Patient | None:
        return self.patients.get(patient_id)

    def list_patients(self) -> None:
        if not self.patients:
            print("No patient records found.")
            return
        for patient in self.patients.values():
            patient.display()


# 9. School Result Processing
class SchoolResult:
    def __init__(self, student_name: str, marks: list[float]):
        if not marks:
            raise ValueError("At least one subject mark is required.")
        if any(mark < 0 or mark > 100 for mark in marks):
            raise ValueError("Each mark must be between 0 and 100.")
        self.student_name = student_name
        self.marks = marks

    def total(self) -> float:
        return sum(self.marks)

    def average(self) -> float:
        return self.total() / len(self.marks)

    def result(self) -> str:
        # A student passes when every subject has at least 35 marks.
        return "Pass" if all(mark >= 35 for mark in self.marks) else "Fail"

    def display(self) -> None:
        print(f"Student: {self.student_name}")
        print(f"Total: {self.total():.1f}")
        print(f"Average: {self.average():.1f}")
        print(f"Result: {self.result()}")


# 10. Online Course Management
class Course:
    def __init__(self, course_name: str):
        self.course_name = course_name
        self.students: list[str] = []

    def enroll(self, student_name: str) -> None:
        if not student_name.strip():
            raise ValueError("Student name cannot be empty.")
        if student_name in self.students:
            raise ValueError("Student is already enrolled.")
        self.students.append(student_name)

    def remove_student(self, student_name: str) -> None:
        if student_name not in self.students:
            raise ValueError("Student is not enrolled.")
        self.students.remove(student_name)

    def display(self) -> None:
        print(f"Course: {self.course_name}")
        print(f"Enrolled students: {len(self.students)}")
        for student in self.students:
            print(f"- {student}")


# Run all ten examples
def main() -> None:
    print("\n1. STUDENT CLASS")
    student = Student("Ravi", 85)
    student.display()
    print("Grade:", student.get_grade())

    print("\n2. BANK ACCOUNT")
    account = BankAccount("Ravi", 1000)
    account.deposit(500)
    account.withdraw(200)
    account.display_balance()

    print("\n3. EMPLOYEE MANAGEMENT")
    manager = EmployeeManager()
    manager.add_employee(Employee(101, "Anu", 30000))
    manager.add_employee(Employee(102, "Ravi", 35000))
    manager.list_employees()

    print("\n4. VEHICLE INHERITANCE")
    print(Car("Toyota").start())
    print(Bike("Honda").start())

    print("\n5. SHAPE AREA CALCULATOR")
    print("Rectangle area:", Rectangle(10, 5).area())
    print("Circle area:", round(Circle(7).area(), 2))

    print("\n6. SHOPPING CART")
    cart = ShoppingCart()
    cart.add_item("Book", 250)
    cart.add_item("Pen", 20)
    cart.display()

    print("\n7. MOVIE RATING SYSTEM")
    movie = Movie("Example Movie")
    movie.add_rating(4)
    movie.add_rating(5)
    movie.display()

    print("\n8. HOSPITAL PATIENT RECORDS")
    patients = PatientManager()
    patients.add_patient(Patient(1, "Sample Patient", 30))
    patients.list_patients()

    print("\n9. SCHOOL RESULT PROCESSING")
    result = SchoolResult("Anu", [80, 75, 90])
    result.display()

    print("\n10. ONLINE COURSE MANAGEMENT")
    course = Course("Python Basics")
    course.enroll("Ravi")
    course.enroll("Anu")
    course.display()


if __name__ == "__main__":
    main()
