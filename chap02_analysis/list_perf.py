import timeit

__author__ = 'darryl'

# concat
def test1(n_size):
    the_list = []
    for i in range(n_size):
        the_list += [i]
    return the_list


# append
def test2(n_size):
    the_list = []
    for i in range(n_size):
        the_list.append(i)
    return the_list


# list comp
def test3(n_size):
    return [i for i in range(n_size)]


# list range
def test4(n_size):
    return list(range(n_size))


if __name__ == '__main__':
    for i in range(4):
        n_size = 1000
        t = timeit.Timer("test%d(%d)" % (i + 1, n_size), setup="from __main__ import test%d" % (i + 1))
        print("List generation %d took %f seconds" % (i + 1, t.timeit(n_size)))