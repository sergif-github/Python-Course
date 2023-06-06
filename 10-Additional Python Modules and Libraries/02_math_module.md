# Module 10: Additional Python Modules and Libraries

## Part 2: Mathematical Operations (math module)

Python provides the `math` module for performing various mathematical operations and functions. This module extends Python's
built-in mathematical capabilities and allows you to work with more advanced mathematical operations.

### 1.2 Math module

To use the `math` module, you need to import it. Here's an example:

```python
import math

# Perform basic mathematical operations
num1 = 10
num2 = 5

sum_result = math.add(num1, num2)
difference_result = math.subtract(num1, num2)
product_result = math.multiply(num1, num2)
quotient_result = math.divide(num1, num2)

print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)

# Perform more advanced mathematical operations
square_root = math.sqrt(25)
power = math.pow(2, 3)
absolute_value = math.abs(-10)
ceil_value = math.ceil(4.7)
floor_value = math.floor(4.7)

print("Square root:", square_root)
print("Power:", power)
print("Absolute value:", absolute_value)
print("Ceiling value:", ceil_value)
print("Floor value:", floor_value)
```

In this example, we import the math module and use it to perform various mathematical operations. Here's what each step does:
- We perform basic mathematical operations like addition, subtraction, multiplication, and division using the appropriate functions
provided by the math module.
- We perform more advanced mathematical operations like square root, power, absolute value, ceiling value (round up to the nearest integer),
and floor value (round down to the nearest integer).

### Summary 

The math module provides many more mathematical functions, such as trigonometric functions, logarithmic functions, and exponential functions.
You can refer to the official Python documentation for a comprehensive list of functions available in the math module.