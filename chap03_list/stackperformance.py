from timeit import Timer

__author__ = 'darryl'

if __name__ == '__main__':
    stmt = """
numlist = [i for i in range(100)]
s = Stack()
for i in numlist:
    s.push(i)
    s.size()
    s.peek()
    s.pop()
    s.is_empty()
"""
    setup = ['from chap03_stack.Stack import Stack', 'from chap03_list.ds.Stack import Stack']
    for i in range(3):
        n_size = 5*10**(i+1)
        for s in setup:
            print('List %d took %f seconds' % (setup.index(s)+1, Timer(stmt, s).timeit(n_size)))