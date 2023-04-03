# FILTER
print('''FILTER''')

print('''Filter() filter out all the elements of an iterable, for which the function returns True.''')

lst = list(range(20))
print("My list: ", lst)
print("Even values in my list: ", list(filter(lambda x: x % 2 == 0, lst)))
print("Odd values in my list: ", list(filter(lambda x: x % 2 != 0, lst)))
