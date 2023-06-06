# Module 6: Object-Oriented Programming

## Part 5: Inheritance and Polymorphism

Inheritance and polymorphism are key concepts in object-oriented programming that allow for code reuse, extensibility, and flexibility.
Let's explore these concepts in more detail:

### 5.1 Inheritance

Inheritance is a mechanism that allows a class to inherit the properties and methods of another class. The class that is being 
inherited from is called the **base class** or **superclass**, while the class that inherits from the base class is called the 
**derived class** or **subclass**. Inheritance promotes code reuse and allows the derived class to add or modify functionality 
from the base class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement the speak method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.name)      # Output: Buddy
print(dog.speak())   # Output: Woof!
print(cat.name)      # Output: Whiskers
print(cat.speak())   # Output: Meow!
```

In this example, the Animal class is the base class, and the Dog and Cat classes are derived from it. Both the Dog and Cat classes 
inherit the name attribute and the speak() method from the Animal class. However, each subclass provides its own implementation
of the speak() method, resulting in different behaviors.

### 5.2 Polymorphism

Polymorphism refers to the ability of objects to take on multiple forms. In the context of inheritance, polymorphism allows objects 
of different classes that share a common base class to be treated as objects of the base class. This means that a function or method
can work with objects of different types, as long as they are derived from the same base class.

```python
def make_speak(animal):
    print(animal.speak())

dog = Dog("Buddy")
cat = Cat("Whiskers")

make_speak(dog)     # Output: Woof!
make_speak(cat)     # Output: Meow!
```

In this example, the make_speak() function can take both Dog and Cat objects as arguments because they are derived from the common
base class Animal. This demonstrates polymorphism, where the same function can work with objects of different types as long as they
adhere to a common interface.

### 5.3 Summary

In this part, you learned about inheritance and polymorphism in object-oriented programming. Inheritance allows a class to inherit
properties and methods from a base class, promoting code reuse and extensibility. Polymorphism enables objects of different types 
but derived from a common base class to be treated interchangeably, providing flexibility and reusability.