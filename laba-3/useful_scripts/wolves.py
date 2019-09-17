# coding: utf-8

"""
brushColor("blue")
polygon([(100,100), (200,50), 
         (300,100), (100,100)])
penColor("white")
brushColor("green")
circle(200, 150, 50)
"""


from graph import *
import shapes
import json

width = 900
height = 718

windowSize(width, height)
canvasSize(width, height)
penColor(255,0,0)
penSize(0)
brushColor(0, 0, 0)
image(-1, -1, '019.jpg')


brushColor(100, 100, 100)
#rectangle(0, 0, width, height)

file = open('shapes.json', 'r')
last_shapes = json.loads(file.read())

for i in last_shapes:
	brushColor(i['color'][0], i['color'][1], i['color'][2])
	penColor(i['color'][0], i['color'][1], i['color'][2])
	#penColor(0, 0, 0)
	polygon(i['points'])
	polyline(i['points'])

output = []
last_point = (0, 0)
def fn(event):
	global last_point
	global output

	output.append([event.x, event.y])
	if last_point != (0, 0):
		line(last_point[0], last_point[1], event.x, event.y)
	last_point = (event.x, event.y)

def fnc(event):
	close()

onMouseDown(fn, 1)
onMouseDown(fnc, 3)

colors = [int(x) for x in input().split(' ')]
penColor(colors[0], colors[1], colors[2])
penColor(255,0,0)

run()

last_shapes.append({'color': colors, 'points': output})
print(json.dumps(last_shapes))