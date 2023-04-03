# CODE TIMMING
print('''CODE TIMMING''')

import time


def func_one(n):
    return [str(num) for num in range(n)]


print("The time module simply calculate the elapsed time for the code. It needs to take at least 0.1 seconds")
start_time = time.time()
result = func_one(1000000)
end_time = time.time() - start_time
print('Time of func_one:', end_time)


import timeit

print("\nThe difference from the time.time() method may not be enough to tell which is code block is faster. "
      "In this case, we can use the timeit module")
print("The timeit module takes in two strings, a statement (stmt) and a setup. "
      "It runs the setup code and runs the stmt code some n number of times and reports back the average time it took.")
setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
print('Average time of func_one:', timeit.timeit('func_one(100)', setup, number=100000))




