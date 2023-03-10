print('''Decorators are functions which modify the functionality of another function. They help to make code shorter''')
print('''They are useful for web developers using Flask or Django''')


print("My global variables: ", globals())
print("My global dictionary keys: ", globals().keys())
print("My global dictionary values: ", globals().values())

print("My local variables in global scope: ", locals())


def locals_func_inside():
    x = 10
    print("My local variables in this function: ", locals())


locals_func_inside()


print("\nFunctions are objects which can be assigned labels and passed into other functions ")
x = locals_func_inside
x()
del locals_func_inside
x()

print("\nFunctions are objects so we can define new functions inside others ")


def hello(name='Jose'):
    print('hello() function executed')

    def hello1():
        return '\t hello1() function executed'

    def hello2():
        return '\t hello2() function executed'

    print(hello1())
    print(hello2())
    print("Back inside the hello() function")


hello()
print("\nFunctions are objects so we can define new functions inside others ")


def bye(y=10):
    print('bye() function executed')

    def bye1():
        return '\t bye1() function executed'

    def bye2():
        return '\t bye2() function executed'

    if y == 10:
        return bye1
    else:
        return bye2


x = bye()
print(x())


print("\nFunctions are objects so we can pass functions as objects ans then use then within other function ")


def a():
    return 'Hi inside a() \n'


def b(func):
    print('Hi2 inside b()')
    print(func())


b(a)


def decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func


def func_decorator():
    print("This function is in need of a Decorator")


func_needs_decorator = decorator(func_decorator)
func_needs_decorator()



