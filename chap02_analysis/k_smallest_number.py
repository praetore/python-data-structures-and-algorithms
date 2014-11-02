import random
import timeit

__author__ = 'darryl'


def linear_find_smallest(values):
    smallest = len(values)
    for i in values:
        if smallest > i != 0:
            smallest = i
    return smallest


def loglinear_find_smallest(values):
    values.sort()
    smallest = len(values)
    for i in values:
        if smallest > i != 0:
            smallest = i
            del values[values.index(i):]
    return smallest


if __name__ == '__main__':
    values = random.sample([i for i in range(1, 10000)], len(range(1, 10000)))
    t = timeit.Timer("linear_find_smallest(%s)" % str(values),
                     setup="from __main__ import linear_find_smallest")
    print("Lineair: found in %f seconds" % t.timeit(number=1000))
    t = timeit.Timer("loglinear_find_smallest(%s)" % str(values),
                     setup="from __main__ import loglinear_find_smallest")
    print("Log linear: found in %f seconds" % t.timeit(number=1000))