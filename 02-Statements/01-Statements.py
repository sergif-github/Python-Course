# STATEMENTS
print('''STATEMENTS''')
print('''Python gets rid of () and {} by incorporating two main factors: a colon and whitespace. ''')
print('''The statement is ended with a colon, and whitespace is used (indentation) to describe what takes place in case of the statement.''')
print('''Also Python don't use semicolons ( ; ) to denote statement endings.\n''')

a = 2
b = 1
print("My a value:", a)
print("My b value:", b)
if a>b:
    print("Inside to first statement")
    if a != b:
        print("Inside second statement")
        a = 2
        b = 4

print("My a value:", a)
print("My b value:", b)