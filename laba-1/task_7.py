#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    while not wall_is_beneath():
        move_down()
    counter = 0
    while wall_is_beneath():
        move_right()
        counter += 1
    move_down()
    for i in range(0, counter):
        move_left()


if __name__ == '__main__':
    run_tasks()
