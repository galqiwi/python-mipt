import turtle
import math
from time import sleep

turtle.shape('turtle')

def star(N):
    turtle.left(180 / N)

    for i in range(0, N):
        turtle.forward(100)
        turtle.left(180 - 180 / N)

star(5)