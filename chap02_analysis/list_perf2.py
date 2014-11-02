import timeit

__author__ = 'darryl'

if __name__ == '__main__':
    popzero = timeit.Timer("x.pop(0)",
                           "from __main__ import x")
    popend = timeit.Timer("x.pop()",
                          "from __main__ import x")

    x = list(range(2000000))
    print(popzero.timeit(number=1000))
    print(popend.timeit(number=1000))