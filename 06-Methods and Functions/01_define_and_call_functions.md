# Module 6: Methods and Functions

## Part 1: Defining and Calling Functions## Module 5: Loops

In Python, functions are reusable blocks of code that perform a specific task. They allow you to break down your program
into smaller, more manageable pieces, making your code more organized and easier to understand. Let's explore how to define
and call functions in Python:

### 1.1 Defining a Function

To define a function in Python, you use the `def` keyword followed by the function name, parentheses, and a colon. 
Any code indented under the function definition is part of the function's body. Here's an example of a simple function
that greets the user:

```python
def greet():
    print("Hello, welcome!")
```

In this example, the greet() function is defined without any parameters. The function body contains a single statement
that prints a greeting message.

### 1.2 Calling a Function

Once a function is defined, you can call or invoke it to execute its code. To call a function, you simply write its name 
followed by parentheses. Here's how you can call the greet() function defined earlier:

```python
greet()
```

When you call the greet() function, the code inside the function's body is executed, and the output "Hello, welcome!" 
is displayed.

### 1.3 Function Parameters

Functions can also accept parameters, which are placeholders for values that are passed into the function when it is called.
Parameters allow functions to work with different inputs and make the code more flexible and reusable. Here's an example
of a function that takes a parameter:

```python
def greet(name):
    print("Hello,", name, "welcome!")
```

In this example, the greet() function has a single parameter named name. When the function is called, you provide a value
for the name parameter, which is then used inside the function to print the personalized greeting message.

### 1.4 Return Statement
Functions can also return values using the return statement. The return statement allows a function to compute a result
and pass it back to the code that called the function. Here's an example:

```python
def add_numbers(a, b):
    return a + b
```

In this example, the add_numbers() function takes two parameters a and b, and it returns their sum using the return statement.
You can store the returned value in a variable or use it in any other part of your program.

### 1.5 Summary

In this part, you learned how to define and call functions in Python. Functions are reusable blocks of code that allow you
to break down your program into smaller, more manageable pieces. You can define functions without parameters or with one
or more parameters, and you can use the return statement to pass back a value from a function. Functions help make your
code more organized, modular, and easier to understand.