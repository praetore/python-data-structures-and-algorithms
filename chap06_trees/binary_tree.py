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

    def insert(self, value):
        if self.head is None:
            self.head = BinaryNode(value)
        else:
            self.head.add(value)


class BinaryTreeTest(unittest.TestCase):
    def testInsert(self):
        bt = BinaryTree()
        for i in range(100):
            bt.insert(i)
        expected = [i for i in range(100)]
        found = [i for i in expected if i in bt]
        self.assertEqual(found, expected)