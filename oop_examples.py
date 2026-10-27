
"""
Story 2 - OOP Implementation in Python

This file demonstrates:
1. Encapsulation
2. Single inheritance
3. Multiple inheritance
4. Multilevel inheritance
5. Hierarchical inheritance
6. Polymorphism and method overriding
7. Method overloading using default arguments
8. Composition
9. Aggregation
"""


# --------------------------------------------------
# 1. ENCAPSULATION
# --------------------------------------------------
# Encapsulation ante data and methods ni oka class lo
# organize cheyyadam, data access ni control cheyyadam.


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = balance  # Name-mangled attribute

    def deposit(self, amount: float) -> None:
        # Deposit amount positive ga undali.
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        # Withdraw amount valid ga undali.
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.__balance:
            raise ValueError("Insufficient balance.")

        self.__balance -= amount

    def get_balance(self) -> float:
        # Balance ni method dwara access chestham.
        return self.__balance


print("\n--- 1. Encapsulation ---")

account = BankAccount("Ravi", 1000)
account.deposit(500)
account.withdraw(200)

print("Account owner:", account.owner)
print("Account balance:", account.get_balance())


# --------------------------------------------------
# 2. SINGLE INHERITANCE
# --------------------------------------------------
# Single inheritance lo oka child class,
# oka parent class nunchi inherit cheskuntundi.


class Person:
    def __init__(self, name: str):
        self.name = name

    def introduce(self) -> str:
        return f"My name is {self.name}."


class Student(Person):
    # Student class, Person class nunchi inherit chesthundi.
    def study(self) -> str:
        return f"{self.name} is studying."


print("\n--- 2. Single Inheritance ---")

student = Student("Priya")
print(student.introduce())  # Parent class method
print(student.study())      # Child class method


# --------------------------------------------------
# 3. MULTIPLE INHERITANCE
# --------------------------------------------------
# Multiple inheritance lo oka child class
# multiple parent classes nunchi inherit cheskuntundi.


class Flyer:
    def fly(self) -> str:
        return "Flying in the sky."


class Swimmer:
    def swim(self) -> str:
        return "Swimming in the water."


class Duck(Flyer, Swimmer):
    # Duck class rendu parent classes methods ni use chesthundi.
    pass


print("\n--- 3. Multiple Inheritance ---")

duck = Duck()
print(duck.fly())
print(duck.swim())


# --------------------------------------------------
# 4. MULTILEVEL INHERITANCE
# --------------------------------------------------
# Multilevel inheritance chain laga untundi:
# Grandparent -> Parent -> Child


class Animal:
    def eat(self) -> str:
        return "Animal is eating."


class Mammal(Animal):
    def walk(self) -> str:
        return "Mammal is walking."


class Dog(Mammal):
    def bark(self) -> str:
        return "Dog is barking."


print("\n--- 4. Multilevel Inheritance ---")

dog = Dog()
print(dog.eat())   # Animal nunchi inherited
print(dog.walk())  # Mammal method
print(dog.bark())  # Dog method


# --------------------------------------------------
# 5. HIERARCHICAL INHERITANCE
# --------------------------------------------------
# Hierarchical inheritance lo multiple child classes
# same parent class nunchi inherit cheskuntayi.


class Employee:
    def __init__(self, name: str):
        self.name = name

    def show_name(self) -> str:
        return f"Employee name: {self.name}"


class Developer(Employee):
    def write_code(self) -> str:
        return f"{self.name} is writing code."


class Manager(Employee):
    def manage_team(self) -> str:
        return f"{self.name} is managing the team."


print("\n--- 5. Hierarchical Inheritance ---")

developer = Developer("Arun")
manager = Manager("Kiran")

print(developer.show_name())
print(developer.write_code())

print(manager.show_name())
print(manager.manage_team())


# --------------------------------------------------
# 6. POLYMORPHISM AND METHOD OVERRIDING
# --------------------------------------------------
# Polymorphism ante same method call different objects ki
# different behavior ivvadam.
#
# Method overriding ante child class lo parent class
# method ki own implementation ivvadam.


class Notification:
    def send(self) -> str:
        return "Sending a general notification."


class EmailNotification(Notification):
    def send(self) -> str:
        # Parent send() method ni override chesthunnam.
        return "Sending an email notification."


class SMSNotification(Notification):
    def send(self) -> str:
        # Same method, different behavior.
        return "Sending an SMS notification."


print("\n--- 6. Polymorphism and Method Overriding ---")

notifications = [
    Notification(),
    EmailNotification(),
    SMSNotification(),
]

for notification in notifications:
    print(notification.send())


# --------------------------------------------------
# 7. METHOD OVERLOADING USING DEFAULT ARGUMENTS
# --------------------------------------------------
# Python lo traditional method overloading laga same name
# tho multiple method definitions use cheyyalem.
# Default arguments use chesi different number of inputs
# accept cheyyachu.


class Calculator:
    def add(self, a: float, b: float = 0, c: float = 0) -> float:
        # One, two, or three numbers add cheyyachu.
        return a + b + c


print("\n--- 7. Method Overloading Using Default Arguments ---")

calculator = Calculator()

print("One number:", calculator.add(10))
print("Two numbers:", calculator.add(10, 20))
print("Three numbers:", calculator.add(10, 20, 30))


# --------------------------------------------------
# 8. COMPOSITION
# --------------------------------------------------
# Composition ante oka object, vere object ni contain chesthundi.
# Ee example lo Car object, Engine object ni create chesi
# use chesthundi.


class Engine:
    def start(self) -> str:
        return "Engine started."


class Car:
    def __init__(self):
        # Car object tana Engine object ni create chesthundi.
        self.engine = Engine()

    def start_car(self) -> str:
        return self.engine.start() + " Car is ready."


print("\n--- 8. Composition ---")

car = Car()
print(car.start_car())


# --------------------------------------------------
# 9. AGGREGATION
# --------------------------------------------------
# Aggregation ante oka object, already existing object ni
# receive chesi use chesthundi.
# Ee example lo Department, external ga create chesina
# Employee object ni receive chesthundi.


class TeamEmployee:
    def __init__(self, name: str):
        self.name = name


class Department:
    def __init__(self, name: str, employee: TeamEmployee):
        self.name = name
        self.employee = employee

    def show_member(self) -> str:
        return (
            f"{self.employee.name} works in "
            f"{self.name} department."
        )


print("\n--- 9. Aggregation ---")

# Employee object ni separate ga create chesthunnam.
team_employee = TeamEmployee("Sneha")

# Existing employee object ni Department ki pass chesthunnam.
department = Department("Engineering", team_employee)

print(department.show_member())
