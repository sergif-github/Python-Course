# Module 4: Loops

## Part 2: For Loop

The `for` loop in Python is used to iterate over a sequence or iterable object, such as a list, tuple, string, or range. It allows you to execute a block of code for each item in the sequence. Here's the basic syntax of a `for` loop:

```python
for item in sequence:
    # Code to be executed for each item in the sequence
```

In this syntax, item is a variable that represents each item in the sequence, and sequence is the iterable object that provides the sequence of items. The code block inside the for loop is executed for each item in the sequence, with the item variable taking on the value of each item in turn.

Here's an example that demonstrates the usage of a for loop:

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

print("Loop finished")
```

In this example, the for loop iterates over each item in the fruits list. For each iteration, the value of the current fruit is assigned to the fruit variable, and then the print statement prints the name of the fruit. After iterating over all the items in the list, the message "Loop finished" is printed.

The range() function is commonly used in conjunction with for loops to generate a sequence of numbers. Here's an example:

```python
for i in range(5):
    print(i)

print("Loop finished")
```

In this example, the range(5) function generates a sequence of numbers from 0 to 4. The for loop iterates over each number in the sequence, and the print statement prints the value of i. After printing all the numbers, the message "Loop finished" is printed.

### Summary

In this part, you learned about the for loop in Python. The for loop allows you to iterate over a sequence or iterable object and execute a block of code for each item in the sequence. Use the item variable to access the value of each item in the loop. The range() function is often used to generate a sequence of numbers for iteration.