# Module 3: Operators

## Part 5: Bitwise Operators

Bitwise operators are used to perform bitwise operations on the binary representation of integers. 

### 5.1 Bitwise Operators

These operators work on individual bits of the operands. Python provides several bitwise operators for performing operations at the bit level.

#### Bitwise AND Operator (`&`)

The bitwise AND operator (`&`) performs a bitwise AND operation between the corresponding bits of two operands. It returns a value where each bit is set if both corresponding bits are set in the operands. For example:

```python
x = 5  # Binary: 0101
y = 3  # Binary: 0011

result = x & y  # Binary: 0001 -> Decimal: 1
print("Result:", result)  # Output: Result: 1
```

#### Bitwise OR Operator (|)

The bitwise OR operator (|) performs a bitwise OR operation between the corresponding bits of two operands. It returns a value where each bit is set if at least one of the corresponding bits is set in the operands. For example:

```python
x = 5  # Binary: 0101
y = 3  # Binary: 0011

result = x | y  # Binary: 0111 -> Decimal: 7
print("Result:", result)  # Output: Result: 7
```

#### Bitwise XOR Operator (^)

The bitwise XOR operator (^) performs a bitwise exclusive OR operation between the corresponding bits of two operands. It returns a value where each bit is set if only one of the corresponding bits is set in the operands. For example:

```python
x = 5  # Binary: 0101
y = 3  # Binary: 0011

result = x ^ y  # Binary: 0110 -> Decimal: 6
print("Result:", result)  # Output: Result: 6
```

#### Bitwise NOT Operator (~)

The bitwise NOT operator (~) performs a bitwise complement operation on the operand, which flips the bits. It returns the one's complement of the operand. For example:

```python
x = 5  # Binary: 0101

result = ~x  # Binary: 1010 -> Decimal: -6
print("Result:", result)  # Output: Result: -6
```

#### Bitwise Left Shift Operator (<<)

The bitwise left shift operator (<<) shifts the bits of the left operand to the left by the number of positions specified by the right operand. For example:

```python
x = 5  # Binary: 0101

result = x << 2  # Binary: 010100 -> Decimal: 20
print("Result:", result)  # Output: Result: 20
```

#### Bitwise Right Shift Operator (>>)

The bitwise right shift operator (>>) shifts the bits of the left operand to the right by the number of positions specified by the right operand. For example:

```python
x = 5  # Binary: 0101

result = x >> 2  # Binary: 0001 -> Decimal: 1
print("Result:", result)  # Output: Result: 1
```

### 5.2 Summary

In this part, you explored the bitwise operators in Python, including the bitwise AND (&), bitwise OR (|), bitwise XOR (^), bitwise NOT (~), bitwise left shift (<<), and bitwise right shift (>>) operators. These operators are useful for performing operations at the bit level on binary representations of integers.