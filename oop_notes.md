
# Story 1 – Python OOP Fundamentals

## 1. Introduction to OOP

Object-Oriented Programming (OOP) is a programming approach based on classes and objects.

OOP helps us organize code, reuse existing code, and represent real-world things in a program.

### Real-world example

A car has properties and behaviors.

Properties:
- Brand
- Color
- Speed

Behaviors:
- Start
- Stop
- Accelerate

In Python, we can represent a car using a class.

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.brand} car is starting.")


car1 = Car("Toyota", "White")
car1.start()
```

Output:

```text
Toyota car is starting.
```

## 2. Classes and Objects

### Class

A class is a blueprint used to create objects.

Example: `Car` is a class.

### Object

An object is an instance of a class.

Example: `car1` is an object created from the `Car` class.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = Student("Ravi", 85)
student2 = Student("Priya", 92)

print(student1.name)
print(student2.name)
```

Output:

```text
Ravi
Priya
```

### Diagram

```text
             Student Class
                  |
          -------------------
          |                 |
      student1           student2
      Ravi, 85            Priya, 92
```

### Real-world example

Student is a class. Each individual student is an object.

## 3. Constructors: __init__()

A constructor-like initialization method in Python is `__init__()`.

It runs automatically when an object is created and initializes the object's attributes.

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee1 = Employee("Ravi", 30000)

print(employee1.name)
print(employee1.salary)
```

Output:

```text
Ravi
30000
```

### Important points

- `__init__()` runs automatically after a new instance is created.
- It initializes object attributes.
- `self` refers to the current instance.
- Python's `__new__()` method is responsible for creating the instance; `__init__()` initializes it.

### Real-world example

When an employee record is created, the employee name and salary can be initialized using `__init__()`.

## 4. Instance Variables and Class Variables

### Instance variables

Instance variables belong to an individual object.

Different objects can have different values.

### Class variables

Class variables are defined inside the class but outside instance methods. They are shared through the class unless an instance overrides the attribute.

```python
class Employee:
    company = "ABC Technologies"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee1 = Employee("Ravi", 30000)
employee2 = Employee("Priya", 40000)

print(employee1.name)
print(employee2.name)
print(employee1.company)
print(employee2.company)
```

Output:

```text
Ravi
Priya
ABC Technologies
ABC Technologies
```

Here:
- `name` and `salary` are instance variables.
- `company` is a class variable.

### Comparison

| Instance Variable | Class Variable |
|---|---|
| Belongs to an individual object | Defined on the class |
| Can differ for each object | Commonly shared across instances |
| Usually assigned through `self` | Usually defined directly in the class body |
| Example: employee name | Example: company name |

### Important note

Avoid changing a mutable class variable, such as a list, through one instance when you intend each object to have its own list. Use an instance variable for per-object data.

## 5. Instance Methods

Instance methods work with a particular object.

They use `self` as the first parameter.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")


student = Student("Ravi", 85)
student.display()
```

Output:

```text
Name: Ravi
Marks: 85
```

Use instance methods when the operation needs an object's data.

## 6. Class Methods

Class methods work with the class itself and receive `cls` as their first parameter.

Use the `@classmethod` decorator to define a class method.

```python
class Employee:
    company = "ABC Technologies"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


employee = Employee("Ravi")

Employee.change_company("XYZ Technologies")

print(employee.company)
```

Output:

```text
XYZ Technologies
```

### When to use class methods

- To update class-level information.
- To create alternative constructors.
- To perform operations that logically belong to the class rather than one specific object.

## 7. Static Methods

Static methods do not automatically receive `self` or `cls`.

Use the `@staticmethod` decorator.

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b


result = Calculator.add(10, 20)
print(result)
```

Output:

```text
30
```

### When to use static methods

Use them for utility operations related to the class that do not need instance or class state.

## 8. self and cls

### self

`self` refers to the current object.

It allows an instance method to access that object's attributes and other instance methods.

### cls

`cls` refers to the class passed to a class method.

It allows a class method to access or update class-level attributes.

```python
class Example:
    category = "General"

    def __init__(self, name):
        self.name = name

    def show_name(self):
        return self.name

    @classmethod
    def show_category(cls):
        return cls.category


item = Example("Laptop")

print(item.show_name())
print(Example.show_category())
```

Output:

```text
Laptop
General
```

### Comparison

| self | cls |
|---|---|
| Refers to the current instance | Refers to the class |
| Used in instance methods | Used in class methods |
| Accesses instance attributes | Accesses class-level attributes |
| Convention, not a Python keyword | Convention, not a Python keyword |

Python passes `self` and `cls` automatically when the corresponding methods are called on an instance or class.

## 9. Instance, Class, and Static Methods Compared

| Feature | Instance Method | Class Method | Static Method |
|---|---|---|---|
| Decorator | None required | `@classmethod` | `@staticmethod` |
| First parameter | `self` | `cls` | No automatic first parameter |
| Main purpose | Work with an object | Work with class-level data | Utility operation |
| Access instance data directly | Yes | No, not without an instance | No, not automatically |
| Access class data through parameter | Via `self` | Via `cls` | No automatic class reference |

## 10. Object Lifecycle

The object lifecycle describes the stages an object passes through.

### Main stages

1. Class definition: Python defines the class.
2. Object creation: `__new__()` creates an instance.
3. Initialization: `__init__()` initializes the instance.
4. Usage: The program accesses attributes and calls methods.
5. Cleanup: When an object is no longer referenced, it may become eligible for garbage collection.

### Diagram

```text
Class Definition
      |
      v
Object Creation (__new__)
      |
      v
Initialization (__init__)
      |
      v
Object Used
      |
      v
No Longer Referenced
      |
      v
Eligible for Garbage Collection
```

### Example

```python
class Demo:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} object initialized")


obj = Demo("Sample")
print(obj.name)

del obj
```

Possible output:

```text
Sample object initialized
Sample
```

`del obj` removes the name `obj`; it does not guarantee that the object is immediately destroyed. If other references exist, the object can remain alive.

## 11. Real-World Example: Employee Management

```python
class Employee:
    company = "ABC Technologies"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        return f"{self.name} earns {self.salary}"

    @classmethod
    def company_name(cls):
        return cls.company

    @staticmethod
    def is_valid_salary(salary):
        return salary >= 0


employee1 = Employee("Ravi", 30000)
employee2 = Employee("Priya", 40000)

print(employee1.display())
print(employee2.display())
print(Employee.company_name())
print(Employee.is_valid_salary(30000))
```

Output:

```text
Ravi earns 30000
Priya earns 40000
ABC Technologies
True
```

This example demonstrates:
- Class and objects
- Constructor
- Instance variables
- Class variable
- Instance method
- Class method
- Static method

## 12. Summary

- A class is a blueprint for creating objects.
- An object is an instance of a class.
- `__init__()` initializes an object.
- Instance variables store object-specific data.
- Class variables store class-level data.
- Instance methods use `self`.
- Class methods use `cls`.
- Static methods are utility methods that need no automatic instance or class reference.
- Objects can become eligible for garbage collection when no references keep them alive.

These fundamentals provide the foundation for inheritance, encapsulation, abstraction, polymorphism, and larger Python applications.
