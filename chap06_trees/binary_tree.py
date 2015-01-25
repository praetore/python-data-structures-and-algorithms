import random
import unittest

__author__ = 'darryl'


class BinaryNode:
    def __init__(self, value, right=None, left=None):
        self.right = right
        self.left = left
        self.value = value

    def add(self, value):
        if value > self.value:
            if self.right:
                self.right.add(value)
            else:
                self.right = BinaryNode(value)
        else:
            if self.left:
                self.left.add(value)
            else:
                self.left = BinaryNode(value)

    def remove(self):
        if self.right is self.left is None:
            return None
        if self.left is None:
            return self.right
        if self.right is None:
            return self.left

        child = self.left
        grandchild = self.right
        if grandchild:
            while grandchild.right:
                child = grandchild
                grandchild = child.right
            self.value = grandchild.value
            child.right = grandchild.left
        else:
            self.left = child.left
            self.value = child.value

        return self


class BinaryTree:
    def __init__(self, head=None):
        self.head = head

    def __contains__(self, item):
        node = self.head
        while node:
            if item == node.value:
                return True
            elif item > node.value:
                node = node.right
            else:
                node = node.left
        return False

    def __iter__(self):
        n = self.min()
        if n is None:
            raise StopIteration
        while n <= self.max():
            if n in self or n == self.max() or n == self.min():
                yield n
            n += 1

    def max(self):
        node = self.head
        if node:
            if node.right:
                while node.right:
                    node = node.right
            return node.value
        else:
            return None

    def min(self):
        node = self.head
        if node:
            if node.left:
                while node.left:
                    node = node.left
            return node.value
        else:
            return None

    def insert(self, value):
        if self.head is None:
            self.head = BinaryNode(value)
        else:
            self.head.add(value)

    def remove(self, item):
        if self.head and item in self:
            self.head = self.remove_from_parent(self.head, item)

    def remove_from_parent(self, head, item):
        if head is None:
            return None

        if item == head.value:
            return head.remove()
        elif item < head.value:
            head.left = self.remove_from_parent(head.left, item)
        else:
            head.right = self.remove_from_parent(head.right, item)

        return head


class BinaryTreeTest(unittest.TestCase):
    def testInsert(self):
        bt = BinaryTree()
        for i in range(20, 100):
            bt.insert(i)
        expected = [i for i in range(20, 100)]
        found = [i for i in bt]
        self.assertEqual(found, expected)
        self.assertFalse(19 in bt)
        self.assertFalse(101 in bt)

    def testRemove(self):
        bt = BinaryTree()
        for i in range(100):
            bt.insert(i)
        r = [i for i in range(100)]
        random.shuffle(r)
        for i in r:
            bt.remove(i)

        found = [i for i in bt]
        expected = []
        self.assertEqual(found, expected)
