import turtle
import math
from time import sleep

turtle.shape('turtle')

def circle(R = 50, N = 50, left = True, half = False, color_fill = 'white', color_board = 'black', to_fill = False, width = 1):
	turtle.width(width)
	if to_fill:
		turtle.begin_fill()
	turtle.color(color_board)
	turtle.pendown()
	for i in range(0, N + 1):
		turtle.forward((1 if (i == 0 or i == N) else 2) * math.pi * R / N / (2 if half else 1))
		if i != N:
			if left:
				turtle.left(360 / N / (2 if half else 1))
			else:
				turtle.right(360 / N / (2 if half else 1))

	if to_fill:
		turtle.color(color_fill)
		turtle.end_fill()



def circle_abs(x, y, R = 50, *args, **argv):
	turtle.penup()
	turtle.goto(x, y - R)
	turtle.pendown()
	circle(R = R, *args, **argv)

def line(x0, y0, x1, y1, color = 'black', width = 1):
	turtle.width(width)
	turtle.penup()
	turtle.goto(x0, y0)
	turtle.pendown()
	turtle.color(color)
	turtle.goto(x1, y1)

circle_abs(0, 0, 150, color_fill = 'yellow', to_fill = True)
circle_abs(50, 60, 30, color_fill = 'blue', to_fill = True)
circle_abs(-50, 60, 30, color_fill = 'blue', to_fill = True)

line(0, 30, 0, 10, width = 10)

turtle.penup()
turtle.goto(40, -10)
turtle.right(90)
circle(R = 40, left = False, half = True, color_board='red', width = 20)

sleep(1000)
