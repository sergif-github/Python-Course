# WHILE LOOP
print('''WHILE LOOP''')
print('''A while statement will repeatedly execute a statement as long as the condition is true.''')
print('''   break: Breaks out of the current closest enclosing loop.
   continue: Goes to the top of the closest enclosing loop.
   pass: Does nothing at all.\n''')
      
x = 0
while x < 10:
    print('x is currently:', x)
    print(' x is still less than 10, adding 1 to x')
    x += 1
    if x == 3:
        print('Breaking while because x == 3')
        break
    else:
        print('continuing...')
        continue
else:
    # Not reached because while break
    # This is only reached when while condition is false
    print('x is equal 3')

