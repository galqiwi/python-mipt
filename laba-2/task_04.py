import turtle
import math

turtle.shape('turtle')

N = 100

for i in range(0, N):
	turtle.forward(2. * math.pi * 50. / N)
	turtle.left(360. / N)