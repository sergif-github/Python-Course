## Module 8: Exception Handling

### Part 2: Handling Exceptions Using try-except Blocks

In Python, you can handle exceptions using the `try-except` block. This construct allows you to catch and handle specific exceptions
that may occur during the execution of your code. By handling exceptions, you can prevent your program from crashing and provide 
alternative actions or error messages to users.

#### 2.1 Syntax of the try-except Block

The `try-except` block consists of the `try` block, where you place the code that might raise an exception, and one or more `except` 
blocks that define how to handle specific exceptions. Here's the basic syntax:

```python
try:
    # Code that might raise an exception
    # ...
except ExceptionType:
    # Exception handling code
    # ...
```

In the except block, you specify the type of exception you want to handle by mentioning the ExceptionType. If an exception of that 
type occurs in the try block, the corresponding except block is executed. You can have multiple except blocks to handle different types 
of exceptions.

#### 2.2 Handling Multiple Exceptions

You can handle multiple exceptions by using multiple except blocks. Each except block can handle a specific type of exception. 
The first except block that matches the raised exception type will be executed, and subsequent except blocks will be skipped.

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
```

#### 2.3 Handling Multiple Exceptions with a Single Except Block

If you want to handle multiple exceptions with the same handling code, you can specify multiple exception types within a single except
 block. This is useful when you want to provide the same error handling logic for different types of exceptions.

```python
try:
    # Code that might raise an exception
    # ...
except (ExceptionType1, ExceptionType2):
    # Exception handling code for ExceptionType1 and ExceptionType2
    # ...
```

#### 2.4 Handling All Exceptions

You can also use a generic except block to handle any type of exception. This can be useful when you want to catch all exceptions
 and provide a common error handling routine.

```python
try:
    # Code that might raise an exception
    # ...
except:
    # Exception handling code for any type of exception
    # ...
```

#### 2.5 The else Block

In addition to the try and except blocks, you can include an optional else block after all the except blocks. The code inside the
else block is executed if no exceptions occur in the try block. It is often used to perform cleanup or additional actions that 
should only happen when no exceptions are raised.

```python
try:
    # Code that might raise an exception
    # ...
except ExceptionType:
    # Exception handling code
    # ...
else:
    # Code that executes if no exceptions occur
    # ...
```

#### 2.6 The finally Block

Another optional block that can be used with the try-except block is the finally block. The code inside the finally block is 
always executed, regardless of whether an exception was raised or not. It is commonly used to release resources, close files, 
or perform other cleanup actions.

```python
try:
    # Code that might raise an exception
    # ...
except ExceptionType:
    # Exception handling code
    # ...
finally:
    # Code that always executes
    # ...
```

#### 2.7 Summary

Handling exceptions using the try-except block is a powerful technique in Python to deal with potential errors and ensure the
smooth execution of your code. By catching and handling exceptions, you can provide better error messages, recover from unexpected situations, and prevent your program from crashing. With the else and finally blocks, you have additional flexibility to perform cleanup actions and handle various scenarios in your code.
