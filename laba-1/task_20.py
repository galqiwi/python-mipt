#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
	for k in range(0, 12):
		for i in range(0, 27):
			move_right()
			fill_cell()
		move_down()
		for i in range(0, 27):
			move_left()
	move_right()


if __name__ == '__main__':
    run_tasks()
