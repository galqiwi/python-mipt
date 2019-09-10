import turtle
import math
from time import sleep

turtle.shape('turtle')

FACE_CENTER = (50, 0)
FACE_RADIUS = 150
FACE_WIDTH = 1
FACE_COLOR = 'yellow'

RIGHT_EYE_CENTER = (50, 60) # left eye is symmetrical
RIGHT_EYE_RADIUS = 30
RIGHT_EYE_WIDTH = 1
RIGHT_EYE_COLOR = 'blue'

NOSE_HEIGHTS = [10, 30]
NOSE_WIDTH = 20
NOSE_COLOR = 'black'

SMILE_HEIGHT = -30
SMILE_RADIUS = 100
SMILE_WIDTH = 30
SMILE_COLOR = 'red'

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

circle_abs(FACE_CENTER[0], FACE_CENTER[1], FACE_RADIUS, color_fill = FACE_COLOR, to_fill = True, width = FACE_WIDTH)
circle_abs(FACE_CENTER[0] + RIGHT_EYE_CENTER[0], RIGHT_EYE_CENTER[1], RIGHT_EYE_RADIUS, color_fill = RIGHT_EYE_COLOR, to_fill = True, width = RIGHT_EYE_WIDTH)
circle_abs(FACE_CENTER[0] - RIGHT_EYE_CENTER[0], RIGHT_EYE_CENTER[1], RIGHT_EYE_RADIUS, color_fill = RIGHT_EYE_COLOR, to_fill = True, width = RIGHT_EYE_WIDTH)

line(FACE_CENTER[0], NOSE_HEIGHTS[0], FACE_CENTER[0], NOSE_HEIGHTS[1], width = NOSE_WIDTH, color = NOSE_COLOR)

turtle.penup()
turtle.goto(FACE_CENTER[0] + SMILE_RADIUS, SMILE_HEIGHT)
turtle.right(90)
circle(R = SMILE_RADIUS, left = False, half = True, color_board=SMILE_COLOR, width = SMILE_WIDTH)

sleep(1000)
