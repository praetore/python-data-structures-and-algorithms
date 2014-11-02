import timeit

__author__ = 'darryl'


if __name__ == '__main__':
    values = [range(1000), range(10000), range(100000), range(1000000)]
    for i in range(len(values)):
        t = timeit.Timer("values[%s][200]" % i, setup="from __main__ import values")
        print("%f seconds expired for a problem size of %d" % (t.timeit(number=1000), len(values[i])))