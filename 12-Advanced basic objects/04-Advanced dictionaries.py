# ADVANCED DICTIONARIES
print('''ADVANCED DICTIONARIES''')
print('''Dictionaries are paired sequences with associated keys and values''')

# Dictionaries generators
a = {x: x**2 for x in range(10)}
print("My dict a: ", a)

# Iterators
print("Iterator thought keys")
for k in a.keys():
    print(k)

print("\nIterator thought values")
for v in a.values():
    print(v)

print("\nIterator thought keys + values")
for item in a.items():
    print(item)

print("\nGet all keys")
print(a.keys())

print("\nGet all values")
print(a.values())
