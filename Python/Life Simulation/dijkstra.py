from random import randint
from math import inf

class Vertex:
	def __init__(self, num, sizeX, sizeY, value = inf):
		self.isChecked = False
		self.value = value
		self.num = num
		self.n = []
		for i in range(sizeX):
			temp = []
			for j in range(sizeY):
				temp.append(inf)
			self.n.append(temp)
		i = num // sizeY
		j = num % sizeY
		self.n[i][j] = 0
		if i - 1 >= 0:
			self.n[i - 1][j] = 1.0
		if i + 1 < sizeX:
			self.n[i + 1][j] = 1.0
		if j - 1 >= 0:
			self.n[i][j - 1] = 1.0
		if j + 1 < sizeY:
			self.n[i][j + 1] = 1.0
		if i - 1 >= 0 and j - 1 >= 0:
			self.n[i - 1][j - 1] = 1.41421
		if i - 1 >= 0 and j + 1 < sizeY:
			self.n[i - 1][j + 1] = 1.41421
		if i + 1 < sizeX and j - 1 >= 0:
			self.n[i + 1][j - 1] = 1.41421
		if i + 1 < sizeX and j + 1 < sizeY:
			self.n[i + 1][j + 1] = 1.41421

	def chgValue(self, value):
		self.value = value

	def checked(self):
		self.isChecked = True


def vertCalc(vert, num, sizeX, sizeY):
	global recCount
	i = num // sizeY
	j = num % sizeY
	if i - 1 >= 0:
		if vert[i][j].value + vert[i][j].n[i - 1][j] < vert[i - 1][j].value and vert[i - 1][j].isChecked == False:
			vert[i - 1][j].value = round(vert[i][j].value + vert[i][j].n[i - 1][j], 5)
	if i + 1 < sizeX:
		if vert[i][j].value + vert[i][j].n[i + 1][j] < vert[i + 1][j].value and vert[i + 1][j].isChecked == False:
			vert[i + 1][j].value = round(vert[i][j].value + vert[i][j].n[i + 1][j], 5)
	if j - 1 >= 0:
		if vert[i][j].value + vert[i][j].n[i][j - 1] < vert[i][j - 1].value and vert[i][j - 1].isChecked == False:
			vert[i][j - 1].value = round(vert[i][j].value + vert[i][j].n[i][j - 1], 5)
	if j + 1 < sizeY:
		if vert[i][j].value + vert[i][j].n[i][j + 1] < vert[i][j + 1].value and vert[i][j + 1].isChecked == False:
			vert[i][j + 1].value = round(vert[i][j].value + vert[i][j].n[i][j + 1], 5)
	if i - 1 >= 0 and j - 1 >= 0:
		if vert[i][j].value + vert[i][j].n[i - 1][j - 1] < vert[i - 1][j - 1].value and vert[i - 1][j - 1].isChecked == False:
			vert[i - 1][j - 1].value = round(vert[i][j].value + vert[i][j].n[i - 1][j - 1], 5)
	if i - 1 >= 0 and j + 1 < sizeY:
		if vert[i][j].value + vert[i][j].n[i - 1][j + 1] < vert[i - 1][j + 1].value and vert[i - 1][j + 1].isChecked == False:
			vert[i - 1][j + 1].value = round(vert[i][j].value + vert[i][j].n[i - 1][j + 1], 5)
	if i + 1 < sizeX and j - 1 >= 0:
		if vert[i][j].value + vert[i][j].n[i + 1][j - 1] < vert[i + 1][j - 1].value and vert[i + 1][j - 1].isChecked == False:
			vert[i + 1][j - 1].value = round(vert[i][j].value + vert[i][j].n[i + 1][j - 1], 5)
	if i + 1 < sizeX and j + 1 < sizeY:
		if vert[i][j].value + vert[i][j].n[i + 1][j + 1] < vert[i + 1][j + 1].value and vert[i + 1][j + 1].isChecked == False:
			vert[i + 1][j + 1].value = round(vert[i][j].value + vert[i][j].n[i + 1][j + 1], 5)
	vert[i][j].isChecked = True
	if i - 1 >= 0:
		if vert[i - 1][j].isChecked == False:
			vertCalc(vert, (i - 1) * sizeY + j, sizeX, sizeY)
	if i + 1 < sizeX:
		if vert[i + 1][j].isChecked == False:
			vertCalc(vert, (i + 1) * sizeY + j, sizeX, sizeY)
	if j - 1 >= 0:
		if vert[i][j - 1].isChecked == False:
			vertCalc(vert, i * sizeY + j - 1, sizeX, sizeY)
	if j + 1 < sizeY:
		if vert[i][j + 1].isChecked == False:
			vertCalc(vert, i * sizeY + j + 1, sizeX, sizeY)
	if i - 1 >= 0 and j - 1 >= 0:
		if vert[i - 1][j - 1].isChecked == False:
			vertCalc(vert, (i - 1) * sizeY + j - 1, sizeX, sizeY)
	if i - 1 >= 0 and j + 1 < sizeY:
		if vert[i - 1][j + 1].isChecked == False:
			vertCalc(vert, (i - 1) * sizeY + j + 1, sizeX, sizeY)
	if i + 1 < sizeX and j - 1 >= 0:
		if vert[i + 1][j - 1].isChecked == False:
			vertCalc(vert, (i + 1) * sizeY + j - 1, sizeX, sizeY)
	if i + 1 < sizeX and j + 1 < sizeY:
		if vert[i + 1][j + 1].isChecked == False:
			vertCalc(vert, (i + 1) * sizeY + j + 1, sizeX, sizeY)

def vertPath(vert, start, end, sizeX, sizeY, path = []):
	same = []
	i = end // sizeY
	j = end % sizeY
	path.insert(0, i * sizeY + j)
	if i * sizeY + j == start:
		vert.clear()
		return path
	if i - 1 >= 0:
		if round(vert[i][j].value - vert[i][j].n[i - 1][j], 5) == vert[i - 1][j].value:
			same.append((i - 1) * sizeY + j)
	if i + 1 < sizeX:
		if round(vert[i][j].value - vert[i][j].n[i + 1][j], 5) == vert[i + 1][j].value:
			same.append((i + 1) * sizeY + j)
	if j - 1 >= 0:
		if round(vert[i][j].value - vert[i][j].n[i][j - 1], 5) == vert[i][j - 1].value:
			same.append(i * sizeY + j - 1)
	if j + 1 < sizeY:
		if round(vert[i][j].value - vert[i][j].n[i][j + 1], 5) == vert[i][j + 1].value:
			same.append(i * sizeY + j + 1)
	if i - 1 >= 0 and j - 1 >= 0:
		if round(vert[i][j].value - vert[i][j].n[i - 1][j - 1], 5) == vert[i - 1][j - 1].value:
			same.append((i - 1) * sizeY + j - 1)
	if i - 1 >= 0 and j + 1 < sizeY:
		if round(vert[i][j].value - vert[i][j].n[i - 1][j + 1], 5) == vert[i - 1][j + 1].value:
			same.append((i - 1) * sizeY + j + 1)
	if i + 1 < sizeX and j - 1 >= 0:
		if round(vert[i][j].value - vert[i][j].n[i + 1][j - 1], 5) == vert[i + 1][j - 1].value:
			same.append((i + 1) * sizeY + j - 1)
	if i + 1 < sizeX and j + 1 < sizeY:
		if round(vert[i][j].value - vert[i][j].n[i + 1][j + 1], 5) == vert[i + 1][j + 1].value:
			same.append((i + 1) * sizeY + j + 1)
	return vertPath(vert, start, same[randint(0, len(same)) - 1], sizeX, sizeY, path)

def findPath(sizeX, sizeY, start, end):
	vert = []
	for i in range(sizeX):
		temp = []
		for j in range(sizeY):
			temp.append(Vertex(i * sizeY + j, sizeX, sizeY))
		vert.append(temp)
	vert[start // sizeY][start % sizeY].value = 0
	vertCalc(vert, start, sizeX, sizeY)
	return vertPath(vert, start, end, sizeX, sizeY)