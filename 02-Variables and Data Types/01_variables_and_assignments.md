# Module 2: Variables and Data Types

## Part 1: Variables and Assignments

In Python, variables are used to store data values. A variable is like a container that holds a value, which can be of different types such as numbers, strings, or other objects. Assigning a value to a variable is known as variable assignment.

### 1.1 Variable Names

When choosing variable names, there are a few rules to follow:

- Variable names can only contain letters (a-z, A-Z), digits (0-9), and underscores (_). They cannot start with a digit.
- Variable names are case-sensitive. For example, `myVariable` and `myvariable` are different variables.
- Variable names should be descriptive and meaningful, helping to understand the purpose of the variable.

Here are some valid variable names:

```python
age = 25
name = "Alice"
is_student = True
```

Variable Assignment
In Python, you can assign a value to a variable using the = operator. The variable on the left side of the = sign is assigned the value on the right side. For example:

```python
x = 10
y = 5.5
message = "Hello, World!"
```

You can also assign multiple variables in a single line:
```python
a, b, c = 1, 2, 3
```

Variable Reassignment
In Python, you can change the value of a variable by assigning a new value to it. This is known as variable reassignment. For example:

```python
x = 10
print(x)  # Output: 10

x = 20
print(x)  # Output: 20
```

When you reassign a variable, the new value overwrites the previous value stored in that variable.

### 1.2 Printing Variables
To display the value of a variable, you can use the print() function. This allows you to see the current value stored in a variable during program execution. For example:

```python
Copy code
name = "Alice"
print(name)  # Output: Alice

age = 25
print("Age:", age)  # Output: Age: 25
The print() function can take one or more arguments, separated by commas. It converts each argument to a string and displays it on the console.
```

### 1.3 Summary

In this part, you learned about variables, variable names, variable assignment, variable reassignment, and printing variables. Variables are fundamental in Python programming as they allow you to store and manipulate data dynamically.