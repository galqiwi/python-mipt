import turtle
import math

turtle.shape('turtle')

N = 15
INIT_RADIUS = 30
RADIUS_INCREASE = 20
VERSION = False #True is for constant radius increase

radius = INIT_RADIUS
old_radius = 0
for i in range(0, N):
	turtle.penup()
	turtle.forward(radius - old_radius)
	turtle.pendown()
	nangles = 3 + i
	side = 2 * math.sin(math.pi / nangles) * radius
	angle = 360 / nangles
	turtle.left(90 + angle / 2)
	for k in range(0, nangles):
		turtle.forward(side)
		turtle.left(angle)
	turtle.right(90 + angle / 2)

	old_radius = radius
	if VERSION:
		radius = radius + RADIUS_INCREASE #math.cos(math.pi / (nangles + 1))
	else:
		radius /= math.cos(math.pi / (nangles + 1))
