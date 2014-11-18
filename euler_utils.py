from fractions import gcd
from functools import reduce, wraps
from math import sqrt
import time

__author__ = 'darryl'


def lcm(a, b):
    return a * b // gcd(a, b)


def lcmm(*args):
    return reduce(lcm, *args)


def is_prime(number):
    n = abs(int(number))
    if n <= 2:
        return n == 2
    if not n & 1:
        return False
    x = 3
    while x < int(sqrt(n)) + 1:
        if n % x == 0:
            return False
        x += 2
    return True


def factorize_primes(number, div=2, primes=list(), initialized=True):
    if initialized and len(primes):
        # print("On start, list contains", factors)
        primes = []
    if number <= 1:
        if len(primes):
            return primes
        else:
            return []
    if number == 2:
        if len(primes):
            primes.append(number)
            return primes
        else:
            return [2]
    if is_prime(div):
        while not number % div:
            primes.append(div)
            # print('Adding %d to list' % div)
            number //= div
            # print('Div is now %d' % number)
            # print('List now contains', factors)
    return factorize_primes(number, div + 1, primes, initialized=False)


def timeit(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        start = time.clock()
        result = f(*args, **kwargs)
        end = time.clock()
        print("Execution of %s took %f seconds" % (f.__name__, end - start))
        return result

    return decorator