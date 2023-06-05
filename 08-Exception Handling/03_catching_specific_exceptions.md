# Module 8: Exception Handling

## Part 3: Catching Specific Exceptions

In Python, you can catch and handle specific exceptions by specifying the exception type in the `except` block. This allows you
to customize the error handling for different types of exceptions that may occur in your code.

### 3.1 Catching a Specific Exception

To catch a specific exception, you specify the exception type after the `except` keyword. If the raised exception matches the
specified type, the corresponding `except` block is executed. Here's the syntax:

```python
try:
    # Code that might raise an exception
    # ...
except ExceptionType:
    # Exception handling code for the specific exception
    # ...
```

For example, if you want to handle a ValueError, you can write the following code:

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age. Please enter a valid integer.")
```

In the above example, if the user enters a non-integer value for the age, a ValueError will be raised, and the corresponding except
ValueError block will be executed, displaying the error message.

### 3.2 Catching Multiple Specific Exceptions

You can handle multiple specific exceptions by using multiple except blocks. Each except block can handle a specific type of exception. 
The first except block that matches the raised exception type will be executed, and subsequent except blocks will be skipped. Here's an example:

```python
try:
    # Code that might raise an exception
    # ...
except ValueError:
    # Exception handling code for ValueError
    # ...
except TypeError:
    # Exception handling code for TypeError
    # ...
```

In the above example, if a ValueError occurs, the first except ValueError block will be executed. If a TypeError occurs, the second 
except TypeError block will be executed.

### 3.3 Catching Multiple Specific Exceptions with a Single Except Block

If you want to handle multiple exceptions with the same handling code, you can specify multiple exception types within a single
except block. This can be useful when you want to provide the same error handling logic for different types of exceptions. 
Here's an example:

```python
try:
    # Code that might raise an exception
    # ...
except (ValueError, TypeError):
    # Exception handling code for ValueError and TypeError
    # ...
```

In the above example, if either a ValueError or a TypeError occurs, the except (ValueError, TypeError) block will be executed.

### 3.4 Handling Specific Exceptions in a Hierarchical Manner

When handling specific exceptions, it's important to consider the exception hierarchy. Python has a built-in hierarchy of exceptions,
 where some exceptions are subclasses of others. You can handle exceptions in a hierarchical manner by starting with the most specific
  exceptions and moving towards more general ones.

For example, if you want to handle a specific exception like FileNotFoundError and its parent exception IOError, you can write 
the code as follows:

```python
try:
    # Code that might raise an exception
    # ...
except FileNotFoundError:
    # Exception handling code for FileNotFoundError
    # ...
except IOError:
    # Exception handling code for IOError
    # ...
```

In the above example, if a FileNotFoundError occurs, the first except FileNotFoundError block will be executed. If an IOError
occurs that is not a FileNotFoundError, the second except IOError block will be executed.

### 3.5 Catching All Other Exceptions

To handle all other exceptions that are not explicitly caught by specific except blocks, you can use a generic except block 
without specifying the exception type. However, it is generally recommended to catch specific exceptions whenever possible 
to provide more meaningful error handling. Here's an example of a generic except block:

```python
try:
    # Code that might raise an exception
    # ...
except:
    # Generic exception handling code
    # ...
```

In the above example, if any exception occurs that is not caught by previous except blocks, the generic except block will be executed.

### 3.5 Summary

Catching specific exceptions allows you to handle different types of exceptions differently in your code. By specifying 
the exception type in the except block, you can provide customized error handling for specific scenarios. You can catch a single
specific exception, handle multiple specific exceptions, or handle multiple exceptions with a single except block. 
It's important to consider the exception hierarchy and handle exceptions in a hierarchical manner to ensure that exceptions 
are handled appropriately.
