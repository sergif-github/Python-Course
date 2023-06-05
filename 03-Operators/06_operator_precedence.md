# Module 3: Operators

## Part 6: Operator Precedence

Operator precedence determines the order in which operators are evaluated in an expression. When multiple operators are used in the same expression, the operator with higher precedence is evaluated first.

### 6.1 Operator precedence

Python follows a specific set of rules to determine operator precedence. Here are some key points to understand:

- Operators with higher precedence are evaluated before operators with lower precedence.
- Parentheses can be used to override the default precedence and specify the order of evaluation.
- Operators of the same precedence are evaluated from left to right.

Here is a general overview of the operator precedence in Python:

1. Parentheses: `()`
2. Exponentiation: `**`
3. Positive/Negative sign: `+x`, `-x`
4. Multiplication, Division, Floor Division, Modulo: `*`, `/`, `//`, `%`
5. Addition and Subtraction: `+`, `-`
6. Bitwise Shifts: `<<`, `>>`
7. Bitwise AND: `&`
8. Bitwise OR: `|`
9. Bitwise XOR: `^`
10. Comparison Operators: `<`, `<=`, `>`, `>=`, `==`, `!=`
11. Logical NOT: `not`
12. Logical AND: `and`
13. Logical OR: `or`

It's important to note that when in doubt about the order of evaluation, using parentheses is always a good practice to ensure the desired outcome.

Example:

```python
result = 10 + 2 * 3  # Multiplication has higher precedence than addition
print("Result:", result)  # Output: Result: 16

result = (10 + 2) * 3  # Using parentheses to change the order of evaluation
print("Result:", result)  # Output: Result: 36
```

In the first example, without parentheses, the multiplication is evaluated first, resulting in 10 + 6 = 16. In the second example, the parentheses force the addition to be evaluated first, resulting in (10 + 2) * 3 = 36.

Understanding operator precedence is crucial in writing expressions that produce the desired results.

### 6.2 Summary

In this part, you learned about operator precedence in Python. Operator precedence determines the order in which operators are evaluated in an expression. Parentheses can be used to override the default precedence and specify the order of evaluation. Remember to use parentheses when in doubt to ensure the desired outcome.