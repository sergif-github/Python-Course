# Module 1: Variables and Data Types

## Part 2: Numeric Data Types (int, float)

In Python, there are two primary numeric data types: `int` and `float`. These data types are used to represent whole numbers and floating-point numbers, respectively.

### 2.1 Integer (int) Data Type

The `int` data type represents whole numbers without any fractional parts. It can be used to store positive and negative numbers, as well as zero. For example:

```python
age = 25
quantity = -10
population = 1000000
```

Python provides various arithmetic operations that can be performed on int values, such as addition, subtraction, multiplication, and division.
These operations return results of type int when both operands are integers. For example:

```python
x = 10
y = 3

sum = x + y
difference = x - y
product = x * y
quotient = x / y

print("Sum:", sum)  # Output: Sum: 13
print("Difference:", difference)  # Output: Difference: 7
print("Product:", product)  # Output: Product: 30
print("Quotient:", quotient)  # Output: Quotient: 3.3333333333333335
```

### 2.2 Floating-Point (float) Data Type

The float data type represents numbers with fractional parts. It can store both small and large floating-point numbers. For example:

```python
pi = 3.14159
temperature = -10.5
price = 19.99
```

Floating-point numbers can also be used in arithmetic operations:

```python
x = 5.0
y = 2.0

sum = x + y
difference = x - y
product = x * y
quotient = x / y

print("Sum:", sum)  # Output: Sum: 7.0
print("Difference:", difference)  # Output: Difference: 3.0
print("Product:", product)  # Output: Product: 10.0
print("Quotient:", quotient)  # Output: Quotient: 2.5
```

It's important to note that when an int and a float are used in an arithmetic operation, the result will be a float:

```python
x = 10
y = 3.0

result = x / y

print("Result:", result)  # Output: Result: 3.3333333333333335
```

### 2.3 Summary
In this part, you explored the int and float data types in Python. These data types are used to represent whole numbers and floating-point numbers,
respectively. They support various arithmetic operations and can be used in mathematical calculations.
