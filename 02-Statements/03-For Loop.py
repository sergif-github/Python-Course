# FOR LOOP
print('''FOR LOOP''')
print('''For loop acts as an iterator in Python. It goes through items that are in a sequence or any iterable item.''')
print('''We can iterate over include strings, lists, tuples, and even built-in iterables for dictionaries, 
such as keys or values. \n''')

print("Iterate a numerical list")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list1:
    if num % 2 == 0:
        print('Even number', num)
    else:
        print('Odd number', num)
print('\n')

print("Iterate string characters")
for letter in 'Iterate a string':
    print(letter)
print('\n')

print("Iterate a list with tuples")
list2 = [(2, 4), (6, 8), (10, 12)]
for tup in list2:
    print(tup)
print('\n')

print("Unpacking a list with tuples")
for (elem1, elem2) in list2:
    print(elem1)
print('\n')

dict = {'k1': 1, 'k2': 2, 'k3': 3}
print("Iterate dictionary key and values")
for item1, item2 in dict.items():
    print(str(item1) +": "+ str(item2))
print('\n')

print("Iterate dictionary keys")
for item in dict:
    print(item)
print('\n')

print("Iterate dictionary keys with dict.keys()")
for item in dict.keys():
    print(item)
print('\n')

print("Iterate dictionary values with dict.values()")
for item in dict.values():
    print(item)
print('\n')