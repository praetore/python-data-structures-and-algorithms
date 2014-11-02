from chap03_list.LinkedList import LinkedList
from chap03_list.Node import Node

__author__ = 'darryl'


class OrderedList(LinkedList):
    def add(self, item):
        item = Node(item)
        current = self._head
        previous = None
        if not current:
            self._head = item
            self._tail = item
        elif item.get_data() < current.get_data():
            item.set_next(current)
            self._head = item
        else:
            while current:
                if current.get_data() > item.get_data():
                    current = previous
                    break
                previous = current
                current = current.get_next()
            if current and current.get_next():
                item.set_next(current.get_next())
                current.set_next(item)
            else:
                previous.set_next(item)
                self._tail = item
        self._length += 1

if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/orderedlist.txt')