# BOOLEANS
print('''BOOLEANS''')
print('''Booleans represent one of two values: True or False''')
print('''They are basically just the integers 1 and 0 and we use it to evaluate any Python expression''')
a = True
b = False
print("My boolean a:", a)
print("My boolean b:", b, "\n")


print("We can use var = None as a placeholder for an object that we don't want to reassign yet")
a = None
print("My boolean a:", a, "\n")


print('''Comparison operators allow us to compare variables and output boolean values''')
print("Equal operator ==")
a = (1 == 1)
print("My evaluation (1==1):", a)
print("Not equal operator !=")
a = (1 != 1)
print("My evaluation (1!=1):", a)
print("Greather than operator >")
a = (2 > 1)
print("My evaluation (2>1):", a)
print("Less than operator <")
a = (2 < 1)
print("My evaluation (2<1):", a)
print("Greather than or equal to operator >=")
a = (1 > 1)
print("My evaluation (2>=1):", a)
print("Less than or equal to operator <=")
a = (3 <= 6)
print("My evaluation (3 <= 6):", a)


print('''We can chain multiple comparisons to perform more complex evaluations''')
print("And evaluation is true when all connected expressions are true")
a = (1 == 1) and (2 == 2)
print("My evaluation (1 == 1) and (2 == 2):", a)
print("Or evaluation is true when one of all connected expressions is true")
a = (1 == 1) or (3 == 2)
print("My evaluation (1 == 1) or (3 == 2):", a)



