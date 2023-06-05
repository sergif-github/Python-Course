# Module 3: Operators

## Part 3: Logical Operators

Logical operators are used to combine multiple conditions and perform logical operations.

### 3.1 Logical operators

Python provides three logical operators: `and`, `or`, and `not`. These operators are useful for making decisions based on multiple conditions.

#### Logical AND Operator (`and`)

The logical AND operator (`and`) returns `True` if both of its operands are `True`, and `False` otherwise. For example:

```python
x = 5
y = 3
z = 7

result = (x > y) and (y < z)  # (5 > 3) and (3 < 7) -> True and True -> True
print("Result:", result)  # Output: Result: True
```

#### Logical OR Operator (or)

The logical OR operator (or) returns True if at least one of its operands is True, and False if both operands are False. For example:

```python
x = 5
y = 3
z = 7

result = (x > y) or (y > z)  # (5 > 3) or (3 > 7) -> True or False -> True
print("Result:", result)  # Output: Result: True
```

#### Logical NOT Operator (not)

The logical NOT operator (not) negates the value of its operand. If the operand is True, it returns False, and if the operand is False, it returns True. For example:

```python
x = True

result = not x  # not True -> False
print("Result:", result)  # Output: Result: False
```

#### Operator Precedence

When using multiple logical operators together, it's important to understand their precedence. The not operator has the highest precedence, followed by and, and then or. However, it's always a good practice to use parentheses to clarify the intended order of operations.

```python
result = (x > y) and (y < z) or (x == z)
```

In the above example, the comparison (x > y) and (y < z) is evaluated first due to the parentheses, followed by the or operation with (x == z).

### 3.2 Summary

In this part, you explored the logical operators in Python, including the logical AND (and), logical OR (or), and logical NOT (not) operators. These operators are useful for combining conditions and making decisions based on logical expressions.