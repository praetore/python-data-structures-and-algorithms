from euler_utils import timeit

__author__ = 'darryl'


def search_recursive(nums, elem, _idx=0):
    if _idx > len(nums) - 1:
        return False
    elif nums[_idx] == elem:
        return True
    return search_recursive(nums, elem, _idx + 1)


def search_loop(nums, elem):
    for i in nums:
        if i == elem:
            return True
    return False


@timeit
def test_recursive():
    assert search_recursive(nums, 551)
    assert False == search_recursive(nums, 660)


@timeit
def test_loop():
    assert search_loop(nums, 551)
    assert False == search_loop(nums, 660)


if __name__ == '__main__':
    nums = [i for i in range(1, 1000, 2)]
    test_recursive()
    test_loop()