## Module 5: Loops

### Part 3: Loop Control Statements (break, continue)

In Python, you can use loop control statements to alter the normal flow of execution within loops. Two commonly used loop control statements are `break` and `continue`.

### 3.1. Break Statement

The `break` statement is used to exit the loop prematurely when a certain condition is met. When the `break` statement is encountered inside a loop, the loop is immediately terminated, and the program execution continues with the next statement after the loop. Here's an example:

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        break
    print(num)

print("Loop finished")
```

In this example, the break statement is used to exit the loop when the value of num is equal to 3. As soon as the condition is met, the loop is terminated, and the program execution continues with the statement after the loop. In this case, only the numbers 1 and 2 will be printed before the loop is exited.

### 3.2. Continue Statement
The continue statement is used to skip the current iteration of a loop and continue with the next iteration. When the continue statement is encountered inside a loop, the remaining code in the loop for the current iteration is skipped, and the loop proceeds with the next iteration. Here's an example:

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        continue
    print(num)

print("Loop finished")
```

In this example, the continue statement is used to skip the iteration when the value of num is equal to 3. When the condition is met, the print statement is skipped, and the loop continues with the next iteration. As a result, all the numbers except 3 will be printed.

### 3.3 Summary

In this part, you learned about the loop control statements break and continue. The break statement allows you to exit the loop prematurely when a certain condition is met, while the continue statement allows you to skip the current iteration and proceed with the next iteration. Use these statements judiciously to control the flow of your loops based on specific conditions.