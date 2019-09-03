#!/usr/bin/python3

from pyrob.api import *

dirs = [[wall_is_above, move_up], [wall_is_on_the_right, move_right], [wall_is_beneath, move_down], [wall_is_on_the_left, move_left]]

@task
def task_8_21():
	initwalls = [dirs[i][0]() for i in range(0, 4)]
	for ind, initwall in enumerate(initwalls):
		if not initwall:
			continue
		while not dirs[(ind + 2) % 4][0]():
			dirs[(ind + 2) % 4][1]()


if __name__ == '__main__':
    run_tasks()
