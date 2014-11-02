import random

__author__ = 'Darryl'
__date__ = '16-8-2014'


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def get_waittime(self, current_time):
        return current_time - self.timestamp