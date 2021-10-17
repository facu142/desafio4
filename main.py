import math
import os
import pickle


class Point:
	def __init__(self, cx, cy, desc='p'):
		self.x = cx
		self.y = cy
		self.descripcion = desc


def to_string(point):
	r = str(point.descripcion) + '(' + str(point.x) + ', ' + str(point.y) + ')'
	return r


def distance_between(p1, p2):
	# calcular "delta y" y "delta x"
	dy = p2.y - p1.y
	dx = p2.x - p1.x

	# Distancia entre ellos... Pitágoras...
	return math.sqrt(pow(dx, 2) + pow(dy, 2))


puntos = []

archivo = open('puntos.df4', 'rb')
tam = os.path.getsize('puntos.df4')

while archivo.tell() < tam:
	puntos.append(pickle.load(archivo))

dmax = 0
dmin = distance_between(puntos[0], puntos[1])

n = len(puntos)

for i in range(0, n):
	for j in range(i+1 , n):
		d = distance_between(puntos[i], puntos[j])
		if d < dmin:
			dmin = d
		if d > dmax:
			dmax = d

print('Dmin =', dmin)
print('DMAX =', dmax)
