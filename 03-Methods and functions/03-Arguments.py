# ARGUMENTS
print('''ARGUMENTS''')
print('''In function definitions we eventually encounter *args and **kwargs as parameters''')
print('''*args and **kwargs provide the flexibilty to work with arbitrary numbers of arguments!''')


def myfunc(arg1, arg2):
    print('''Arg1 and arg2 are positional arguments''')
    print(str(arg1 + arg2)+'\n')


def myfunc2(arg1=0, arg2=0):
    print('''Arg1 and arg2 are positional arguments with default values''')
    print(str(arg1 + arg2)+'\n')


def myfunc3(*args):
    print('''A function starting with * allows an arbitrary number of arguments and takes them in a tuple''')
    print(str(sum(args))+'\n')


def myfunc4(**kwargs):
    print('''**kwargs instead of accepting positional arguments it accepts keyword (or named) arguments''')
    print('''Instead of creating a tuple of values, **kwargs builds a dictionary of key/value pairs''')
    result = 0
    for arg in kwargs.values():
        result += arg
    print(str(result)+'\n')


def myfunc5(*args, **kwargs):
    print('''When working with *args and **kwargs into the same function, *args have to appear before **kwargs''')
    result = 0
    for arg in kwargs.values():
        result += arg
    print(str(sum(args)+result)+'\n')


myfunc(40, 60)
myfunc2(40)
myfunc3(40, 50, 60, 70)
myfunc4(a=1, b=2, c=3, d=4, e=5)
myfunc5(40, 60, a=1, b=2, c=3, d=4, e=5)
