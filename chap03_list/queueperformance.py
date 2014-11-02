from timeit import Timer

__author__ = 'darryl'

if __name__ == '__main__':
    stmt = """
numlist = [i for i in range(1000)]
s = Queue()
for i in numlist:
    s.enqueue(i)
    len(s)
    s.dequeue()
"""
    setup = ['from chap03_queue.Queue import Queue', 'from chap03_list.ds.Queue import Queue']
    for i in range(3):
        n_size = 5*10**(i+1)
        for s in setup:
            print('List %d took %f seconds' % (setup.index(s)+1, Timer(stmt, s).timeit(n_size)))