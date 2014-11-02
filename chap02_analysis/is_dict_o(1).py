import timeit

__author__ = 'darryl'


if __name__ == '__main__':
    for i in range(4):
        n_size = 100*10**(i+1)
        values = dict(zip([i for i in range(n_size)], [None for i in range(n_size)]))
        t = timeit.Timer("values[200] = True", setup="values = %s" % str(values))
        print("%f seconds expired for a problem size of %d" % (t.timeit(number=1000), n_size))