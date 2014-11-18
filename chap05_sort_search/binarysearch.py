from euler_utils import timeit

__author__ = 'darryl'


def search_recursive(nums, elem):
    idx = int(len(nums) - 1 / 2)
    if nums[idx] == elem:
        return True
    elif not idx:
        return False
    elif nums[idx] > elem:
        return search_recursive(nums[:idx], elem)
    elif nums[idx] < elem:
        return search_recursive(nums[idx:], elem)


def search_loop(nums, elem):
    for i in nums:
        idx = int(len(nums) - 1 / 2)
        if i == elem:
            return True
        elif nums[idx] > elem:
            nums = nums[:idx]
        elif nums[idx] < elem:
            nums = nums[idx:]
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