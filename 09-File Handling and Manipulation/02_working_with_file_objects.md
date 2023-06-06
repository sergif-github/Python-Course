# Module 9: File Handling and Manipulation

## Part 2: Working with File Objects

In addition to reading and writing text files, Python provides several methods and attributes that can be used to work with file objects.
In this section, we will explore some of these features.

### 2.1 File Object Methods

File objects in Python come with various methods that allow you to perform operations on the file. Here are some commonly used methods:

- `read(size)`: Reads and returns `size` bytes from the file. If `size` is not specified, it reads the entire file.
- `readline()`: Reads and returns the next line from the file.
- `readlines()`: Reads all lines from the file and returns them as a list of strings.
- `write(string)`: Writes the specified `string` to the file.
- `writelines(lines)`: Writes a list of strings `lines` to the file.
- `seek(offset)`: Changes the file position to the given `offset` (in bytes).
- `tell()`: Returns the current file position.
- `close()`: Closes the file.

Here's an example that demonstrates the usage of some of these methods:

```python
file = open("example.txt", "r")
content = file.read()  # Read the entire file
line = file.readline()  # Read the next line
lines = file.readlines()  # Read all lines into a list
file.close()  # Close the file
```

### 2.2 File Object Attributes

File objects also provide some useful attributes that provide information about the file. Here are a few commonly used attributes:

name: Returns the name of the file.
mode: Returns the mode in which the file was opened.
closed: Returns True if the file is closed, False otherwise.
You can access these attributes using the dot notation. For example:

```python
file = open("example.txt", "r")
print(file.name)  # Print the file name
print(file.mode)  # Print the file mode
print(file.closed)  # Print whether the file is closed
file.close()  # Close the file
```

### 2.3 Using with Statement

To ensure that a file is properly closed, it's a good practice to use the with statement. This automatically takes care of closing
the file, even if an exception occurs.

Here's an example of using the with statement:

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

In this example, the file is automatically closed when the code block inside the with statement is exited, whether by completing
the block or encountering an exception.

### 2.4 Summary

In this section, we explored some of the methods and attributes provided by file objects in Python. These features allow you to 
perform various operations on files, such as reading, writing, seeking, and obtaining information about the file. Remember to close
the file after you have finished working with it to free up system resources. The with statement provides a convenient way to ensure
that the file is properly closed.