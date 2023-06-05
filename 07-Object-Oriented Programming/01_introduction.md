# Module 7: Object-Oriented Programming

## Part 1: Introduction to Classes and Objects

Object-oriented programming (OOP) is a programming paradigm that organizes code into objects, which are instances of classes.
Classes define the structure and behavior of objects, and objects are used to interact with and manipulate data. 
Let's explore the fundamentals of classes and objects in Python:

### 1.1 Classes and Objects

In Python, a class is a blueprint for creating objects. It defines the properties and methods that objects of that class 
will have. Objects, on the other hand, are instances of a class. They represent specific entities or concepts in your program.
Here's an example:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"The {self.brand} {self.model} is driving.")

car1 = Car("Toyota", "Camry")
car1.drive()
```

In this example, we define a Car class with two properties: brand and model. The __init__() method is a special method 
called the constructor, which is executed when an object is created. It initializes the brand and model properties of 
the object using the values passed as arguments. The drive() method is a behavior associated with the Car class that allows
the object to perform the action of driving. We create an instance of the Car class called car1, passing the brand "Toyota"
and the model "Camry" as arguments. Finally, we call the drive() method on the car1 object, which prints the driving message.

### 1.2 Encapsulation and Abstraction

OOP provides two important principles: encapsulation and abstraction. Encapsulation refers to the bundling of data and methods within a class. It allows us to control the access to the internal state of an object. Abstraction, on the other hand, focuses on exposing only essential information and hiding unnecessary details. It allows us to create more understandable and maintainable code.

### 1.3 Summary

In this part, you learned the basics of classes and objects in Python. Classes serve as blueprints for creating objects, which are instances of those classes. Objects encapsulate data and behavior, allowing us to interact with and manipulate data in a structured way. OOP promotes encapsulation and abstraction, which improve code organization, readability, and maintainability.