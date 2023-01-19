# STRING FORMATING

print('''Formatting with placeholders''')
a = "text1"
b = "text2"
print("We can print text here: %s, and here %s .\n"%(a,b))


print('''Format conversion methods''')
a = "\ttext1"
print('%s and %r convert any python object to string using methons str() and repr()')
print("My string is text1\\t")
print("My string using %s is:")
print("%s"%a)
print("My string using %r is:")
print("%r"%a)
print('%d converts numbers into integers without rounding ')
a = 340.57438
print("My number using %s is:")
print("%s"%a)
print("My number using %d is:")
print("%d\n"%a)


print('''Padding and Precision of Floating Point Numbers''')
print("We can format our floating point number to print desired real and decimal part length")
print("My number value is: ",a)
print('''My number using %10.2f is:''')
print('%10.2f' %a)
print('''My number using %1.2f is:''')
print('%1.2f' %a)
print('''My number using %20.10f is:''')
print('%20.10f \n' %a)


print('''Output formating''')
a = 10
b = 20
print("This is a comma separated string with value1 = ", a, "value2 = ", b)
print('This is a string using curly brackets value1 = {}, value2 = {}'.format(a, b))
print('This is a string using curly brackets and passing new values value1 = {a}, value2 = {c}'.format(a=50, b=25, c=40))

print('''Output alignment''')
print('''Creating a price table''')
print('{0:10} | {1:10}'.format('Fruit', 'Price'))
print('{0:10} | {1:0}'.format('Apples', 3))
print('{0:10} | {1:0}'.format('Oranges', 10))
print('{0:10} | {1:0} \n'.format('Bananas', 7))
print('''Format align to left by default. <, ^ and > are used to set left, center or right alignment''')

print('''Creating a aligned price table''')
print('{0:<8} | {1:^8} | {2:>8}'.format('Fruit', 'Quantity', 'Price'))
print('{0:<8} | {1:^8} | {2:>8}'.format('Apples', 20, 3))
print('{0:<8} | {1:^8} | {2:>8}'.format('Oranges', 5, 10))
print('{0:<8} | {1:^8} | {2:>8}\n'.format('Bananas', 40, 7))

print('''Creating a aligned price table with padding characters''')
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Fruit', 'Quantity', 'Price'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Apples', 20, 3))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Oranges', 5, 10))
print('{0:=<8} | {1:-^8} | {2:.>8}\n'.format('Bananas', 40, 7))

print('''Creating a aligned price table with padding characters using f-strings''')
print(f"{'Apples':=<8} | {20:-^8} | {3:.>8}")
print(f"{'Oranges':=<8} | {5:-^8} | {10:.>8}")
print(f"{'Bananas':=<8} | {40:-^8} | {7:.>8}")