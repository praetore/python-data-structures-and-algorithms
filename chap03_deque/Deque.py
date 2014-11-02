__author__ = 'Darryl'
__date__ = '16-8-2014'


class Deque:
    def __init__(self):
        self._items = []

    def add_front(self, item):
        self._items.insert(0, item)

    def add_rear(self, item):
        self._items.append(item)

    def remove_front(self):
        return self._items.pop(0)

    def remove_rear(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)