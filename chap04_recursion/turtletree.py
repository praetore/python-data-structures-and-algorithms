from turtle import Turtle
from turtle import Screen
import random

__author__ = 'darryl'


def get_branch_len(branch_len):
    res = branch_len - random.randint(5, 15)
    return res if res > 0 else 5


def tree(branch_len, t, w=12, c=2):
    i = random.randint(15, 45)
    if branch_len > 5:
        t.width(w-c)
        t.forward(branch_len)
        t.right(i)
        tree(get_branch_len(branch_len), t, w=w-c if w > c else c)
        t.left(i*2)
        tree(get_branch_len(branch_len), t, w=w-c if w > c else c)
        t.right(i)
        tree(get_branch_len(branch_len), t, w=w-c if w > c else c)
        t.backward(branch_len)
    if branch_len < 15:
        t.width(4)
        t.color("green")
    else:
        t.color("brown")


def main():
    t = Turtle()
    my_win = Screen()
    t.width(12)
    t.speed(10)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(75, t)
    my_win.exitonclick()

if __name__ == '__main__':
    main()