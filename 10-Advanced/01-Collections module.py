print("Collections is a built-in module that implements specialized alternative container data types alternatives")

print("\nCounter is a dict subclass which helps count hashable objects.")
print("Elements are stored as dictionary keys and the counts of the objects are stored as the value.")

from collections import Counter

lst = list(range(20))
print("My list", lst)
print("My list counter ", Counter(lst))
str = "a bb ccc dddd eeeee dddd ccc bb a"
print("My str", str)
print("My str counter ", Counter(str))
words = str.split()
print("My str words counter ", Counter(words))
print("My most common str words ", Counter(words).most_common())


print("\nDefaultdict is a dictionary-like object which provides all methods provided by a dictionary but takes"
      " a first argument (default_factory) as a default data type for the dictionary.\n")
print("The functionality of both are the same except that defaultdict never raises a KeyError. "
      "It provides a default value for the key that does not exists")
from collections import defaultdict

d = {}
# Error if
# d['one']
d = defaultdict(object)
print(d['one'])

# Can also initialize with default values:
d = defaultdict(lambda: 0)
print(d['one'])


print("\nThe standard tuple uses numerical indexes to access its members, for example:")
t = (12, 13, 14)
print("My tuple", t)
print("Value at index 0:", t[0])

print("\nA namedtuple assigns names, as well as the numerical index, to each member.")
print("They are like creating a class with some atributes")
from collections import namedtuple

tupleclass = namedtuple('newobj', ['atr1', 'atr2', 'atr3'])
a = tupleclass(atr1=1, atr2=2, atr3=3)
b = tupleclass(atr1='a', atr2='b', atr3='c')
print(tupleclass)
print("My namedtuple a: ", a)
print("My namedtuple b: ", b)

