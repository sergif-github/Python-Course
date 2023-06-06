# Module 5: Methods and Functions

## Part 3: Variable Scope and Global Keyword

In Python, variable scope refers to the region or part of the code where a variable is recognized and can be accessed. 
Understanding variable scope is important to determine the lifetime and visibility of variables within functions. 
Let's explore variable scope and the use of the global keyword in Python:

### 3.1 Local Variables

Variables that are defined inside a function have a local scope. Local variables are only accessible within the function
where they are defined. Once the function execution is complete, the local variables cease to exist. Here's an example:

```python
def my_function():
    x = 10
    print(x)

my_function()
```

In this example, the variable x is a local variable defined within the my_function() function. It can only be accessed 
within the function's scope. When the function is called, the value of x is printed.

### 3.2 Global Variables

Variables that are defined outside of any function have a global scope. Global variables are accessible throughout the 
entire program, including within functions. You can use global variables to store values that need to be accessed from 
multiple parts of your code. Here's an example:

```python
x = 10

def my_function():
    print(x)

my_function()
```

In this example, the variable x is a global variable defined outside the my_function() function. It can be accessed within
the function because it has a global scope. When the function is called, the value of x is printed.

### 3.3 The Global Keyword

If you want to modify a global variable inside a function, you need to use the global keyword to indicate that you want 
to work with the global variable instead of creating a new local variable. Here's an example:

```python
x = 10

def modify_global():
    global x
    x = 20

modify_global()
print(x)
```

In this example, the modify_global() function uses the global keyword to indicate that the x variable being modified 
is the global variable, not a local one. The value of x is changed to 20, and when it is printed outside the function,
 the modified value is displayed.

### 3.4 Summary

In this part, you learned about variable scope and the global keyword in Python. Local variables are defined within functions
 and have a scope limited to the function. Global variables are defined outside functions and can be accessed throughout
  the program. To modify a global variable within a function, you need to use the global keyword. Understanding variable
   scope and the use of global variables is essential for writing modular and maintainable code.