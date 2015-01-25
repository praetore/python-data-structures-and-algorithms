__author__ = 'darryl'


def convert_to_base(num, base):
    convertString = "0123456789ABCDEF"
    if num < base:
        return convertString[num]
    else:
        return convert_to_base(num // base, base) + convertString[num % base]


if __name__ == '__main__':
    print(convert_to_base(1453, 2))