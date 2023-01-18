
#Integer / Int
print('''Integer numbers''')
#   Positive or negative numbers
#   Has no limit on how long value can be
a = 50
b = 25
print("Data type of a is", type(a), " with value ", a)
print("Data type of a is", type(b), " with value ", b)
print("")

#Arithmetic operations
print('''Arithmetic operations''')
# Addition
print("a + b = ", a+b)
# Subtraction
print("a - b = ", a+b)
# Multiplication
print("a * b = ", a*b)
# Division
print("a / b = ", a/b)
# Floor Division (Truncates decimal part of the division)
print("a // b = ", a//b)
# Module
print("a % b = ", a%b)
# Powers
print("a ^ b = ", a**b)
print("")

#Order of operations (Parentheses, exponentiation, multiplication, division, addition and subtraction)
print ('''Order of operations''')
print('''2 + 10 * 10 + 3 = ''', 2 + 10 * 10 + 3)
# We can use parentheses to specify desired order of operations
print('''(2+10) * (10+3) = ''', (2+10) * (10+3))
print("")

#When reassigning variables we can use shortcuts
print ('''Reassign variables shortcuts''')
print("a = a + 10  =>  a += 10 ")
a += 10
print(a)
print("a = a - 10  =>  a -= 10 ")
a += 10
print(a)
print("a = a * 10  =>  a *= 10 ")
a += 10
print(a)
print("a = a / 10  =>  a -/ 10 ")
a += 10
print(a)


#Float
print('''Float numbers''')
#   Decimal point numbers or exponential (e)
#   1.8 * 10^308 maximum value
a = 20.5654
#   Infinite
b = 1.8e308
print("Data type of a is", type(a), " with value ", a)
print("Data type of a is", type(b), " with value ", b)

#   Closest to 0
a = 5e-324
#   Effectively zero
b = 1e-325
print("Data type of a is", type(a), " with value ", a)
print("Data type of a is", type(b), " with value ", b)
print("")

#Complex
print('''Complex numbers''')
a = 100 + 1j
print("Data type of a is", type(a), " with value ", a)


