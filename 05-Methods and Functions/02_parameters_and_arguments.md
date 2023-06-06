# Module 5: Methods and Functions

## Part 2: Function Parameters and Arguments

In Python, function parameters are placeholders for values that are passed into the function when it is called.
They allow you to provide input to the function and make the function more flexible and reusable. Let's explore function
parameters and arguments in more detail:

### 2.1 Function Parameters

Function parameters are defined inside the parentheses of a function's definition. They specify the expected inputs that 
the function will work with. Parameters act as variables within the function's body, allowing you to perform operations 
and calculations using these values. Here's an example:

```python
def greet(name):
    print("Hello,", name, "welcome!")
```

In this example, the greet() function has a single parameter name. The parameter name acts as a variable that can be used
within the function's body.

### 2.2 Function Arguments

When you call a function, you provide values known as arguments that match the function's parameters. Arguments are the 
actual values that are passed into the function. Here's how you can call the greet() function and provide an argument for
the name parameter:

```python
greet("John")
In this example, the string "John" is passed as an argument to the greet() function. The argument value is assigned to 
the name parameter within the function.
```

### 2.3 Default Parameters

You can also specify default parameter values in a function's definition. Default parameters are used when no argument 
is provided for that parameter during function call. Here's an example:

```python
def greet(name="guest"):
    print("Hello,", name, "welcome!")
```

In this example, the greet() function has a default parameter name set to "guest". If no argument is provided when calling
the function, it will use the default value. However, if an argument is provided, it will override the default value.

### 2.4 Multiple Parameters

Functions can have multiple parameters, allowing you to work with multiple inputs. The parameters are separated by commas
within the parentheses. Here's an example:

```python
def add_numbers(a, b):
    return a + b
```

In this example, the add_numbers() function has two parameters, a and b. The function can accept two arguments that will
be used to perform the addition operation.

### 2.5 Summary

In this part, you learned about function parameters and arguments in Python. Parameters are defined in a function's 
definition and act as placeholders for the values that will be passed into the function as arguments. You can specify default
parameter values and have multiple parameters in a function. Understanding parameters and arguments allows you to create
functions that can work with different inputs and make your code more flexible.