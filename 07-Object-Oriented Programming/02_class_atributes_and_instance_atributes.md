# Module 7: Object-Oriented Programming

## Part 2: Class Attributes and Instance Attributes

In Python, classes can have attributes that are shared by all instances of the class (class attributes) and attributes that
are unique to each instance (instance attributes). Understanding the difference between class attributes and instance attributes
is crucial for effective object-oriented programming. Let's explore these concepts in more detail:

### 2.1 Class Attributes

Class attributes are defined within the class but outside of any methods. They are shared by all instances of the class. 
Here's an example:

```python
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.pi * self.radius * self.radius

circle1 = Circle(5)
circle2 = Circle(3)

print(circle1.pi)  # Output: 3.14159
print(circle2.pi)  # Output: 3.14159
```

In this example, the pi attribute is a class attribute. It is defined directly within the Circle class. Both circle1 and circle2
instances can access and use the same value of pi.

### 2.2 Instance Attributes

Instance attributes are unique to each instance of the class. They are defined within the __init__() method and are specific
to the object being created. Here's an example:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

rectangle1 = Rectangle(4, 6)
rectangle2 = Rectangle(3, 5)

print(rectangle1.width)  # Output: 4
print(rectangle2.width)  # Output: 3
```

In this example, the width and height attributes are instance attributes. Each instance of the Rectangle class can have different
values for these attributes.

### 2.3 Accessing Attributes

To access class attributes and instance attributes, you use dot notation. For class attributes, you can access them using
the class name or any instance of the class. For instance attributes, you access them using the instance name. 
Here's an example:

```python
class Person:
    species = "Human"

    def __init__(self, name):
        self.name = name

person1 = Person("Alice")
person2 = Person("Bob")

print(Person.species)     # Output: Human
print(person1.species)    # Output: Human
print(person2.species)    # Output: Human
print(person1.name)       # Output: Alice
print(person2.name)       # Output: Bob
```

In this example, the species attribute is a class attribute, and the name attribute is an instance attribute. Both can be accessed
using the class name or any instance of the class.

### 2.4 Summary

In this part, you learned about class attributes and instance attributes in Python. Class attributes are shared by all instances 
of the class, while instance attributes are unique to each instance. Understanding the distinction between these attributes 
is essential for building flexible and efficient object-oriented programs.