from chap03_list.Node import Node

__author__ = 'darryl'


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def size(self):
        return self._length

    def is_empty(self):
        return self._head is None

    def index(self, item):
        item = Node(item)
        current = self._head
        count = 0
        while current:
            if item.get_data() == current.get_data():
                return count
            current = current.get_next()
            count += 1
        return None

    def remove(self, item):
        item = Node(item)
        current = self._head
        previous = None
        while current:
            if current.get_data() == item.get_data():
                if current.get_next():
                    if previous:
                        previous.set_next(current.get_next())
                    else:
                        self._head = current.get_next()
                else:
                    if previous:
                        self._tail = previous
                        previous.set_next(None)
                    else:
                        self._head = None
                self._length -= 1
            previous = current
            current = current.get_next()

    def search(self, item):
        item = Node(item)
        current = self._head
        while current:
            if current.get_data() == item.get_data():
                return True
            current = current.get_next()
        return False

    def pop(self, position=None):
        current = self._head
        previous = None
        count = 0
        if position:
            if position == 0:
                self._head = self._head.get_next()
            else:
                while not position == count:
                    count += 1
                previous.set_next(current.get_next())
            self._length -= 1
            return current.get_data()
        else:
            item = self._tail
            if previous:
                previous.set_next(None)
                self._tail = previous
            elif not previous:
                self._head = None
            self._length -= 1
            return item.get_data()

    def last(self):
        return self._tail.get_data()

    def __str__(self):
        current = self._head
        string = '[' + ''
        while current:
            if current != self._tail:
                string += current.get_data() + ', '
            else:
                string += current.get_data() + ''
            current = current.get_next()
        return string + ']'