import turtle
import math
turtle.shape('turtle')

N = 3
LEN = 50

for i in range(0, N):
    turtle.forward(LEN)
    turtle.stamp()
    turtle.backward(LEN)
    turtle.right(360. / N)
