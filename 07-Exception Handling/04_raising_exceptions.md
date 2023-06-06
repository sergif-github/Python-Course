# Module 7: Exception Handling

## Part 4: Raising Exceptions

In Python, you can raise exceptions explicitly to indicate that an error or exceptional condition has occurred during the execution
of your code. This can be useful when you want to handle specific situations or enforce certain conditions.

### 4.1 Raising Exceptions

To raise an exception, you use the `raise` statement followed by an instance of an exception class or an exception object. 
Here's the basic syntax:

```python
raise ExceptionType("Error message")
```

For example, to raise a ValueError exception with a custom error message, you can write:

```python
raise ValueError("Invalid input. Please enter a positive number.")
```

When an exception is raised, the program flow is interrupted, and the raised exception is propagated up the call stack until 
it is caught by an appropriate except block.

### 4.2 Custom Exceptions

In addition to built-in exceptions, you can also create your own custom exception classes to represent specific types of 
errors or exceptional conditions in your code. Custom exceptions can provide more meaningful error messages and allow you to 
handle specific situations with greater control.

To create a custom exception, you typically define a new class that inherits from the Exception class or one of its subclasses. 
Here's an example:

```python
class CustomException(Exception):
    pass
```

You can then raise instances of your custom exception class using the same raise statement:

```python
raise CustomException("Custom error message")
```

By raising a custom exception, you can signal specific errors or exceptional conditions in your code and handle them appropriately.

### 4.3 Raising Exceptions in Conditional Statements

Raising exceptions can be particularly useful when certain conditions are not met in your code. For example, you can raise an exception
if a function receives invalid input or encounters an unexpected situation. By raising an exception, you can notify the caller 
of the function or the surrounding code that an error has occurred.

Here's an example that demonstrates raising an exception in a conditional statement:

```python
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
```

In the above example, if the y value is 0, a ValueError exception is raised with the corresponding error message. This ensures that
the function does not perform an invalid division operation.

### 4.4 Summary

Raising exceptions allows you to explicitly indicate errors or exceptional conditions in your code. By raising built-in or custom
exceptions, you can handle specific situations, enforce conditions, and provide meaningful error messages. When an exception is raised,
the program flow is interrupted and the raised exception is propagated up the call stack until it is caught by an appropriate except block.
