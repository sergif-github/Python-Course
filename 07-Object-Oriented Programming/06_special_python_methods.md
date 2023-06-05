# Module 7: Object-Oriented Programming

## Part 6: Special Python Methods (Dunder Methods)

Special Python methods, also known as dunder methods (short for double underscore methods), are predefined methods in Python 
classes that allow customization of various operations and behaviors. These methods have a specific naming convention with 
double underscores at the beginning and end of their names. Let's explore some commonly used dunder methods:

### 6.1 `__init__()`

The `__init__()` method is used for initializing objects of a class. It is called automatically when a new object is created
from the class and allows you to set initial attributes or perform any necessary setup.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(3, 4)
```

### 6.2 __str__()

The __str__() method returns a string representation of an object. It is commonly used for providing a human-readable representation
of the object's state. It is called by the str() built-in function or when an object is printed.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

point = Point(3, 4)
print(point)   # Output: Point(3, 4)
```

### 6.3 __repr__()

The __repr__() method returns a string representation of an object that can be used to recreate the object. It is typically used
for debugging and provides a more detailed representation compared to __str__(). It is called by the repr() built-in function.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

point = Point(3, 4)
print(repr(point))   # Output: Point(3, 4)
```

### 6.4 __len__()

The __len__() method returns the length of an object. It is called by the len() built-in function and allows you to define 
the behavior of getting the length of your custom objects.

```python
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))   # Output: 5
```

### 6.5 __getitem__() and __setitem__()

The __getitem__() and __setitem__() methods are used for accessing and modifying elements of an object using indexing syntax ([]).
They allow you to define custom behavior for getting and setting values.

```python
class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

my_list = MyList([1, 2, 3, 4, 5])
print(my_list[2])     # Output: 3
my_list[2] = 10
print(my_list[2])     # Output: 10
```

### 6.6 __eq__() and __ne__()

The __eq__() and __ne__() methods are used for implementing equality and inequality comparisons between objects. They allow 
you to define custom comparison logic based on the object's attributes.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

point1 = Point(3, 4)
point2 = Point(3, 4)
print(point1 == point2)   # Output: True
print(point1 != point2)   # Output: False
```

### 6.7 Summary

In this part, you learned about special Python methods, also known as dunder methods, which allow customization of various 
operations and behaviors in classes. These methods provide hooks into built-in functions and operators, allowing you to define
custom behavior for object initialization, string representation, length, indexing, comparisons, and more.