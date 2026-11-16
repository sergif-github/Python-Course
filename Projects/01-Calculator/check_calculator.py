"""Открытые проверки базовых функций проекта «Калькулятор»."""

from calculator import add, divide, exponentiate, multiply, subtract


assert add(2, 3) == 5
assert add(-2, 2) == 0
assert subtract(10, 4) == 6
assert multiply(3, 5) == 15
assert multiply(0, 100) == 0
assert divide(8, 2) == 4
assert exponentiate(2, 3) == 8

print("Базовые проверки пройдены.")
