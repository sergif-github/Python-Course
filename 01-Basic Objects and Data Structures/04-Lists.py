# LISTS
print('''LISTS''')
print('''Lists are sequences same as strings but they are mutable and can contain different object types''')
a = ['string var', 10, 40.57, 'x', ["another", "list inside", 30]]
print("My list: ", a)


print("List indexing")
print('''Use list_variable[index] to acces specific list elements starting from 0''')
print("This is my list: ", a)
print("First and last element: ", a[0], "", a[len(a)-1], "\n")
print('''Grabing multiple with mystring_variable[:] ''')
print("All string a[:] ", a[:])
print("First element a[1] ", a[1])
print("Last element a[-1] ", a[-1])
print("Everything without first 3 letters a[3:] ", a[3:])
print("Everything without last 3 letters a[:-3] ", a[:-3])
print("Everything with steps sizes of 2 a[::2] ", a[::2], "\n")


print("List operations")
print('''Use list_variable1 + list_variable2 to concatenate string variables''')
a = [10, 20, 30]
b = [40, 50, 60]
print("This is my first list: ", a)
print("This is my second list: ", b)
print("Using a+b: ", a + b, "\n")
print('''Use list_variable1*number to create repetitions''')
print("Using a*3: ", a*3, "\n")


print('''List build-in methods''')
print("Using len(a) to get list lenght: ", len(a))
a.append('new item')
print("Using a.append(element) to append a new element at the end of the list: ", a)
a.pop(2)
print("Using a.pop(2) to take off an existent element (second) identifyed by index 2: ", a)
a.reverse()
print("Using a.reverse() to reverse list: ", a)
a = [10,5,2,7,8,1,0]
b = ["a","z","b","j","o","r"]
print("This is my first list: ", a)
print("This is my second list: ", b)
a.sort()
b.sort()
print("Using a.sort() to sort integer list ascending or string lists in alphabetical: ", a)
print("Using b.sort() to sort string list in alphabetical : ", b, "\n")


print('''Nesting lists (Matrix)''')
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
print("This is my first list: ", a)
print("This is my second list: ", b)
print("This is my third list: ", c)
d = [a, b, c]
print("Using new_list = [list1, list2, list3] my new nested list is: ", d, "and has", len(d), "elements\n")
print("Using new_list[1] to acces first element", d[1])
print("Using new_list[1][1] to acces first element of first nested list (matrix)", d[1][1])
