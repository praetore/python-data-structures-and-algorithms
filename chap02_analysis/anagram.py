import timeit

__author__ = 'darryl'


def anagram_solution1(s1, s2):
    a_list = list(s2)
    pos1 = 0
    still_ok = True
    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(a_list) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 += 1
        if not found:
            still_ok = False
        pos1 += 1

    return still_ok


def anagram_solution2(s1, s2):
    a_list1 = list(s1)
    a_list2 = list(s2)
    a_list1.sort()
    a_list2.sort()
    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if a_list1[pos] == a_list2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches


def anagram_solution3(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j += 1
        else:
            still_ok = False

    return still_ok


def anagram_solution4(s1, s2):
    return set(s1) <= set(s2) and len(s1) == len(s2)

if __name__ == '__main__':
    for i in range(4):
        n_size = 1000
        t = timeit.Timer("anagram_solution%d('abcd','dcba')" % (i+1),
                         setup="from __main__ import anagram_solution%d" % (i+1))
        print("Solution %d took %f seconds, given a problem size of %d" % (i+1, t.timeit(number=n_size), n_size))