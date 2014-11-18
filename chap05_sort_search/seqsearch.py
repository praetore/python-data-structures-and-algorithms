__author__ = 'darryl'


def search(nums, elem, _idx=0):
    if _idx > len(nums) - 1:
        return False
    elif nums[_idx] == elem:
        return True
    else:
        return search(nums, elem, _idx + 1)


if __name__ == '__main__':
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    assert search(testlist, 32)
    assert False == search(testlist, 66)
    assert search(testlist, 0)