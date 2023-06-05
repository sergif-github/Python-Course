# Module 11: Additional Python Modules and Libraries

## Part 5: Zip Files (zipfile module)

The `zipfile` module in Python provides functionalities for creating, extracting, and manipulating zip files. Zip files are compressed
archives that can contain one or more files and directories.

### 5.1 Zipfile module

To work with zip files in Python, you don't need to install any additional modules as the `zipfile` module is part of the standard library.

Here's an example that demonstrates some basic operations with zip files:

```python
import zipfile

# Create a new zip file
with zipfile.ZipFile("archive.zip", "w") as zip_file:
    # Add files to the zip file
    zip_file.write("file1.txt")
    zip_file.write("file2.txt")
    zip_file.write("directory/file3.txt")

# Extract files from a zip file
with zipfile.ZipFile("archive.zip", "r") as zip_file:
    zip_file.extractall("extracted_files")

# List files in a zip file
with zipfile.ZipFile("archive.zip", "r") as zip_file:
    file_list = zip_file.namelist()
    for file_name in file_list:
        print(file_name)

# Open and read a specific file from a zip file
with zipfile.ZipFile("archive.zip", "r") as zip_file:
    with zip_file.open("file1.txt") as file:
        content = file.read()
        print(content)
```

In this example, we import the zipfile module and use it to perform various operations on a zip file. Here's what each step does:
- We create a new zip file using the ZipFile constructor with mode "w" (write).
- We add files to the zip file using the write() method, specifying the file or directory to be added.
- We extract files from the zip file using the extractall() method, specifying the target directory where the files should be extracted.
- We list the files in the zip file using the namelist() method, which returns a list of file names.
- We open and read a specific file from the zip file using the open() method, specifying the file name. We can then read the content
of the file using the read() method.

## 5.2 Summary

The zipfile module provides additional functionalities for working with zip files, such as deleting files from a zip, adding files
with different compression levels, and more. You can refer to the official Python documentation for detailed information on the zipfile module and its capabilities.