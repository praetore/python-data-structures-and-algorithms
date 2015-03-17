from turtle import Turtle
from turtle import Screen

__author__ = 'darryl'


def tree(branch_len, t, w=12, c=2):
    if branch_len > 5:
        t.width(w-c)
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15, t, w=w-c)
        t.left(40)
        tree(branch_len - 15, t, w=w-c)
        t.right(20)
        t.backward(branch_len)


def main():
    t = Turtle()
    my_win = Screen()
    t.width(10)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    my_win.exitonclick()

if __name__ == '__main__':
    main()