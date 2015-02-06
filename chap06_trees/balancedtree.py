import unittest
from chap06_trees.binary_tree import BinaryTree

__author__ = 'darryl'


class BalancedTree:
    def __init__(self):
        self.bt = BinaryTree()

    def insert_list(self, nums):
        idx = len(nums) // 2
        try:
            self.bt.insert(nums[idx])
            self.insert_list(nums[:idx])
            self.insert_list(nums[idx+1:])
        except IndexError:
            pass

    def __contains__(self, item):
        return item in self.bt

    def __len__(self):
        return len(self.bt)

    def __iter__(self):
        gen = self.bt.__iter__()
        while True:
            yield next(gen)

    def mid(self):
        return self.bt.mid()

    def max(self):
        return self.bt.max()

    def min(self):
        return self.bt.min()

    def root(self):
        return self.bt.head.value


class TestBalancedTree(unittest.TestCase):
    def testInsertion(self):
        bt = BalancedTree()
        bt.insert_list(list(i for i in range(200)))
        self.assertEqual(len(bt), 200, len(bt))
        self.assertEqual(bt.min(), 0, bt.min())
        self.assertEqual(bt.mid(), 99, bt.mid())
        self.assertEqual(bt.root(), 100, bt.root())
        self.assertEqual(bt.max(), 199, bt.max())