# Module 10: File Handling and Manipulation

## Part 3: File Modes and File Paths

When working with files in Python, it's important to understand file modes and how to work with file paths. In this section,
we will explore these concepts.

### 3.1 File Modes

File modes define how a file should be opened and accessed. When opening a file, you need to specify the mode as a second argument
to the `open()` function. Here are some commonly used file modes:

- `'r'`: Read mode. Opens the file for reading. Raises an error if the file does not exist.
- `'w'`: Write mode. Opens the file for writing. Creates a new file if it doesn't exist, or truncates the file if it does.
- `'a'`: Append mode. Opens the file for appending. The file pointer is at the end of the file, and new data is written to the end.
- `'x'`: Exclusive creation mode. Creates a new file, but raises an error if the file already exists.
- `'b'`: Binary mode. Opens the file in binary mode, allowing you to read or write binary data.
- `'t'`: Text mode. Opens the file in text mode, which is the default. In text mode, data is encoded as Unicode strings.

You can combine multiple modes by specifying them as a string. For example, `'rb'` opens the file in binary mode for reading.

### 3.2 File Paths

A file path is the location of a file on the file system. In Python, you can use either a relative or an absolute file path to refer
to a file. Here are a few examples:

- Relative file path: `"example.txt"` (refers to a file in the current directory)
- Absolute file path: `"C:/Documents/example.txt"` (refers to a file using the full path)

When working with file paths, it's important to consider the platform you are working on. On different operating systems, file paths
may use different separators. For example, Windows uses backslashes (`\`) as the separator, while Unix-based systems use forward slashes (`/`).

To handle file paths in a platform-independent way, you can use the `os` module in Python, which provides functions for working with
file paths. Here's an example:

```python
import os

# Joining file path components
file_path = os.path.join("directory", "example.txt")

# Checking if a file exists
if os.path.exists(file_path):
    print("File exists")
else:
    print("File does not exist")
```

In this example, the os.path.join() function is used to join the directory and file name components to create a file path.
The os.path.exists() function is used to check if the file exists.

### 3.3 Summary

In this section, we explored file modes and file paths in Python. File modes allow you to specify how a file should be opened and accessed, 
such as for reading, writing, or appending. File paths represent the location of a file on the file system and can be either relative or absolute.
The os module provides functions for working with file paths in a platform-independent way. Understanding file modes and file paths is essential 
for effectively working with files in Python.