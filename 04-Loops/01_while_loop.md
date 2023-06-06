# Module 4: Loops

## Part 1: While Loop

The `while` loop in Python allows you to repeatedly execute a block of code as long as a certain condition is true. It's used when you want to iterate over a block of code an unknown number of times until a specific condition is met. Here's the basic syntax of a `while` loop:

```python
while condition:
    # Code to be executed while the condition is true
```

The condition is an expression that is evaluated at the beginning of each iteration. If the condition is true, the code block inside the while loop is executed. After each iteration, the condition is checked again, and if it's still true, the loop continues. If the condition becomes false, the loop is exited, and the program continues to the next statement after the while loop.

Here's an example that demonstrates the usage of a while loop:

```python
count = 0

while count < 5:
    print("Count:", count)
    count += 1

print("Loop finished")
```

In this example, the while loop continues as long as the value of count is less than 5. Inside the loop, the current value of count is printed, and then count is incremented by 1 using the += operator. Once the value of count reaches 5, the condition becomes false, and the loop is exited. The message "Loop finished" is then printed.

It's important to ensure that the condition inside the while loop eventually becomes false; otherwise, you may end up with an infinite loop, which can cause your program to hang or consume excessive resources. To avoid this, make sure that the condition is properly updated within the loop so that the termination condition is eventually met.

### Summary

In this part, you learned about the while loop in Python. The while loop allows you to repeatedly execute a block of code as long as a certain condition is true. It's used when you want to iterate over a block of code an unknown number of times until a specific condition is met. Ensure that the condition eventually becomes false to avoid infinite loops.