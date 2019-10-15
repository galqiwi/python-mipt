import turtle
import math

turtle.shape('turtle')

N = 100
RADIUS = 50

for i in range(0, N):
    turtle.forward(2. * math.pi * RADIUS / N)
    turtle.left(360. / N)
