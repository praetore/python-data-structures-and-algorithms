import random
from chap03_queue.AltQueue import AltQueue
from chap03_queue.Printer import Printer
from chap03_queue.Queue import Queue
from chap03_queue.Task import Task

__author__ = 'Darryl'
__date__ = '16-8-2014'


def simulation(num_seconds, pages_per_minute, number_of_students, print_queue=Queue()):
    lab_printer = Printer(pages_per_minute)
    waiting_times = []

    for current_second in range(num_seconds):

        if new_print_task(number_of_students):
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (len(print_queue)):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.get_waittime(current_second))
            lab_printer.next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, len(print_queue)))


def new_print_task(n_students):
    num = random.randrange(1, 3600/n_students+1)
    if num == 3600/n_students:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Using standard queue")
    for i in range(10):
        simulation(3600, 10, 120)
    print("Using alternative queue")
    for i in range(10):
        simulation(3600, 10, 120, AltQueue())