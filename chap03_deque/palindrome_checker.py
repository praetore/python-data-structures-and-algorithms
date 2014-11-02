from chap03_deque.Deque import Deque

__author__ = 'Darryl'
__date__ = '16-8-2014'


def pal_check(palin):
    dq = Deque()
    for char in palin.replace(' ', '').lower():
        dq.add_rear(char)
    valid = ""
    while len(dq) > 1 and not valid:
        if dq.remove_front() != dq.remove_rear():
            valid = "not "
    print("This is %sa palidrome" % valid)


if __name__ == '__main__':
    pal_check('parterretrap')
    pal_check('yolo')
    pal_check('I prefer pi')