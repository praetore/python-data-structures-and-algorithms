import timeit

__author__ = 'darryl'


for i in range(3):
    n_size = 100*10**(i+1)
    for x in range(5):
        values = dict(zip([i for i in range(n_size)], [None for i in range(n_size)]))
        stmt = """
to_del = len(values)-1
del values[to_del]
"""
        t = timeit.Timer(stmt=stmt, setup="values = %s" % str(values))
        print("%f seconds expired for a problem size of %d" % (t.timeit(number=1000), n_size))