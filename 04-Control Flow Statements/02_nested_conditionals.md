## Module 4: Conditional Statements

### Part 2: Nested Conditionals

Nested conditionals are conditional statements that are placed inside other conditional statements. They allow you to check multiple conditions and execute different blocks of code based on those conditions. Here's an example of nested conditionals:

```python
num = 10

if num > 0:
    print("Number is positive.")
    if num % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")
else:
    print("Number is non-positive.")
```

In this example, the outer if statement checks if num is greater than 0. If the condition is true, it prints "Number is positive." Then, there is a nested if-else statement inside the first code block. It checks if num is divisible by 2 to determine if it's even or odd.

Nested conditionals can have multiple levels depending on the complexity of the conditions you need to check. It's important to properly indent the code blocks to indicate the hierarchy of the conditionals.

Nested conditionals allow for more precise control over the flow of the program based on different conditions. However, it's essential to keep the code readable and maintainable by using proper indentation and avoiding excessive nesting.

### 2.1 Summary

In this part, you learned about nested conditionals in Python. Nested conditionals allow you to place conditional statements inside other conditional statements, enabling you to check multiple conditions and execute different blocks of code based on those conditions. Make sure to properly indent the code blocks to indicate the hierarchy of the conditionals and maintain readability.