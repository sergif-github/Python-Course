print("Generators allow us to generate as we go along, instead of holding everything in memory.")
print("Generator functions can send back a value and then later resume to pick up where it left off")
print("Using yield, we can define new generators that act like this, automatically suspending and resuming"
      " their execution and state around the last point of value generation")


def genfibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


for num in genfibon(10):
    print(num)


print("Next() function access the next element in a sequence")
# Like this we are creating a generator and accessing the first element with the iterator
print(next(genfibon(10)))
print(next(genfibon(10)))
print(next(genfibon(10)))

print("\nWe need to assign the generator to keep accessing the next iterator value")
a = genfibon(10)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# After yielding all the values next() caused a StopIteration error
# A for loop automatically catches this error and stops calling next()


print("\nThe iter() function allows us to create an iterator for the given objects that are iterable")
s = "String"
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
