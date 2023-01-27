# TUPLES
print('''TUPLES''')
print('''Tuples are sequences same as strings but they are immutable and can contain different object types''')
print('''Actually tuples are just immutable lists''')
a = (1, 2, 3, "x", "str")
print("My tuple a: ", a, "\n")


print("Tuple indexing")
print('''Use tuple_variable[index] to acces specific tuple elements starting from 0''')
print("This is my tuple: ", a)
print("First and last element: ", a[0], "", a[len(a)-1], "\n")
print('''Grabbing multiple elements with tuple_variable[:] ''')
print("All tuple elements a[:] ", a[:])
print("First tuple element a[0] ", a[0])
print("Last tuple element a[-1] ", a[-1], "\n")


print('''Tuple build-in methods''')
print('''Use len(tuple) to get tuple length''')
print("My tuple length: ", len(a))
print("Using tuple.index(\"element\") to get tuple index on element inside")
print("My tuple index of element 2:", a.index(2))
print("My tuple index of element x:", a.index("x"))
a = (1, 2, 3, "x", "str", 1, 2, 3, "x", "str")
print("Using tuple.count(\"element\") to get count of specific element inside")
print("My tuple a: ", a)
print("My tuple a.count(2): ", a.count(2))
