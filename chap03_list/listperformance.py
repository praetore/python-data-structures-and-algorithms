from timeit import Timer

__author__ = 'darryl'


if __name__ == '__main__':
    setup = ["""
class UnorderedList(list):
    def add(self, item):
        self.insert(0, item)

    def search(self, item):
        return item in self

    def size(self):
        return len(self)
""", 'from chap03_list.UnorderedList import UnorderedList']
    stmt = """
l = UnorderedList()
bam = [i for i in range(100)]
for i in bam:
    l.add(i)
    l.search(i)
    l.remove(i)
    l.append(i)
    l.pop()
    l.insert(i, i)
    l.index(i)
    l.pop(0)
"""
    for i in range(3):
        n_size = 5*10**(i+1)
        for s in setup:
            t = Timer(stmt, s)
            print('List %d took %f seconds' % (setup.index(s)+1, t.timeit(number=n_size)))