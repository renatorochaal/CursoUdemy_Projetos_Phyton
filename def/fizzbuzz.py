"""
Função FizzBuzz
div 3 = Fizz
div 5 = Buzz
div 3 e 5 = FizzBuzz

"""


def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'FizzBuzz, {n} é divisível por 3 e 5'
    if n % 5 == 0:
        return f'Buzz, {n} é divisível por 5'
    if n % 3 == 0:
        return f'Fizz, {n} é divisível por 3'
    return n


# importando uma biblioteca
from random import randint
for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))