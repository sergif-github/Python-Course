# Module 6: Methods and Functions

## Part 4: Returning Values from Functions

In Python, functions can return values to the caller using the `return` statement. Returning values from functions allows
you to perform calculations or operations and pass the result back to the calling code. Let's explore how to return values
from functions in Python:

### 4.1 Return Statement

The `return` statement is used to return a value from a function. When the `return` statement is encountered, the function
execution stops, and the control is returned to the caller along with the specified value. Here's an example:

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)
print(result)
```

In this example, the add_numbers() function takes two arguments a and b, performs the addition operation, and returns the
 result using the return statement. The returned value is stored in the variable result, and it is then printed.

### 4.2 Multiple Return Values

Functions in Python can also return multiple values using tuples. A tuple is an ordered collection of elements enclosed 
in parentheses. Here's an example:

```python
def calculate_stats(numbers):
    count = len(numbers)
    total = sum(numbers)
    average = total / count
    return count, total, average

result = calculate_stats([1, 2, 3, 4, 5])
print(result)
```

In this example, the calculate_stats() function takes a list of numbers as an argument, calculates the count, total, and
 average of the numbers, and returns them as a tuple. The returned tuple is stored in the variable result and printed.

### 4.3 None and Empty Return

If a function does not specify a return statement or uses the return statement without any value, it returns None.
None is a special value in Python that represents the absence of a value. Here's an example:

```python
def say_hello():
    print("Hello!")

result = say_hello()
print(result)
```

In this example, the say_hello() function does not have a return statement. When the function is called, it prints "Hello!"
 but does not return any value. The variable result is assigned None, which is then printed.

### 4.4 Summary

In this part, you learned how to return values from functions in Python. The return statement is used to specify the value
to be returned from a function. Functions can return a single value or multiple values using tuples. If a function does 
not specify a return statement or returns without a value, it returns None. Returning values from functions enables 
you nto pass data back to the calling code and use the results of calculations or operations.