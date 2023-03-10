# NUMBERS
print('''NUMBERS''')

# Integer / Int
print('''Integer numbers''')
#   Positive or negative numbers
#   Has no limit on how long value can be
a = 50
b = 25
print("Data type of a is", type(a), " with value ", a)
print("Data type of b is", type(b), " with value ", b, "\n")


# Arithmetic operations
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
print("a ^ b = ", a**b, "\n")


# Order of operations (Parentheses, exponentiation, multiplication, division, addition and subtraction)
print ('''Order of operations''')
print('''2 + 10 * 10 + 3 = ''', 2 + 10 * 10 + 3)
# We can use parentheses to specify desired order of operations
print('''(2+10) * (10+3) = ''', (2+10) * (10+3), "\n")


# When reassigning variables we can use shortcuts
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
print(a,"\n")


# Float
print('''Float numbers''')
#   Decimal point numbers or exponential (e)
#   1.8 * 10^308 maximum value
a = 20.5654
#   Infinite
b = 1.8e308
print("Data type of a is", type(a), " with value ", a)
print("Data type of a is", type(b), " with value ", b)
#   Closest number to 0
a = 5e-324
#   Effectively zero
b = 1e-325
print("Data type of a is", type(a), " with value ", a)
print("Data type of a is", type(b), " with value ", b, "\n")


# Complex
print('''Complex numbers''')
a = 100 + 1j
print("Data type of a is", type(a), " with value ", a, "\n")


# Build-in functions
print('''Build-in functions''')
a = -10
b = 100.5528
print('''Using abs(variable) to get the absolute value''')
print("Value is ", a, ".Absolute value is", abs(a))
print('''Using divmod(variable, divisor) to get the quotient and remainder of integer division''')
print("Value is ", a, ".Auotient and remainder are", divmod(a, 2))
print('''Using round(variable, decimals) to round a floating-point value''')
print("Value is ", b, ".Rounded value is:", round(b), ".Rounded value with two decimals is:", round(b, 2), "\n")
