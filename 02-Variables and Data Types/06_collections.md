# Module 2: Variables and Data Types

## Part 6: Working with Collections

In Python, collections are data structures used to store multiple values together. There are several built-in collection types that provide different functionalities for organizing and manipulating data.

### 6.1 Lists

A list is an ordered collection that can contain elements of different data types. Lists are mutable, meaning that you can modify their elements after they are created. Lists are defined by enclosing elements in square brackets (`[]`) and separating them with commas. For example:

```python
fruits = ['apple', 'banana', 'cherry']
numbers = [1, 2, 3, 4, 5]
mixed = [1, 'apple', True]

print(fruits)  # Output: ['apple', 'banana', 'cherry']
print(numbers)  # Output: [1, 2, 3, 4, 5]
print(mixed)  # Output: [1, 'apple', True]
```

Lists support various operations and methods for adding, removing, and modifying elements.

### 6.2 Tuples

A tuple is an ordered collection similar to a list, but tuples are immutable, meaning that their elements cannot be modified once they are created. Tuples are defined by enclosing elements in parentheses (()) and separating them with commas. For example:

```python
coordinates = (3, 4)
person = ('John', 25, 'Engineer')

print(coordinates)  # Output: (3, 4)
print(person)  # Output: ('John', 25, 'Engineer')
```

Tuples are often used to represent a collection of related values that should not be modified.

### 6.3 Sets

A set is an unordered collection of unique elements. Sets are mutable, and you can add or remove elements from them. Sets are defined by enclosing elements in curly braces ({}) or using the set() constructor. For example:

```python
fruits = {'apple', 'banana', 'cherry'}
numbers = set([1, 2, 3, 4, 5])

print(fruits)  # Output: {'apple', 'banana', 'cherry'}
print(numbers)  # Output: {1, 2, 3, 4, 5}
```

Sets are useful for operations such as finding unique elements, set operations (union, intersection, difference), and membership testing.

### 6.4 Dictionaries
A dictionary is an unordered collection of key-value pairs. Each value is associated with a unique key, allowing for efficient retrieval of values based on their keys. Dictionaries are defined by enclosing key-value pairs in curly braces ({}) or using the dict() constructor. For example:

```python
person = {'name': 'John', 'age': 25, 'occupation': 'Engineer'}

print(person)  # Output: {'name': 'John', 'age': 25, 'occupation': 'Engineer'}
```

Dictionaries are commonly used for storing and retrieving data based on specific keys.

### 6.5 Summary

In this part, you explored different types of collections in Python, including lists, tuples, sets, and dictionaries. Each collection type has its own characteristics and use cases. Understanding collections is essential for organizing and manipulating data effectively in your programs.