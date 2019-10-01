#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    for i in range(0, 13):
        move_down()
        for k in range(0, i + 1):
            move_right()
            fill_cell()

        for k in range(0, i + 1):
            move_left()
    move_down()
    move_right()


if __name__ == '__main__':
    run_tasks()
