# REDUCE
print('''REDUCE''')

from functools import reduce

print('''Reduce() continually applies the function to the sequence. It then returns a single value.''')

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("My list: ", lst)
print("Sum all values: ", reduce(lambda x, y: x+y, lst))
print("Find max: ", reduce(lambda a, b: a if (a > b) else b, lst))
