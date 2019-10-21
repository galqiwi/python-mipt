import graph as gr
import sys
import json
import os
import tty
import termios
from time import sleep

width = 1190
height = 950

gr.windowSize(width, height)
gr.canvasSize(width, height)

gr.brushColor(90, 90, 90)
gr.penColor(90, 90, 90)
gr.rectangle(0, 0, width, height)

scene = []
with open('anim.scene', 'r') as file:
    scene = json.loads(file.read())

polygons_screen = []
polygons = []
polygonTypeV = 'full'


def updatePolygons():
    global polygons_screen, polygonTypeV, polygons
    for polygon in polygons_screen:
        gr.deleteObject(polygon)

    for i in polygons:
        gr.brushColor(i['color'][0], i['color'][1], i['color'][2])
        gr.penColor(i['color'][0], i['color'][1], i['color'][2])
        if polygonTypeV == 'full':
            polygons_screen.append(gr.polygon(i['points']))
        else:
            polygons_screen.append(gr.polyline(i['points']))


tickId = 0


def drawLoop():
    SPEED = 100
    SIZE = 100
    global polygons_screen, tickId, polygons
    tickId += 1
    localTime = (tickId * 1000) / 30

    x0 = width - width / 2 * 0.4
    y0 = height - height / 2 * 0.4
    xk = 0.4
    yk = 0.4

    def shrinkPoint(v, x0, y0, xk, yk):
        return [(v[0] - x0) * xk + x0, (v[1] - y0) * yk + y0]

    def shrinkPolygon(polygon, x0, y0, xk, yk):
        return {
            'color': polygon['color'],
            'points': [
                shrinkPoint(
                    v,
                    x0,
                    y0,
                    xk,
                    yk) for v in polygon['points']]}

    polygons = []
    for i in range(0, 3):
        shrink = SIZE ** (-(-tickId % SPEED + (i - 1) * SPEED) / SPEED)
        polygons += [shrinkPolygon(polygon,
                                   width / 2,
                                   height / 3,
                                   shrink,
                                   shrink) for polygon in scene[0]['polygons']]

    updatePolygons()


gr.onTimer(drawLoop, 1000 // 30)

gr.run()
