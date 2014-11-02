import random
import timeit

__author__ = 'darryl'


def find_min_lineair(the_array):
    result = 0
    for i in the_array:
        if i < result or result == 0:
            result = i
    return result


def find_min_quadratic(the_array):
    result = 0
    for i in the_array:
        check = i
        for y in the_array:
            if check > y:
                check = y
        if check < result or result == 0:
            result = check
    return result


def main():
    values = [random.randrange(1, 50) for i in range(20)]
    setup = """
from __main__ import find_min_lineair
from __main__ import find_min_quadratic
"""
    t1 = timeit.Timer("find_min_lineair(%s)" % values, setup=setup)
    t2 = timeit.Timer("find_min_quadratic(%s)" % values, setup=setup)
    for i in range(5):
        n_size = 10*10**(i+1)
        print("With a problem size of %d, lineair search took %f seconds" % (n_size, t1.timeit(number=n_size)))
        print("With a problem size of %d, quadratic search took %f seconds" % (n_size, t2.timeit(number=n_size)))

if __name__ == "__main__":
    main()