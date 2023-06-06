# Module 0: Introduction to Python

## Part 5:  User Input

### 5.1. User input with input()

In Python, you can interact with the user by prompting them to enter values using the input() function. The input() function
allows you to capture user input and store it in a variable for further processing.

To get input from the user, you can use the following syntax:

```python
variable_name = input(prompt)
```

Here, variable_name is the name of the variable where you want to store the user's input, and prompt is an optional string that you can display to the user as a prompt.

Let's look at an example:

```python
name = input("Enter your name: ")
print("Hello, " + name + "! Nice to meet you.")
```

In this example, the input() function is used to capture the user's name, which is stored in the name variable. The prompt "Enter your name: " is displayed to the user. The print() function then displays a personalized greeting message using the entered name.

It's important to note that the input() function always returns a string. If you want to perform numerical operations on the user's input, you need to convert the input to the desired data type using functions like int() or float().

Here's an example of converting user input to an integer:

```python
age = int(input("Enter your age: "))
years_remaining = 100 - age
print("You have approximately " + str(years_remaining) + " years until you turn 100.")
```

In this example, the input() function captures the user's age as a string, which is then converted to an integer using the int() function. The result is stored in the age variable, and further calculations are performed on the integer value.

### 5.2 Summary

Remember to handle user input with caution. You may want to add validation and error handling to ensure the user enters the expected type of input and handle any potential exceptions that may occur.

User input is a powerful tool that allows your Python programs to interact with users, making them more dynamic and interactive.