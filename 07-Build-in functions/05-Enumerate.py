# ENUMERATE
print('''ENUMERATE''')

print('''Enumerate allows you to keep a count as you iterate through an object. by returning a tuple (count, element''')

months = ['March', 'April', 'May', 'June']

for number, item in enumerate(months):
    print(number, "-", item)

print(list(enumerate(months, start=3)))
