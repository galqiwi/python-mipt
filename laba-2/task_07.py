import turtle
import math

turtle.shape('turtle')

N = 100
SPEED = 0.1
ANGLE = 10

for i in range(0, N):
	turtle.forward(SPEED * i)
	turtle.right(ANGLE)