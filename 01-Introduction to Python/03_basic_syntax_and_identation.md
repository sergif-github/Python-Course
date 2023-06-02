# Module 1: Introduction to Python

## Part 3: Basic Syntax and Indentation

Python follows a simple and readable syntax that uses indentation to define the structure of code blocks. 
Understanding the basic syntax rules and proper indentation is crucial for writing correct and maintainable Python programs.

### 3.1. Statements and Lines

In Python, statements are instructions or commands that perform specific actions. Each statement typically occupies a single line,
but you can extend a statement across multiple lines using line continuation techniques.

A line of code in Python is terminated by a newline character. However, you can use a backslash () at the end of a line
to indicate that the statement continues on the next line.

For example:
```python
print("Hello,")
print("World!")

Output:
Hello,
World!
```

### 3.2. Indentation

In Python, indentation plays a crucial role in defining the structure and scope of code blocks. Unlike other programming languages
that use braces or keywords, Python uses consistent indentation to indicate the beginning and end of blocks.
Indentation is typically done using spaces or tabs, but it's essential to be consistent throughout your code. 
The standard recommendation is to use four spaces for each indentation level.

For example:
```python
if condition:
    # Indented block of code
    statement1
    statement2
else:
    # Another indented block of code
    statement3
    statement4
```

Proper indentation is crucial for code readability and ensures that the program logic is correctly interpreted by the Python interpreter.

### 3.2. Blank Lines

Blank lines, i.e., empty lines, are ignored by the Python interpreter and can be used to improve code readability by separating
code sections or logical blocks. You can use blank lines to enhance the visual structure and organization of your code.

### 3.3. Code Blocks and Control Flow

Control flow statements like if, for, while, and function definitions create code blocks. These code blocks are defined by their
indentation level. All statements within a code block must be indented at the same level.
For example:
```python
if condition:
    # Code block 1
    statement1
    statement2
else:
    # Code block 2
    statement3
    statement4
```

### 3.3 Summary

Indentation defines the hierarchy and nesting of code blocks. It's important to ensure proper indentation to avoid syntax
errors and accurately represent the desired program logic.

Understanding and adhering to the basic syntax rules and indentation principles in Python is fundamental for writing clear,
readable, and error-free code. It promotes consistency and helps others understand and maintain your code.