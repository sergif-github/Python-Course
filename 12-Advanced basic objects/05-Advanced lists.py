# LISTS
print('''LISTS''')
print('''Lists are sequences same as strings but they are mutable and can contain different object types''')

# Append vs extend
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("This is my list: ", a)
a.append([11, 12, 13])
print("This is my list after a.append([11, 12, 13]): ", a)
a.extend([11, 12, 13])
print("This is my list after a.extend([11, 12, 13]): ", a, "\n")

# Indexing
print("a.index(3)): ", a.index(3), "\n")

# Insert and remove
a.insert(3, 3.5)
print("This is my list after a.insert(3, 3.5): ", a)
a.remove(3.5)
print("This is my list after a.remove(3.5): ", a)