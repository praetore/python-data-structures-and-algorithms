import turtle

__author__ = 'darryl'


def draw_spiral(t, line_len):
    if line_len > 0:
        t.forward(line_len)
        t.right(90)
        draw_spiral(t, line_len-5)

if __name__ == '__main__':
    t = turtle.Turtle()
    win = turtle.Screen()
    draw_spiral(t, 100)
    win.exitonclick()
