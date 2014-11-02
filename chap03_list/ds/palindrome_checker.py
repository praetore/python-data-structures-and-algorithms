from chap03_list.ds.Deque import Deque

__author__ = 'Darryl'
__date__ = '29-9-2014'


def pal_check(palin):
    dq = Deque()
    for char in palin.replace(' ', '').lower():
        dq.add_rear(char)
    count = 0
    while len(dq) > 1:
        front = dq.remove_front()
        rear = dq.remove_rear()
        if front != rear:
            return False
        count += 1
    return True


if __name__ == '__main__':
    print(pal_check('parterretrap') == True)
    print(pal_check('yolo') == False)
    print(pal_check('I prefer pi') == True)