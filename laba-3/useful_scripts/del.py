import json



file = open('shapes.json', 'r')
last_shapes = json.loads(file.read())
last_shapes = last_shapes[:-1]
print(json.dumps(last_shapes))