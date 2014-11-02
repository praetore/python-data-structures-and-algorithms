from chap03_list.UnorderedList import UnorderedList

__author__ = 'Darryl'
__date__ = '16-8-2014'


class Deque:
    def __init__(self):
        self._items = UnorderedList()

    def add_front(self, item):
        self._items.insert(0, item)

    def add_rear(self, item):
        self._items.append(item)

    def remove_front(self):
        return self._items.pop(0)

    def remove_rear(self):
        return self._items.pop()

    def __len__(self):
        return self._items.size()

    def __str__(self, *args, **kwargs):
        return str(self._items)