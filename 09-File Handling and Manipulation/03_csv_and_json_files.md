# Module 9: File Handling and Manipulation

## Part 4: CSV and JSON File Processing

In addition to working with plain text files, Python provides built-in support for processing CSV (Comma-Separated Values) 
and JSON (JavaScript Object Notation) files. In this section, we will explore how to read and write data in CSV and JSON formats.

### 4.1 CSV File Processing

CSV files are commonly used for storing tabular data, where each row represents a record and the values are separated by commas. 
Python provides the `csv` module for reading and writing CSV files.

To read data from a CSV file, you can use the `csv.reader()` function. Here's an example:

```python
import csv

with open("data.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
```

In this example, we open the CSV file "data.csv" in read mode and create a csv_reader object using the csv.reader() function. 
We can then iterate over the csv_reader object to access each row as a list of values.

To write data to a CSV file, you can use the csv.writer() function. Here's an example:

```python
import csv

data = [
    ["Name", "Age", "Country"],
    ["John", 25, "USA"],
    ["Alice", 30, "Canada"],
    ["Bob", 28, "UK"]
]

with open("data.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
```

In this example, we have a list of lists representing the data to be written to the CSV file. We open the file "data.csv"
in write mode and create a csv_writer object using the csv.writer() function. We then use the writerows() method to write 
all the rows of data to the CSV file.

### 4.2 Splitting CSV Files with Desired Delimiter

Sometimes, you may encounter CSV files where the values are not separated by commas but by a different delimiter. In such cases,
you can specify the desired delimiter when reading or writing the CSV file.

For example, to split a CSV file with a semicolon (;) delimiter, you can modify the code as follows:

```python
import csv

with open("data.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter=";")
    for row in csv_reader:
        print(row)
```


In this example, we pass the delimiter=";" argument to the csv.reader() function, specifying that the values in the CSV file are separated by semicolons.

Similarly, when writing data to a CSV file with a different delimiter, you can specify the desired delimiter in the csv.writer() function:

```python
import csv

data = [
    ["Name", "Age", "Country"],
    ["John", 25, "USA"],
    ["Alice", 30, "Canada"],
    ["Bob", 28, "UK"]
]

with open("data.csv", "w", newline="") as file:
    csv_writer = csv.writer(file, delimiter=";")
    csv_writer.writerows(data)
```

In this example, we pass the delimiter=";" argument to the csv.writer() function, specifying that the values in the CSV file should be separated by semicolons.

By using the appropriate delimiter, you can handle CSV files with different separators and process the data accordingly.

### 4.3 JSON File Processing

JSON files are used for storing structured data in a human-readable format. Python provides the json module for working with JSON files.

To read data from a JSON file, you can use the json.load() function. Here's an example:

```python
import json

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
```

In this example, we open the JSON file "data.json" in read mode and use the json.load() function to load the data from the file
into a Python object. We can then work with the data as a dictionary, list, or other suitable data structure.

To write data to a JSON file, you can use the json.dump() function. Here's an example:

```python
import json

data = {
    "name": "John",
    "age": 25,
    "country": "USA"
}

with open("data.json", "w") as file:
    json.dump(data, file)
```

In this example, we have a dictionary representing the data to be written to the JSON file. We open the file "data.json" in write 
mode and use the json.dump() function to write the data to the file in JSON format.

### 4.4 Summary

In this section, we explored how to process CSV and JSON files in Python. The csv module provides functions for reading and writing
CSV files, allowing you to work with tabular data. The json module allows you to read and write JSON files, which are commonly
used for storing structured data. Understanding how to work with CSV and JSON files is crucial for handling data in 
various formats within your Python programs.