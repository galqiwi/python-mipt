#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_7_5():
	i = 0
	move_right()
	while True:
		i += 1
		if not wall_is_on_the_right():
			fill_cell()
		if not wall_is_on_the_right():
			for k in range(0, i):
				if wall_is_on_the_right():
					return
				move_right()



if __name__ == '__main__':
    run_tasks()
