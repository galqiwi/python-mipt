#!/usr/bin/python3

from pyrob.api import *

dirs = [
    [wall_is_above, move_up], [wall_is_on_the_right, move_right],
    [wall_is_beneath, move_down], [wall_is_on_the_left, move_left]
]


@task(delay=0.01)
def task_5_10():
    flag = 0
    while flag < 2:
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
        fill_cell()
        while not wall_is_on_the_left():
            move_left()
        if not wall_is_beneath():
            move_down()
        if wall_is_beneath():
            flag += 1


if __name__ == '__main__':
    run_tasks()
