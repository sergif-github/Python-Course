# FUNCTIONS
print('''FUNCTIONS''')
print('''Functions are groups of statements. They allow us to not have repeatedly write the same code.''')


def add_num(arg1, arg2):
    print('add_num result:', arg1+arg2)


def add_num_2(arg1, arg2):
    return arg1+arg2


add_num(1, 2)

print('''Return keyword allows us to save the result of the output''')
result = add_num_2(1, 2)
print("add_num_2 result:", result)


def check_even_list(num_list):
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers


result = check_even_list([1, 2, 3, 4, 5, 6])
print("check_even_list([1,2,3,4,5,6]):", result)


def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


primes = count_primes2(100)
print("count_primes2(100)", primes)

