__author__ = 'darryl'

import unittest


def reverse(s):
    if len(removeWhite(s)):
        s_start = s[len(s) - 1]
        s_rev = reverse(s[:-1])
        s = s_start + s_rev
    return ''.join(s)


def isPal(s):
    return s == reverse(s)


def removeWhite(s):
    is_valid = lambda x: x in [chr(i) for i in range(97, 123)]
    s = [i.lower() for i in s if is_valid(i.lower())]
    return "".join(s)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(isPal(removeWhite("x")), True)
        self.assertEqual(isPal(removeWhite("radar")), True)
        self.assertEqual(isPal(removeWhite("hello")), False)
        self.assertEqual(isPal(removeWhite("")), True)
        self.assertEqual(isPal(removeWhite("hannah")), True)
        self.assertEqual(isPal(removeWhite("madam i'm adam")), True)


if __name__ == '__main__':
    unittest.main()
