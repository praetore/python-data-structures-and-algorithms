__author__ = 'Darryl'
__date__ = '14-8-2014'


class Queue:
    def __init__(self):
        self._items = []

    def dequeue(self):
        return self._items.pop(0)

    def enqueue(self, item):
        self._items.append(item)

    def __len__(self):
        return len(self._items)