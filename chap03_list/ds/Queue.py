from chap03_list.UnorderedList import UnorderedList

__author__ = 'darryl'


class Queue:
    def __init__(self):
        self._items = UnorderedList()

    def dequeue(self):
        return self._items.pop()

    def enqueue(self, item):
        self._items.add(item)

    def __len__(self):
        return self._items.size()

    def __repr__(self, *args, **kwargs):
        return str(self._items)


if __name__ == '__main__':
    import doctest
    doctest.testfile('../tests/queue.txt')
