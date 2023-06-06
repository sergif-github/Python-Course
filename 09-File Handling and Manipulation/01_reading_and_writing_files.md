# Module 9: File Handling and Manipulation

## Part 1: Reading and Writing Text Files

Reading and writing text files is a common task in many Python applications. In this section, we will explore how to open,
read, and write text files using Python.

### 1.1 Opening a Text File

To open a text file in Python, you can use the built-in `open()` function. It takes the file path as a parameter and returns
a file object that can be used to perform various operations on the file.

Here's an example of opening a text file named "example.txt" in read mode:

```python
file = open("example.txt", "r")
```

In this example, the file is opened in read mode using the "r" parameter. Other modes include "w" for write mode, "a" for 
append mode, and "x" for exclusive creation mode.

### 1.2 Reading from a Text File

Once you have opened a text file, you can read its contents using the read() or readline() methods of the file object.

The read() method reads the entire contents of the file as a single string:

```python
file = open("example.txt", "r")
content = file.read()
print(content)
```

The readline() method reads one line at a time from the file:

```python
file = open("example.txt", "r")
line = file.readline()
print(line)
```

You can also iterate over the file object directly to read each line in a loop:

```python
file = open("example.txt", "r")
for line in file:
    print(line)
```

### 1.3 Writing to a Text File

To write to a text file, you need to open it in write mode or append mode using the "w" or "a" parameter, respectively.

Here's an example of opening a file named "output.txt" in write mode and writing some content to it:

```python
file = open("output.txt", "w")
file.write("Hello, World!")
file.close()
```

In this example, the "w" parameter opens the file in write mode, and the write() method is used to write the specified content to the file.

To append content to an existing file, you can open it in append mode using the "a" parameter:

```python
file = open("output.txt", "a")
file.write("Appending new content.")
file.close()
```

### 1.4 Closing the File

After you have finished working with a file, it's important to close it using the close() method of the file object. 
This ensures that any resources associated with the file are properly released.

```python
file = open("example.txt", "r")
file.close()
```

### 1.5 Perform file operations

Alternatively, you can use the with statement, which automatically closes the file when you're done with it:

```python
with open("example.txt", "r") as file:
    # Perform file operations
```

Using the with statement is recommended as it ensures that the file is always closed, even if an exception occurs within the block.

### 1.6 Summary

In this section, we learned how to work with text files in Python. We explored opening files, reading their contents, writing to them,
and properly closing them. File handling is a fundamental skill for many Python applications, and understanding these concepts 
will help you effectively manipulate text files in your programs.