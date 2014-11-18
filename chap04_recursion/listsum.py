__author__ = 'darryl'


def listsum(numslist, _total=0):
    if len(numslist) > 1:
        _total += numslist[-1]
        numslist = numslist[:-1]
        return listsum(numslist, _total)
    else:
        _total += numslist[-1]
        return _total


if __name__ == '__main__':
    print(listsum([10, 10, 10]))
