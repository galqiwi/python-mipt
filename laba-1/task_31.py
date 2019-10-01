#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    while True:
        done = True
        while not wall_is_on_the_left():
            move_left()

        bflag = True
        while (not wall_is_on_the_right()) and bflag:
            move_right()
            if not wall_is_beneath():
                move_down()
                done = False
                bflag = False
        if done:
            while not wall_is_on_the_left():
                move_left()
            return


if __name__ == '__main__':
    run_tasks()
