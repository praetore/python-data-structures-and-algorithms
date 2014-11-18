__author__ = 'darryl'


def search(nums, elem):
    idx = int(len(nums) - 1 / 2)
    if nums[idx] == elem:
        return True
    elif not idx:
        return False
    elif nums[idx] > elem:
        return search(nums[:idx], elem)
    elif nums[idx] < elem:
        return search(nums[idx:], elem)

if __name__ == '__main__':
    nums = [i for i in range(1, 100, 2)]
    print(search(nums, 3))
    print(search(nums, 4))