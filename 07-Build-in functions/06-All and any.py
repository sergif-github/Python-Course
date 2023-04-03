# ALL and ANY
print('''ALL and ANY''')

print('''All() and any() are built-in functions in Python that allow to conveniently check for boolean matching
 in an iterable.''')

lst = [True, True, False, True]
print("My list: ", lst)

print('''\nAll() will return True if all elements in an iterable are True''')
print("Are all elements true? ", all(lst))

print('''\nAny() will return True if any of the elements in the iterable are True''')
print("Are any elements true? ", any(lst))
