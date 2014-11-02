import random
from chap03_list.ds.Queue import Queue

__author__ = 'Darryl'
__date__ = '14-8-2014'


def hot_potato(names, count):
    q = Queue()
    for i in names:
        q.enqueue(i)

    while len(q) > 1:
        num = random.randint(0, count)
        for i in range(num+1):
            grab = q.dequeue()
            q.enqueue(grab)

        print("Bye %s!" % q.dequeue())

    print("%s gets the hot potato!" % q.dequeue())


if __name__ == '__main__':
    with open('names.txt') as f:
        peeps = f.readlines()
    COUNT = 7
    random.shuffle(peeps)
    hot_potato(peeps, COUNT)