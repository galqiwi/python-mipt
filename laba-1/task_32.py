#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():

    count = 0

    def fill_smart():
        count_l = 0
        if wall_is_above():
            if cell_is_filled():
                count_l += 1
            else:
                fill_cell()
        else:
            while not wall_is_above():
                move_up()
                if cell_is_filled():
                    count_l += 1
                else:
                    fill_cell()
            while not wall_is_beneath():
                move_down()
        return count_l

    count += fill_smart()
    flag = True
    while flag:
        move_right()
        flag = not wall_is_on_the_right()
        if flag:
            count += fill_smart()

    mov('ax', count)
    #print(count)



if __name__ == '__main__':
    run_tasks()
