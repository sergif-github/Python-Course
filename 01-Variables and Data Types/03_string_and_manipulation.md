# Module 1: Variables and Data Types

## Part 3: Strings and String Manipulation

In Python, a string is a sequence of characters enclosed in single quotes (`'`) or double quotes (`"`). It is used to represent 
text or a collection of characters. Strings are immutable, meaning that once they are created, their values cannot be changed.

### 3.1 Creating Strings

You can create strings by enclosing text within single quotes or double quotes. For example:

```python
name = 'Alice'
message = "Hello, World!"


Both single quotes and double quotes can be used interchangeably to define strings. However, make sure to use the same type 
of quotes at the beginning and end of the string.

### 3.2 String Manipulation

Python provides various operations and methods for manipulating strings. Here are some commonly used string manipulation techniques:

#### 3.2.1 Concatenation
You can concatenate two or more strings using the + operator. This combines the strings into a single string:

```python
first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe
```

#### 3.2.2 String Length and count
You can determine the length of a string using the len() function. It returns the number of characters in the string:
```python
message = "Hello, World!"
length = len(message)
print("Length:", length)  # Output: Length: 13
```

You can determine the occurrences of a word in a string using the count() function. It returns the number of occurrences in the string:
```python
message = "Hello, World!"
word = "Hello"
occurrences = message.count(word)
print("Occurrences:", occurrences)  # Output: Length: 13
```

#### 3.2.3 Accessing Characters

You can access individual characters within a string by using indexing. Indexing starts from 0 for the first character:

```python
message = "Hello, World!"
first_char = message[0]
print("First Character:", first_char)  # Output: First Character: H
```

You can also use negative indexing to access characters from the end of the string. -1 refers to the last character:

```python
last_char = message[-1]
print("Last Character:", last_char)  # Output: Last Character: !
```

#### 3.2.4 Slicing
You can extract a substring from a string using slicing. Slicing allows you to specify a range of indices to extract a portion of the string:

```python
message = "Hello, World!"
substring = message[7:12]
print("Substring:", substring)  # Output: Substring: World
```

### 3.3 String Methods

Python provides a rich set of built-in string methods that allow you to manipulate strings. Here are some commonly used string methods:

```python
message = "Hello, World!"

# Convert to uppercase
uppercase = message.upper()
print("Uppercase:", uppercase)  # Output: Uppercase: HELLO, WORLD!

# Convert to lowercase
lowercase = message.lower()
print("Lowercase:", lowercase)  # Output: Lowercase: hello, world!

# Replace substring
replaced = message.replace("Hello", "Hi")
print("Replaced:", replaced)  # Output: Replaced: Hi, World!

# Split into a list
words = message.split(", ")
print("Words:", words)  # Output: Words: ['Hello', 'World!']
```

### 3.4 Summary

In this part, you explored strings and string manipulation in Python. Strings are used to represent text and can be manipulated using
various operations and methods. Understanding string manipulation techniques is crucial for working with textual data in Python.