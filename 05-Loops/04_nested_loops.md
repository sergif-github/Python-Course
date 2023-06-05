## Module 5: Loops

### Part 4: Nested Loops

In Python, you can nest loops within each other to create nested loops. A nested loop is a loop that is placed inside another loop. 
This allows you to iterate over multiple levels of data structures or perform complex repetitive tasks. Here's an example of a nested loop:

```python
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "blue"]

for fruit in fruits:
    for color in colors:
        print(fruit, color)

print("Nested loops finished")
```

In this example, we have two lists: fruits and colors. The outer for loop iterates over each fruit, and for each fruit, the inner 
for loop iterates over each color. The print statement inside the nested loops will display the combination of each fruit and color. The output will be:

```
apple red
apple yellow
apple blue
banana red
banana yellow
banana blue
cherry red
cherry yellow
cherry blue
```

Nested loops can be nested to any level as per your requirement. However, it's important to consider the performance implications 
of deeply nested loops, as they can result in a large number of iterations.

### 4.1 Summary

In this part, you learned about nested loops in Python. Nested loops allow you to iterate over multiple levels of data structures 
or perform complex repetitive tasks. Be cautious with deeply nested loops to avoid potential performance issues.