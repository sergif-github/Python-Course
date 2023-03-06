# SCOPE
print('''SCOPE''')
print('''Name assignments will create or change local names by default''')
print('''Name references search (at most) four scopes:''')
print('''   Local, enclosing functions, global and build-in''')
print('''All variables have the scope of the block they are declared \n''')

print('''Local names are those assigned within a function (def or lambda)''')
# x is local
lambda x: x + 2
print('\n')

print('''Enclosing function locals are those assigned inside a function''')
def sum_function(arg1, arg2):
    # ret is an enclosing funciton local
    ret = arg1+arg2
    return ret


print('''A global name is recognized from all scopes''')
x = 'global name'
print('\n')

print('''A build-in function name is reserved and cannot be overwrited such as (len or range)''')
print('\n')

print('''To tell Python that the name that we use is not local, but it's global, we use the global statement:''')
x = 50


def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)


print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)
