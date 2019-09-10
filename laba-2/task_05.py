import turtle
import math

turtle.shape('turtle')
turtle.penup()

INIT_SQUARE_HALFSIDE = 10
N = 10

def square(x):
	turtle.pendown()
	for i in range(0, 4):
		turtle.forward(x)
		turtle.left(90)
	turtle.penup()

for i in range(0, N):
	turtle.right(90)
	turtle.forward(INIT_SQUARE_HALFSIDE)
	turtle.right(90)
	turtle.forward(INIT_SQUARE_HALFSIDE)
	turtle.right(180)
	square((i + 1) * INIT_SQUARE_HALFSIDE * 2)