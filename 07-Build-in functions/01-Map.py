print('''Map() is a built-in Python function that takes in two or more arguments (A function and one or more iterables) 
and returns an iterator.''')
print('''We will cast map() as a list to see the results immediately.''')


def fahrenheit(celsius):
    return (9 / 5) * celsius + 32


temps = [0, 22.5, 40, 100]
F_temps = map(fahrenheit, temps)
print(list(F_temps))


print('''\nHowever we don't have to define our functions beforehand. We can use lambda expression insted.''')
print(list(map(lambda x: (9/5)*x + 32, temps)))


print('''\nMap() can accept more than one iterable that should be the same length. 
If not map() will stop as soon as the shortest iterable is exhausted.''')
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 10, 11, 12]
print(list(map(lambda x, y: x+y, a, b)))
print(list(map(lambda x, y, z: x+y+z, a, b, c)))
