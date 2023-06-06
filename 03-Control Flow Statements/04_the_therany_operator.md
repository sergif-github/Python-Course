# Module 3: Conditional Statements

## Part 4: Ternary Operator

The ternary operator, also known as the conditional expression, provides a concise way to write simple conditional statements in Python. It allows you to evaluate a condition and return a value based on the result of the condition. The syntax of the ternary operator is as follows:

```python
value_if_true if condition else value_if_false
```

Here's an example to illustrate the usage of the ternary operator:

```python
num = 10

result = "Positive" if num > 0 else "Non-positive"

print(result)
```

In this example, the ternary operator is used to assign a value to the variable result based on the condition num > 0. If the condition is True, the value "Positive" is assigned to result; otherwise, the value "Non-positive" is assigned. The value of result is then printed, which will be either "Positive" or "Non-positive" depending on the value of num.

The ternary operator can be used to simplify the code and make it more readable in cases where you need to assign a value based on a simple condition. However, it's important to use it judiciously and avoid nesting multiple ternary operators, as it can make the code less understandable.

### Summary

In this part, you learned about the ternary operator in Python. The ternary operator provides a concise way to write simple conditional statements and assign a value based on a condition. It can make the code more readable and compact in certain situations. However, it's important to use it sparingly and avoid excessive nesting to maintain code clarity.