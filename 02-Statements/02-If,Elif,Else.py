# IF, ELIF, ELSE
print('''IF, ELIF, ELSE STATEMENTS''')
print('''If Statements allows us to tell the computer to perform alternative actions based on a certain results. 
We can then expand the idea further with elif and else statements. \n''')

x = 1
for i in range(3):
    if x == 1:
        print('X == 1')
    elif x == 2:
        print('X == 2')
    else:
        print('X != 1 && X != 2')
    x += 1
