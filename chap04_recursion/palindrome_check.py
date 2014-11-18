__author__ = 'darryl'


def reverse(s):
    if len(s):
        s_start = s[len(s)-1]
        s_rev = reverse(s[:-1])
        s = s_start + s_rev
    return ''.join(s)


def test_equal(a, b):
    print(a == b, a)


if __name__ == '__main__':
    test_equal(reverse("hello"), "olleh")
    test_equal(reverse("l"), "l")
    test_equal(reverse("follow"), "wollof")
    test_equal(reverse(""), "")
    test_equal(reverse("ghhs"), "shg")