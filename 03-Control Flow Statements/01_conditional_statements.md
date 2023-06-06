# Module 3: Conditional Statements

## Part 1: Conditional Statements (if, else, elif)

Conditional statements are used in Python to execute different blocks of code based on certain conditions. The most common conditional statements in Python are the `if`, `else`, and `elif` statements.

### 1.1 The `if` Statement

The `if` statement is used to check a condition and execute a block of code if the condition is true. Here's the basic syntax of the `if` statement:

```python
if condition:
    # code to execute if the condition is true
```

Example:

```python
age = 20

if age >= 18:
    print("You are an adult.")
```

In this example, the if statement checks if the age variable is greater than or equal to 18. If the condition is true, the code block inside the if statement is executed, and the message "You are an adult." is printed.

### 1.2 The else Statement

The else statement is used to specify a block of code to be executed if the condition in the if statement is false. Here's the basic syntax of the else statement:

```python
if condition:
    # code to execute if the condition is true
else:
    # code to execute if the condition is false
```

Example:

```python
age = 15

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

In this example, if the condition age >= 18 is false, the code block inside the else statement is executed, and the message "You are a minor." is printed.

### 1.3 The elif Statement

The elif statement is short for "else if" and is used to specify additional conditions to check if the preceding if statement is false. Here's the basic syntax of the elif statement:

```python
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true
else:
    # code to execute if all conditions are false
```

Example:

```python
age = 25

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```

In this example, the elif statement checks if the age is between 18 and 65. If the first condition is false and the second condition is true, the code block inside the elif statement is executed, and the message "You are an adult." is printed.

### 1.4 Summary

In this part, you learned about conditional statements in Python, including the if, else, and elif statements. Conditional statements allow you to execute different blocks of code based on certain conditions. Use the if statement to check a condition, the else statement to specify code for when the condition is false, and the elif statement to check additional conditions if the preceding if statement is false.