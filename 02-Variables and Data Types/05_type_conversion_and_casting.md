# Module 2: Variables and Data Types

## Part 5: Type Conversion and Casting

In Python, you can convert one data type to another using type conversion or casting. Type conversion allows you to change the data type of a value, while casting explicitly specifies the desired data type.

### 5.1 Implicit Type Conversion

Python automatically performs implicit type conversion when it encounters expressions involving different data types. For example, when you perform arithmetic operations between different numeric types, Python will automatically convert the operands to a common type:

```python
x = 10
y = 3.5

result = x + y  # Implicit conversion of int to float
print("Result:", result)  # Output: Result: 13.5
```

In this example, the integer x is implicitly converted to a float to perform the addition operation with y.

### 5.2 Explicit Type Casting

You can explicitly cast values from one data type to another using casting functions. Python provides several built-in functions for type casting, including:

int() - converts a value to an integer
float() - converts a value to a float
str() - converts a value to a string
bool() - converts a value to a Boolean
For example:

```python
x = 10.5
y = int(x)  # Explicitly cast float to int

print("Original value:", x)  # Output: Original value: 10.5
print("Casted value:", y)  # Output: Casted value: 10
```

In this example, the float value x is explicitly casted to an integer using the int() function.

### 5.3 Summary
In this part, you explored type conversion and casting in Python. Implicit type conversion allows Python to automatically convert values of different data types, while explicit type casting enables you to explicitly convert values using casting functions. Understanding type conversion and casting is important for manipulating and transforming data in your programs.