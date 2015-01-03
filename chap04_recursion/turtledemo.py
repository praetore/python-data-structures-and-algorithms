import turtle

__author__ = 'darryl'


def draw_spiral(turtle, line_len):
    if line_len > 0:
        turtle.forward(line_len)
        turtle.right(90)
        draw_spiral(turtle, line_len-5)

if __name__ == '__main__':
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    draw_spiral(myTurtle, 100)
    myWin.exitonclick()
