__author__ = 'Darryl'
__date__ = '16-8-2014'


class List:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.insert(0, item)

    def remove(self, item):
        del self._items[item.index]

    def search(self, item):
        for i in self._items:
            if i == item:
                return True
        return False

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def append(self, item):
        self._items.append(item)

    def insert(self, item, index):
        self._items.insert(index, item)

    def pop(self, index=-1):
        item = self._items[index]
        del self._items[index]
        return item