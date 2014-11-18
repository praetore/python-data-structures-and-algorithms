__author__ = 'darryl'


def convert_to_base(num, base, _res=list()):
    if num < base:
        _res.insert(0, str(1))
        return "".join(_res)
    else:
        _res.append(str(round(num % base)))
        return convert_to_base(num / base, base, _res)

if __name__ == '__main__':
    print(convert_to_base(10, 2))