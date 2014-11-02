__author__ = 'Darryl'
__date__ = '17-8-2014'


class AltQueue:
    def __init__(self):
        self._items = []

    def dequeue(self):
        return self._items.pop()

    def enqueue(self, item):
        self._items.insert(item, 0)

    def __len__(self):
        return len(self._items)