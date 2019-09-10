import turtle
import math

turtle.shape('turtle')

N = 100
INIT_SPIRAL_SIZE = 10

for i in range(0, N):
	turtle.forward(i * INIT_SPIRAL_SIZE)
	turtle.left(90)
	turtle.forward(i * v)
	turtle.left(90)