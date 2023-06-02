# Module 2: Variables and Data Types

## Part 4: Boolean Data Type

In Python, the `bool` data type represents Boolean values, which can have two possible states: `True` or `False`. Booleans are often used in programming for logical operations, decision-making, and comparisons.

### 4.1 Boolean Values

The Boolean values `True` and `False` are keywords in Python and are used to represent the concept of truth or falsehood. For example:

```python
is_raining = True
is_sunny = False
```

Boolean values are commonly used in conditional statements and logical operations to determine the flow of the program based on certain conditions.

### 4.2 Comparison Operators

Python provides various comparison operators that can be used to compare values and produce Boolean results. Some commonly used comparison operators include:

- == (equal to)
- != (not equal to)
- \> (greater than)
- < (less than)
- \>= (greater than or equal to)
- <= (less than or equal to)

These operators compare two values and return True or False based on the comparison result. For example:

```python
x = 10
y = 5

result1 = x > y  # True
result2 = x == y  # False
result3 = x != y  # True
```

### 4.3 Logical Operators

Python also provides logical operators that can be used to combine multiple Boolean values or expressions. The three logical operators are:

- and (logical AND)
- or (logical OR)
- not (logical NOT)

These operators allow you to perform logical operations on Boolean values and produce Boolean results. For example:

```python
Copy code
x = 10
y = 5

result1 = x > 0 and y > 0  # True
result2 = x > 10 or y > 10  # False
result3 = not(x > y)  # False
```

### 4.4 Summary

In this part, you explored the Boolean data type in Python. Booleans represent truth or falsehood and are commonly used in conditional statements, logical operations, and comparisons. Understanding Boolean values and operators is essential for decision-making and controlling the flow of your programs.