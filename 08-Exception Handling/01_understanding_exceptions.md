## Module 8: Exception Handling

### Part 1: Understanding Exceptions

In Python, an exception is an error that occurs during the execution of a program. When an exception occurs, it disrupts the normal
flow of the program and can cause the program to terminate if not handled properly. Understanding exceptions is crucial for writing 
robust and error-tolerant code.

#### 1.1 What is an Exception?

An exception is a Python object that represents an error condition. It can be raised (generated) by the interpreter or by the programmer
to indicate that something unexpected or erroneous has happened. Exceptions can occur due to various reasons, such as invalid input,
division by zero, file not found, or network errors.

#### 1.2 Exception Handling

Exception handling is the process of catching and handling exceptions in a program. It allows you to gracefully handle errors, 
prevent program crashes, and provide meaningful error messages to users. By handling exceptions, you can recover from errors or take 
alternative actions to ensure that your program continues running.

#### 1.3 The Exception Hierarchy

In Python, exceptions are organized in a hierarchical structure. At the top of the hierarchy is the `BaseException` class, which 
is the superclass of all built-in exceptions. Derived from `BaseException`, there are several built-in exception classes such as 
`Exception`, `TypeError`, `ValueError`, and `FileNotFoundError`. You can also create your own custom exception classes by subclassing 
the built-in exception classes.

#### 1.4 The try-except Block

To handle exceptions, you use the `try-except` block. The `try` block contains the code that might raise an exception, and the `except`
block specifies the code to be executed if a specific exception occurs. Multiple `except` blocks can be used to handle different types
of exceptions. Additionally, you can include an optional `else` block that executes when no exceptions occur in the `try` block, 
and a `finally` block that always executes regardless of whether an exception was raised or not.

```python
try:
    # Code that might raise an exception
    # ...
except ExceptionType1:
    # Exception handling code for ExceptionType1
    # ...
except ExceptionType2:
    # Exception handling code for ExceptionType2
    # ...
else:
    # Code that executes if no exceptions occur
    # ...
finally:
    # Code that always executes
    # ...
```

#### 1.5 Raising Exceptions
In addition to handling exceptions raised by the interpreter or external libraries, you can also raise your own exceptions using 
the raise statement. This allows you to indicate that a specific error condition has occurred in your code.

```python
raise ExceptionType("Error message")
```

#### 1.6 Summary
Understanding exceptions and how to handle them is essential for writing robust Python programs. Exceptions allow you to handle errors,
recover from unexpected situations, and ensure the smooth execution of your code. By using the try-except block, you can catch and 
handle exceptions, preventing your program from crashing and providing better user experience.