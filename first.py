def factorial(n):
    if n == 1: return 1
    else: return n * factorial(n - 1)

def power(base, exp):
    if exp == 0: return 1
    else: return base * power(base, exp - 1)

def display():
    print('hello  git')