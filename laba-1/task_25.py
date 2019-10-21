#!/usr/bin/python3

from pyrob.api import *


dirs = [
    [wall_is_above, move_up], [wall_is_on_the_right, move_right],
    [wall_is_beneath, move_down], [wall_is_on_the_left, move_left]
]


@task(delay=0.01)
def task_2_2():
    move_right(1)
    move_down(2)

    def flower():
        fill_cell()
        for i in range(0, 4):
            dirs[i][1]()
            fill_cell()
            dirs[(i + 2) % 4][1]()

    flower()
    for k in range(0, 4):
        move_right(4)
        flower()
    move_up()
    move_left()


if __name__ == '__main__':
    run_tasks()
