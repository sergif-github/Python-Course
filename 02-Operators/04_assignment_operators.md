# Module 2: Operators

## Part 4: Assignment Operators

Assignment operators are used to assign values to variables. 

### 4.1 Assignment Operators

They combine the assignment (`=`) operator with other operators to perform an operation and assign the result to a variable in a single step.

#### Simple Assignment Operator (`=`)

The simple assignment operator (`=`) is used to assign a value to a variable. For example:

```python
x = 5
y = 3
```

### 4.2 Compound Assignment Operators

Python provides compound assignment operators that combine an arithmetic or bitwise operation with the assignment operation. They allow you to perform an operation and update the value of the variable in one step.

#### Addition Assignment Operator (+=)

The addition assignment operator (+=) adds the right operand to the left operand and assigns the result to the left operand. For example:

```python
x = 5
x += 3  # x = x + 3 -> 5 + 3 -> 8
print("Result:", x)  # Output: Result: 8
```

#### Subtraction Assignment Operator (-=)

The subtraction assignment operator (-=) subtracts the right operand from the left operand and assigns the result to the left operand. For example:

```python
x = 5
x -= 3  # x = x - 3 -> 5 - 3 -> 2
print("Result:", x)  # Output: Result: 2
```

#### Multiplication Assignment Operator (*=)

The multiplication assignment operator (*=) multiplies the right operand with the left operand and assigns the result to the left operand. For example:

```python
x = 5
x *= 3  # x = x * 3 -> 5 * 3 -> 15
print("Result:", x)  # Output: Result: 15
```

#### Division Assignment Operator (/=)

The division assignment operator (/=) divides the left operand by the right operand and assigns the result to the left operand. For example:

```python
x = 10
x /= 2  # x = x / 2 -> 10 / 2 -> 5.0
print("Result:", x)  # Output: Result: 5.0
```

#### Modulo Assignment Operator (%=)

The modulo assignment operator (%=) calculates the remainder when the left operand is divided by the right operand and assigns the result to the left operand. For example:

```python
x = 10
x %= 3  # x = x % 3 -> 10 % 3 -> 1
print("Result:", x)  # Output: Result: 1
```

#### Exponentiation Assignment Operator (**=)

The exponentiation assignment operator (**=) raises the left operand to the power of the right operand and assigns the result to the left operand. For example:

```python
x = 2
x **= 3  # x = x ** 3 -> 2 ** 3 -> 8
print("Result:", x)  # Output: Result: 8
```

#### Floor Division Assignment Operator (//=)

The floor division assignment operator (//=) performs integer division between the left operand and the right operand, discarding the fractional part, and assigns the result to the left operand. For example:

```python
x = 10
x //= 3  # x = x // 3 -> 10 // 3 -> 3
print("Result:", x)  # Output: Result: 3
```

### 4.3 Summary

In this part, you learned about assignment operators in Python, including the simple assignment operator (=) and compound assignment operators (+=, -=, *=, /=, %=, **=, //=). These operators are useful for performing an operation and assigning the result to a variable in a single step.