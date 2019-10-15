from tkinter import *
from random import randrange as rnd, choice
import random
import time
import math
import itertools

root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

def randomColor():
    out = '#'
    for i in range(0, 6):
        out += choice([str(x) for x in range(0, 10)] + ['a', 'b', 'c', 'd', 'e', 'f'])
    return out
balls = []

def random_v(wall_id = -1):
    av = 10
    angle = 2 * math.pi * random.random()
    vx = av * math.cos(angle)
    vy = av * math.sin(angle)

    if wall_id == 0:
        vy = +abs(vy)
    if wall_id == 1:
        vx = -abs(vx)
    if wall_id == 2:
        vy = -abs(vy)
    if wall_id == 3:
        vx = +abs(vx)

    return [av * 2 * (random.random() - 0.5), av * 2 * (random.random() - 0.5)]



def new_ball(type_ = 'old'):
    global balls
    canv.delete(ALL)
    x = rnd(100, 700)
    y = rnd(100, 500)
    r = rnd(30, 50)
    balls.append({'x': [x, y], 'v': random_v(), 'r': r, 'color': randomColor(), 'color2': randomColor(), 'type': type_})

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    def __truediv__(self, x):
        return Vector2(self.x / x, self.y / x)
    def __mul__(self, x):
        return Vector2(self.x * x, self.y * x)
    def abs2(self):
        return self.x * self.x + self.y * self.y
    def abs(self):
        return math.sqrt(self.abs2())
    def norm(self):
        return self / self.abs()

def dotmul(a, b):
    return a.x * b.x + a.y * b.y

def update():
    canv.delete(ALL)
    for ball in balls:
        x = ball['x'][0]
        y = ball['x'][1]
        r = ball['r']

        if x < r:
            ball['v'] = random_v(3)
        if x > 800 - r:
            ball['v'] = random_v(1)
        if y < r:
            ball['v'] = random_v(0)
        if y > 600 - r:
            ball['v'] = random_v(2)

        if ball['type'] == 'old':
            canv.create_oval(x-r,y-r,x+r,y+r,fill = ball['color'], width=0)
        else:
            canv.create_oval(x-r,y-r,x+r,y+r,fill = ball['color'], width=0)
            canv.create_oval(x-r / 2,y-r / 2,x+r / 2,y+r / 2,fill = ball['color2'], width=0)

        ball['x'][0] += ball['v'][0] * 0.1
        ball['x'][1] += ball['v'][1] * 0.1

    for ball in balls:
        for ball2 in balls:
            diff = Vector2(ball2['x'][0], ball2['x'][1]) - Vector2(ball['x'][0], ball['x'][1])
            if diff.abs2() >= (ball['r'] + ball2['r']) ** 2 or diff.abs2() == 0:
                continue
            penetrarion = diff.abs() - (ball['r'] + ball2['r'])
            norm = diff.norm()
            ball['x'][0] += (norm * penetrarion / 2).x
            ball['x'][1] += (norm * penetrarion / 2).y
            ball2['x'][0] -= (norm * penetrarion / 2).x
            ball2['x'][1] -= (norm * penetrarion / 2).y

            v0 = Vector2(ball['v'][0], ball['v'][1])
            v1 = Vector2(ball2['v'][0], ball2['v'][1])
            v0_n = norm * dotmul(v0, norm)
            v1_n = norm * dotmul(v1, norm)
            v0 = v0 - v0_n + v1_n;
            v1 = v1 - v1_n + v0_n;
            ball['v'][0] = v0.x
            ball['v'][1] = v0.y
            ball2['v'][0] = v1.x
            ball2['v'][1] = v1.y
    root.after(10, update)


score = 0
def click(event):
    global score, balls
    success_all = [False, False]
    for ball in balls:
        x = ball['x'][0]
        y = ball['x'][1]
        r = ball['r']
        success = (event.x - x) ** 2 + (event.y - y) ** 2 < r ** 2
        if ball['type'] == 'old':
            success_all[0] = success_all[0] or success
        else:
            success_all[1] = success_all[1] or success

    if success_all[0]:
        score += 5
    elif success_all[1]:
        score += 10
    else:
        score -= 50
    print('score', score)


for i in range(0, 10):
    new_ball(random.choice(['old', 'new']))

def key(event):
    global score
    if event.char != 'q':
        return
    scoreboard = []
    with open('scores.txt', 'r') as file:
        scoreboard = [x.split(' ')[::-1] for x in file.read().split('\n')][:-1]
        file.close()
    scoreboard = [[int(x[0]), x[1]] for x in scoreboard]
    name = input('your name: ')
    scoreboard.append([score, name])

    scoreboard = sorted(scoreboard)
    scoreboard.reverse()
    with open('scores.txt', 'w') as file:
        for score in scoreboard:
            file.write(str(score[1]) + ' ' + str(score[0]) + '\n')
        file.close()
    for score in scoreboard[:10]:
        print(score[1], score[0])
    exit(0)

update()
canv.bind('<Button-1>', click)
canv.bind("<Key>", key)
canv.focus_set()
mainloop()