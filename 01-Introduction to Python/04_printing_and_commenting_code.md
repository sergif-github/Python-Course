# Module 1: Introduction to Python

## Part 4: Printing and commenting code

### 4.1. Printing Output with print()

In Python, the print() function is used to display output on the console or terminal. It allows you to print text, variables,
and expressions. The output is typically displayed as a new line, but you can customize the behavior using different arguments.

To print a simple text message, you can pass the message as a string to the print() function:
```python
print("Hello, World!")

Output:
Hello, World!
You can also print the values of variables by including them as arguments in the print() function:
```

```python
name = "Alice"
age = 25
print("Name:", name)
print("Age:", age)

Output:
Name: Alice
Age: 25
```

You can concatenate multiple values or variables using the + operator or format the output using string formatting techniques. 
These methods allow you to create dynamic output based on the values of variables:

```python
x = 10
y = 5
print("The sum of", x, "and", y, "is", x + y)
print("The product of {} and {} is {}".format(x, y, x * y))

Output:
The sum of 10 and 5 is 15
The product of 10 and 5 is 50
```

### 4.2. Commenting Code

Comments in Python are used to provide additional information, explanations, or disable specific lines of code. 
They are ignored by the Python interpreter and are intended for human readers.

To add a single-line comment, you can use the # symbol. Everything after the # symbol on that line is considered a comment:

```python
# This is a single-line comment
print("Hello, World!")  # This line prints the greeting
```

For multi-line comments, you can enclose the text within triple quotes (""" or '''). This is often used for docstrings, 
which provide documentation for functions, classes, or modules:

```python
"""
This is a multi-line comment.
It can span multiple lines.
"""
def greet(name):
    """This function greets the user by name."""
    print("Hello,", name)

greet("Alice")

Output:
Hello, Alice
```

### 4.3 Summary

Comments are essential for code documentation, explaining complex logic, or temporarily disabling code during development or debugging.

By utilizing the print() function and adding comments, you can effectively display output and provide clarity and context within your Python code.