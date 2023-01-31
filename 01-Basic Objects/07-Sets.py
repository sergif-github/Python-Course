# SETS
print('''SETS''')
print('''Sets are unordered collections of unique elements''')
print('''We can imagine a set like a dictionary with only keys''')
a = set()
print("A set is constructed via a = set()")
print("My set a:", a)
print("To add elements we use a.add(element)")
a.add(50)
a.add(30)
a.add(55)
a.add(55)
a.add(55)
print("My set a:", a, "\n")


print("With set() constructor we can create a set using a previous defined list")
a = [1, 1, 1, 2, 3, 4, 5, 5, 5, 10]
print("This is my list : ", a)
a = set(a)
print("This is my set : ", a, "\n")


print('''Set build-in methods''')
print('''Use len(set) to get set length''')
print("My set length: ", len(a))
