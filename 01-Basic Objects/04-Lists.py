# LISTS
print('''LISTS''')
print('''Lists are sequences same as strings but they are mutable and can contain different object types''')
a = ['string var', 10, 40.57, 'x', ["another", "list inside", 30]]
print("My list: ", a)


print("List indexing")
print('''Use list_variable[index] to acces specific list elements starting from 0''')
print("This is my list: ", a)
print("First and last element: ", a[0], "", a[len(a)-1], "\n")
print('''Grabbing multiple elements with list_variable[:] ''')
print("All list elements a[:] ", a[:])
print("First element a[0] ", a[0])
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
print("Using len(a) to get list length: ", len(a))
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
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
print("This is my first list: ", a)
print("This is my second list: ", b)
print("This is my third list: ", c)
d = [a, b, c]
print("Using new_list = [list1, list2, list3] my new nested list is: ", d, "and has", len(d), "elements\n")
print("Using new_list[1] to acces first element", d[1])
print("Using new_list[1][1] to acces first element of first nested list (matrix)", d[1][1])


print('''Zip generates tuples by zipping up together two lists''')
a = [10, 20, 30]
b = [40, 50, 60]
print("This is my first list: ", a)
print("This is my second list: ", b)
for item1, item2 in enumerate(zip(a,b)):
    print('For this tuple, first item was {} and second item was {}'.format(item1,item2))
print("This is my zipped list: ", list(zip(a, b)))
print('\n')


print('''In checks if an object is in a list''')
print("This is my list: ", a)
print("20 is in list", (20 in a))
print('\n')


print('''Not In checks if an object is not in a list''')
print("This is my list: ", b)
print("20 is not in list", (20 not in b))
print('\n')


print('''Max / Min gets maximum and minimum value in a list''')
print("This is my list: ", a)
print("Minimum is", min(a))
print("Maximum value is", max(a))
print('\n')


print('''Not In checks if an object is not in a list''')
print((20 not in b))
print('\n')


print('''Not In checks if an object is not in a list''')
print((20 not in b))
print('\n')

print('''The range function generate a list of integers''')
print("Generate a list of 10 integers from 0 to 10:", list(range(0, 11)))
print("Generate a list of squares:", [x**2 for x in range(0, 11)])
print("Generate a list of even numbers:", [x for x in range(11) if x % 2 == 0])
print("Generate a list of even numbers(2):", list(range(0, 11, 2)))
print('\n')

print('''Enumerate keeps track of how many loops we have been through by creating a tuple (iteration number, value)''')
for i, number in enumerate(list(range(0, 11))):
    print("At index {} the number is {}".format(i, number))
print('\n')
