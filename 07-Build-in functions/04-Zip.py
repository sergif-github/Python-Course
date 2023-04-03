# ZIP
print('''ZIP''')

print('''Zip() makes an iterator that aggregates elements from each of the iterables.''')
print('''The iterator stops when the shortest input iterable is exhausted.''')

x = [1, 2, 3]
y = [4, 5, 6, 7, 8]
print("My list x: ", x)
print("My list y: ", y)

# Zip the lists together
lst = list(zip(x, y))
print("My zipped list: ", lst)


d1 = {'a' : 1, 'b': 2}
d2 = {'c' : 4, 'd': 5}

print("My dict 1: ", d1)
print("My dict 2: ", d2)
lst2 = list(zip(d1, d2))
print("My zipped dictionaries keys: ", lst2)
lst3 = list(zip(d1.values(), d2.values()))
print("My zipped dictionaries values: ", lst3)

