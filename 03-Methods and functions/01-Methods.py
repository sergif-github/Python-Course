# METHODS
print('''METHODS''')
print('''Methods are functions build into objects. 
They perform specific actions on an object and can also take arguments.''')
print('''For example, some list object type build-in methods are: 
        append, count, extend, insert, pop, remove, reverse, sort \n''')

a = [10, 20, 30]
print("This is my list:", a)
a.append(50)
print("List after append 50:", a)
print("List count 30:", a.count(30))
a.extend([60, 70, 80])
print("List after a.extend([60,70,80]):", a)
a.insert(3,40)
print("List after a.insert(3,40):", a)
a.pop()
print("List after a.pop()", a)
a.remove(20)
print("List after a.remove(20)", a)
a.reverse()
print("List after a.reverse()", a)
a.sort()
print("List after a.sort()", a)