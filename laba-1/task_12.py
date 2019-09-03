#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    def fill_smart():
        if ((not wall_is_above()) and (wall_is_beneath())):
            fill_cell()
    fill_smart()
    while not wall_is_on_the_right():
        move_right()
        fill_smart()


if __name__ == '__main__':
    run_tasks()
