#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
	for i in range(0, 2):
	    move_right()
	    move_right()
	    move_down()
	    if i == 0:
	    	move_down()
	    	fill_cell()



if __name__ == '__main__':
    run_tasks()
