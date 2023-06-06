# Module 9: File Handling and Manipulation

## Part 5: Error Handling with Files

When working with files, it's important to handle potential errors that may occur during file operations. Errors can arise when 
a file is not found, permissions are insufficient, or the file is already open by another process. Python provides mechanisms 
to handle these errors and ensure your program gracefully handles any issues.

### 5.1 Handling File-Related Errors

To handle file-related errors, you can use a `try-except` block. The `try` block contains the code that might raise an exception,
while the `except` block handles the exception if one occurs.

Here's an example of handling a `FileNotFoundError`:

```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist.")
```

In this example, we attempt to open the file "data.txt" for reading. If the file is not found, a FileNotFoundError is raised. 
We catch this specific exception in the except block and display a custom error message.

You can also handle other file-related exceptions, such as PermissionError and IOError, in a similar manner by adding additional
 except blocks.

### 5.2 Cleaning Up Resources with finally

The finally block allows you to define code that should be executed regardless of whether an exception occurs or not. It's commonly
 used for releasing resources, such as closing files, to ensure proper cleanup.

Here's an example of using finally to close a file:

```python
try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file does not exist.")
finally:
    file.close()
```

In this example, even if an exception occurs, the finally block will execute, ensuring that the file is properly closed.

### 5.3 Summary

In this section, we covered error handling with files. By using try-except blocks, you can gracefully handle file-related errors 
and provide appropriate error messages. Additionally, the finally block allows you to clean up resources, such as closing files, 
to ensure proper resource management.