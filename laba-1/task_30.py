#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    w = 1
    while not wall_is_on_the_right():
        w += 1
        move_right()
    for i in range(0, w - 1):
        move_left()

    for y in range(0, w):
        if y != 0 and y != w - 1:
            fill_cell()

        for x_ in range(0, w - 1):
            move_right()
            x = x_ + 1
            if x != y and x + y != w - 1:
                fill_cell()
        for x_ in range(0, w - 1):
            move_left()
        if y != w - 1:
            move_down()


if __name__ == '__main__':
    run_tasks()
