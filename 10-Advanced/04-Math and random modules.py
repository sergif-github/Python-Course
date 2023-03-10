import math
# help(math)

print("Math module")
print("My value ", 4.35)
print("To upper integer math.floor(value):", math.floor(4.35))
print("To lower integer math.ceil(value):", math.ceil(4.35))
print("round(value):", round(4.35))
print("math.pi:", math.pi)
print("math.e:", math.e)
print("math.tau:", math.tau)
print("math.inf:", math.inf)
print("math.nan:", math.nan)
print("math.log(math.e):", math.log(math.e))
# print("math.log(0):", math.log(0))
print("math.log(10):", math.log(10))
print("math.e ** 2.302585092994046:", math.e ** 2.302585092994046)
print("math.log(100,10):", math.log(100, 10))
print("10**2:", 10**2)
print("math.sin(10):", math.sin(10))
print("math.cos(10):", math.cos(10))
print("math.degrees(pi/2):", math.degrees(math.pi/2))
print("math.radians(180):", math.radians(180))


print("\nRandom module")
print("Random Module allows us to create random numbers. We can set a seed to produce the same random set every time.")

import random

print("Random between 0 and 100:", random.randint(0, 100))
random.seed(50)
print("Random between 0 and 100 after putting a seed:", random.randint(0, 100))
print("Second random between 0 and 100 after putting a seed:", random.randint(0, 100))
random.seed(50)
print("Random between 0 and 100 after putting the same seed:", random.randint(0, 100))
print("Second random between 0 and 100 after putting the same seed:", random.randint(0, 100))

lst = list(range(0, 20))
print("My list: ", lst)
print("Random element from list: ", random.choice(lst))
print("10 random element from list: ", random.choices(population=lst, k=10))
random.shuffle(lst)
print("My list after suffle: ", lst)

print("Random from a 0 to 100 uniform distribution: ", random.uniform(a=0,b=100))
print("Random from a 0 to 100 normal / gaussian distribution: ", random.gauss(mu=0,sigma=1))


