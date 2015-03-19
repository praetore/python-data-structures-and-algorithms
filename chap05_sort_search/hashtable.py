import unittest

__author__ = 'darryl'


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.count = 0

    def put(self, item, key):
        idx = key % self.size
        if not self.slots[idx]:
            self.slots[idx] = key
            self.data[idx] = item
        else:
            # Replace
            if self.slots[idx] == key:
                self.data[idx] = item
            else:
                while self.slots[idx] and self.slots[idx] != key:
                    idx = (idx + 1) % self.size

                if not self.slots[idx]:
                    self.slots[idx] = key
                    self.data[idx] = item
                else:
                    # Replace
                    self.data[idx] = item
        self.count += 1

    def __len__(self):
        return self.count

    def get(self, key):
        idx = key % self.size
        start = idx
        while self.slots[idx]:
            if self.slots[idx] == key:
                return self.data[idx]
            else:
                idx = (key + 1) % self.size
                if idx == start:
                    return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(value, key)


class HashTableTest(unittest.TestCase):
    def testInsert(self):
        ht = HashTable()
        ht[54] = "cat"
        ht[26] = "dog"
        ht[93] = "lion"
        ht[17] = "tiger"
        ht[77] = "bird"
        ht[31] = "cow"
        ht[44] = "goat"
        ht[55] = "pig"
        ht[20] = "chicken"
        found = len(ht)
        expected = 9
        self.assertEqual(found, expected)