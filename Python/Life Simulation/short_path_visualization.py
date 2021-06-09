from dijkstra import findPath
from random import randint
import pygame.gfxdraw
import pygame

#CONST
FPS = 60
SIZEX = 30
SIZEY = 30
CELL_SIZE = 30
WIDTH = SIZEX * CELL_SIZE
HEIGHT = SIZEY * CELL_SIZE

#COLORS
BLACK = (0, 0, 0)
DARKGRAY = (51, 51, 51)
GRAY = (102, 102, 102)
LIGHTGRAY = (153, 153, 153)
GREEN = (51, 153, 51)
DIRTYYELLOW = (153, 153, 0)
ORANGE = (255, 204, 51)

def vertCoord(num):
    pass

class spriteCircle:
	def __init__(self, xy, numVertPath = -1, moveType = 'oneWay', chgVal = 1):
		self.numVertPath = numVertPath
		self.chgVal = chgVal
		self.moveType = moveType
		self.x = xy[0]
		self.y = xy[1]

	def setCoord(self, xy):
		self.x = xy[0]
		self.y = xy[1]

	def moveCircle(self, screen, listVert):
		if (self.x == vertCoord(listVert[self.numVertPath + self.chgVal])[0] 
		and self.y == vertCoord(listVert[self.numVertPath + self.chgVal])[1]):
			self.numVertPath += self.chgVal
			if (self.numVertPath >= len(listVert) - 1 and self.chgVal == 1) or (self.numVertPath <= 0 and self.chgVal == -1):
				if self.moveType == 'oneWay':
					self.numVertPath = 0
					self.setCoord(vertCoord(listVert[self.numVertPath]))
				elif self.moveType == 'infinity':
					if self.chgVal == 1:
						self.chgVal = -1
					else:
						self.chgVal = 1
			
		if self.x > listVert[self.numVertPath + self.chgVal] // SIZEY * CELL_SIZE + CELL_SIZE // 2:
			self.x -= 1
		elif self.x < listVert[self.numVertPath + self.chgVal] // SIZEY * CELL_SIZE + CELL_SIZE // 2:
			self.x += 1
		if self.y > listVert[self.numVertPath + self.chgVal] % SIZEY * CELL_SIZE + CELL_SIZE // 2:
			self.y -= 1
		elif self.y < listVert[self.numVertPath + self.chgVal] % SIZEY * CELL_SIZE + CELL_SIZE // 2:
			self.y += 1

		pygame.gfxdraw.filled_circle(screen, self.x, self.y, int(CELL_SIZE / 10) + 1, ORANGE)
		pygame.gfxdraw.aacircle(screen, self.x, self.y, int(CELL_SIZE / 10) + 1, ORANGE)

lastStart = 0
lastEnd = 0

def listVertPath(start = -1, end = -1):
	global lastStart, lastEnd
	if start == -1 and end == -1:
		start = randint(0, SIZEX * SIZEY - 1)
		end = randint(0, SIZEX * SIZEY - 1)
	listVert = findPath(SIZEX, SIZEY, start, end)
	lastStart = start
	lastEnd = end
	return listVert

def vertCoord(num):
	return num // SIZEY * CELL_SIZE + CELL_SIZE // 2, num % SIZEY * CELL_SIZE + CELL_SIZE // 2

def vertCoordX(num):
	return num // SIZEY * CELL_SIZE + CELL_SIZE // 2

def vertCoordY(num):
	return num % SIZEY * CELL_SIZE + CELL_SIZE // 2

def drawStartEnd(screen, start, end):
	pygame.gfxdraw.filled_circle(screen, vertCoordX(start), vertCoordY(start), int(CELL_SIZE / 10) + 2, GREEN)
	pygame.gfxdraw.filled_circle(screen, vertCoordX(end), vertCoordY(end), int(CELL_SIZE / 10) + 2, GREEN)
	pygame.gfxdraw.aacircle(screen, vertCoordX(start), vertCoordY(start), int(CELL_SIZE / 10) + 2, GREEN)
	pygame.gfxdraw.aacircle(screen, vertCoordX(end), vertCoordY(end), int(CELL_SIZE / 10) + 2, GREEN)

def launchProgramm():
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('Short path visualization')
	pygame.display.set_icon(pygame.image.load("sprites/icon.bmp"))
	clock = pygame.time.Clock()
	listVert = listVertPath()
	sprites = []
	for numVert in range(len(listVert) - 1):
		sprites.append(spriteCircle(vertCoord(listVert[numVert]), numVert))
	running = True
	while running:
		clock.tick(FPS)
		screen.fill(DARKGRAY)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_n:
					listVert.clear()
					sprites.clear()
					listVert = listVertPath()
					for numVert in range(len(listVert) - 1):
						sprites.append(spriteCircle(vertCoord(listVert[numVert]), numVert))
				elif event.key == pygame.K_c:
					listVert.clear()
					sprites.clear()
					listVert = listVertPath(lastStart, lastEnd)
					for numVert in range(len(listVert) - 1):
						sprites.append(spriteCircle(vertCoord(listVert[numVert]), numVert))
		for numVert in range(SIZEX * SIZEY):
			pygame.draw.line(screen, GRAY, vertCoord(numVert), vertCoord(numVert)) #point
		for numElem in range(len(listVert) - 1):
			pygame.draw.line(screen, DIRTYYELLOW, vertCoord(listVert[numElem]), vertCoord(listVert[numElem + 1]), 1)
		for sprite in sprites:
			sprite.moveCircle(screen, listVert)
		drawStartEnd(screen, listVert[0], listVert[-1])
		pygame.display.flip()


def main():
	launchProgramm()

if __name__ == '__main__':
	main()