#STRINGS
print('''STRINGS''')
#Strings are used in Python to record text information. They are actually a sequence. We can track every element.
# Also, they are immutable, elements cannot be changed or replaced
print("String constructor")
a = 'Hello world in a single quote (\') character'
b = "Hello world in a double quote (\") character"
c = '''Hello world in a triple quote (\'\'\') character that has a single (') and a double (") quote'''
print(a)
print(b)
print(c)
print('''Use print('\\n') to do a new line\n''')


print("String indexing")
print('''Use mystring_variable[index] to acces specific string elements starting from 0''')
print("This is my string: ", a)
print("First and last element: ", a[0],"", a[24], "\n")
print('''Grabing multiple with mystring_variable[:] ''')
print("All string a[:] ", a[:])
print("First letter a[1] ", a[1])
print("Last letter a[-1] ", a[-1])
print("Everything without first 3 letters a[3:] ", a[3:])
print("Everything without last 3 letters a[:-3] ", a[:-3])
print("Everything with steps sizes of 2 a[::2] ", a[::2],"\n")


print("String operations")
print('''Use string_variable1 + string_variable2 to concatenate string variables''')
a = "My first string"
b = " My second string"
print("This is my first string: ", a)
print("This is my second string: ", b)
print("Using a+b: ", a + b, "\n")
print('''Use string_variable1*number to create repetitions''')
print("Using (a+\" \"\)*3: ", (a+" ")*3, "\n")


print('''String build-in methods''')
print("Using len(a) to get string lenght: ", len(a))
print("Using a.upper(): ", a.upper())
print("Using a.lower(): ", a.lower())
print("Using a.split() to split blank spaces: ", a.split())
print("Using a.split('f'): ", a.split('f'), "\n")


print('''Strings to integer bases''')
#   Strings can be prepended to an integer value to indicate a base other than 10 (0+lower/upper case letter)
#   Binary base 2
print('''Using 0b10 or 0B10 to get binary base''')
print("Using 0b10: ", 0b10)
print("Using 0B10: ", 0B10)
#   Octal base 8
print('''Using 0o10 or 0O10 to get octal base''')
print("Using 0o10: ", 0o10)
print("Using 0O10: ", 0O10)
#   Hexadecimal base 16
print('''Using 0x10 or 0x10 to get hexadecimal base''')
print("Using 0x10: ", 0x10)
print("Using 0X10: ", 0X10,"\n")

