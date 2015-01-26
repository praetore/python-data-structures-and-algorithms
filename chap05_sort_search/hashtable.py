import unittest

__author__ = 'darryl'


class HashTable:
    def __init__(self):
        self.table = {}
        for i in range(11):
            self.table[i] = None

    def insert(self, item):
        idx = item % len(self.table)
        self.table[idx] = item

    def __contains__(self, item):
        idx = item % len(self.table)
        return self.table[idx] == item

    def __len__(self):
        return len([i for i in self.table.values() if i is not None])


class HashTableTest(unittest.TestCase):
    def testInsert(self):
        ht = HashTable()
        nums = [54, 26, 93, 17, 77, 31]
        for i in nums:
            ht.insert(i)
            self.assertTrue(i in ht)
        self.assertEqual(len(nums), len(ht))