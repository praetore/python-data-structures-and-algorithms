__author__ = 'darryl'


def reverse(s):
    is_valid = lambda x: x in [chr(i) for i in range(97, 123)]
    s = [i.lower() for i in s if is_valid(i.lower())]
    if len(s):
        s_start = s[len(s) - 1]
        s_rev = reverse(s[:-1])
        s = s_start + s_rev
    return ''.join(s)


if __name__ == '__main__':
    assert reverse("hello") == "olleh", reverse("hello")
    assert reverse("l") == "l", reverse("l")
    assert reverse("follow") == "wollof", reverse("follow")
    assert reverse("") == "", reverse("")
    assert reverse("ghhs") != "shg", reverse("ghhs")
    assert reverse("Go hang a salami; I’m a lasagna hog") == "gohangasalamiimalasagnahog", reverse(
        "Go hang a salami; I’m a lasagna hog")