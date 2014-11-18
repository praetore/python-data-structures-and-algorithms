from euler_utils import timeit

__author__ = 'darryl'


def calc_loop(n):
    total = n
    for i in reversed(range(1, n)):
        total *= i
    return total


def calc_recur(n, _total=1):
    if n == 1:
        return _total
    else:
        _total *= n
        return calc_recur(n - 1, _total)


@timeit
def test_loop():
    print(calc_loop(10))


@timeit
def test_recur():
    print(calc_recur(10))


if __name__ == '__main__':
    test_loop()
    test_recur()