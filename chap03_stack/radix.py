from chap03_stack.Stack import Stack

__author__ = 'darryl'


def create_bins(num):
    bins = {'main': create_main_bin(num)}
    [bins.update({str(i): Stack()}) for i in range(10)]
    return bins


def create_main_bin(num):
    s = Stack()
    num_array = list(str(num))
    for i in num_array:
        factor = num_array.index(i)
        main_digit = int(i) * (10 ** factor)
        s.push(main_digit)
    return s


def place_in_numbered_bin(bins):
    next_num = bins['main'].pop()
    bins[str(next_num)[0]].push(next_num)


def check_bins(bins):
    print('-- Listing bin contents --')
    for k, v in bins.items():
        print('%s has %d items' % (k, v.size()))


if __name__ == '__main__':
    num = 456
    bins = create_bins(num)
    print('-- Bins initialized --')
    check_bins(bins)
    while bins['main'].size():
        place_in_numbered_bin(bins)
    print('-- Bins have been filled --')
    check_bins(bins)
    for k, v in bins.items():
        if k != 'main':
            while v.size():
                bins['main'].push(v.pop())
    print('-- Bin contents pushed to main again --')
    check_bins(bins)
    while bins['main'].size():
        print('Main contains a %d' % bins['main'].pop())