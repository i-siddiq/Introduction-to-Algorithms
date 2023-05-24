# factorial by using reduce function
from functools import reduce


def factorial(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda a, b: a * b, range(1, n + 1))


n = 5
print(factorial(n))
