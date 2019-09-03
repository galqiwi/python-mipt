#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    def fill_smart():
        flag = False
        if not wall_is_above():
            move_up()
            fill_cell()
            move_down()
            flag = True
        if not wall_is_beneath():
            move_down()
            fill_cell()
            move_up()
            flag = True
        if not flag:
            fill_cell()

    fill_smart()
    while not wall_is_on_the_right():
        move_right()
        fill_smart()


if __name__ == '__main__':
    run_tasks()
