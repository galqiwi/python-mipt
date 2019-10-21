import turtle
import math

turtle.shape('turtle')
turtle.left(90)

N = 2
INIT_RADIUS = 30
RADIUS_INCREACE = 5


def circle(
        R=50,
        N=50,
        left=True,
        half=False,
        color_fill='white',
        color_board='black',
        to_fill=False,
        width=1):
    turtle.width(width)
    if to_fill:
        turtle.begin_fill()
    turtle.color(color_board)
    turtle.pendown()
    for i in range(0, N + 1):
        turtle.forward((1 if (i == 0 or i == N) else 2) *
                       math.pi * R / N / (2 if half else 1))
        if i != N:
            if left:
                turtle.left(360 / N / (2 if half else 1))
            else:
                turtle.right(360 / N / (2 if half else 1))

    if to_fill:
        turtle.color(color_fill)
        turtle.end_fill()


for i in range(0, N):
    circle(R=INIT_RADIUS + RADIUS_INCREACE * i)
    circle(R=INIT_RADIUS + RADIUS_INCREACE * i, left=False)
