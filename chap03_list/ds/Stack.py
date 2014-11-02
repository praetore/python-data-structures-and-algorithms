from chap03_list.UnorderedList import UnorderedList

__author__ = 'darryl'


class Stack:
    def __init__(self):
        self._items = UnorderedList()

    def is_empty(self):
        return self._items.is_empty()

    def size(self):
        return self._items.size()

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items.append(self._items.pop())

if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())