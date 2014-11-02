import random
from chap03_queue.Queue import Queue

__author__ = 'Darryl'
__date__ = '14-8-2014'


def hot_potato(names, count):
    q = Queue()
    for i in names:
        q.enqueue(names.pop())

    while len(q) > 1:
        num = random.randint(0, count)
        for i in range(num+1):
            q.enqueue(q.dequeue())

        print("Bye %s!" % q.dequeue())

    print("%s gets the hot potato!" % q.dequeue())


if __name__ == '__main__':
    COUNT = 7
    with open('names.txt', 'r') as f:
        peeps = f.readlines()
    random.shuffle(peeps)
    hot_potato(peeps, COUNT)