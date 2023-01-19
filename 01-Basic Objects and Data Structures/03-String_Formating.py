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
print("My number using %5.2f is:")
print("%s"%a)
print("My number using %d is:")
print("%d\n"%a)