# LAMBDA EXPRESSIONS
print('''LAMBDA EXPRESSIONS''')
print('''Lambda expressions allow us to create "anonymous" functions without needing to properly define a function''')
print('''   Lambda's body it's limited to a single expression, not a block of statements''')


def square(num):
    result = num**2
    return result


print('''Square with a lambda funciton => lambda num: num ** 2''')

my_nums = [1, 2, 3, 4, 5]
# Map allows us to ''map'' a function (lambda expresion) to an iterable object (list)
print(list(map(lambda num: num ** 2, my_nums)))

# Filter returns an iterator for items of iterable object for witch function is true
print(list(filter(lambda n: n % 2 == 0, my_nums)))

print(list(map(lambda n1, n2: n1+n2, my_nums, my_nums)))
