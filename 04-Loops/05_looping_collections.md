# Module 4: Loops

## Part 5: Looping Through Collections

In Python, you can use loops to iterate through collections such as lists, tuples, strings, and dictionaries. This allows you to access 
and process each element or key-value pair within the collection. Let's explore how to loop through different types of collections:

### 5.1. Looping Through Lists and Tuples

To loop through a list or tuple, you can use the `for` loop in conjunction with the collection name. Here's an example:

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

print("Loop finished")
```

In this example, the for loop iterates over each element in the fruits list. The variable fruit takes on the value of each element in turn,
and the print statement displays the value. After iterating over all the elements, the message "Loop finished" is printed.

### 5.2. Looping Through Strings
Strings in Python are iterable, so you can also loop through each character in a string using a for loop. Here's an example:

```python
message = "Hello, World!"

for char in message:
    print(char)

print("Loop finished")
```

In this example, the for loop iterates over each character in the message string. The variable char takes on the value of each character in turn,
and the print statement displays the character. After iterating over all the characters, the message "Loop finished" is printed.

### 5.3. Looping Through Dictionaries
When looping through a dictionary, you can access both the keys and values using the items() method. Here's an example:

```python
student_scores = {"John": 85, "Alice": 92, "Bob": 78}

for name, score in student_scores.items():
    print(name, "scored", score)

print("Loop finished")
```

In this example, the for loop iterates over the key-value pairs in the student_scores dictionary. The variables name and score take on the key
and value of each pair, respectively, and the print statement displays the name and score. After iterating over all the key-value pairs, the message
"Loop finished" is printed.

### 5.4 Summary

In this part, you learned how to loop through different types of collections in Python. Use the for loop to iterate over lists, tuples, strings,
and dictionaries. Customize the loop based on the specific requirements of your program, and access the elements or key-value pairs within the collection as needed.