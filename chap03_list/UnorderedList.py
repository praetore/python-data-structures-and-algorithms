from chap03_list.LinkedList import LinkedList
from chap03_list.Node import Node

__author__ = 'Darryl'
__date__ = '16-8-2014'


class UnorderedList(LinkedList):
    def add(self, item):
        item = Node(item)
        previous = self._head
        item.set_next(previous)
        self._head = item
        if not self._tail:
            self._tail = item
        elif self._tail == item:
            self._tail = previous
        self._length += 1

    def append(self, item):
        item = Node(item)
        if self._tail:
            self._tail.set_next(item)
        if not self._head:
            self._head = item
        self._tail = item
        self._length += 1

    def insert(self, index, item):
        current = self._head
        index = int(index)
        item = Node(item)
        previous = None
        count = 0
        if index > self._length:
            self._tail.set_next(item)
            self._tail = item
            self._length += 1
        elif index == 0:
            self._head = item
            item.set_next(current)
            self._length += 1
        else:
            while current:
                if count == index:
                    item.set_next(current)
                    if previous:
                        previous.set_next(item)
                    self._length += 1
                    if count == self._length:
                        self._tail.set_next(item)
                        self._tail = item
                previous = current
                current = current.get_next()
                count += 1
        if not self._head:
            self._head = item
        if not self._tail:
            self._tail = item

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/unorderedlist.txt')