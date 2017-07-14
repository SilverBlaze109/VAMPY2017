import pygame
import time

SIZE = (640, 480)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE  = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Hello World!")

square = pygame.Rect(640/2 - 100/2, 480/2 - 100/2, 100, 100)
xaxis = 1
yaxis = -1

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			xaxis *= 2
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			xaxis /= 2
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			yaxis *= 2
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			yaxis /= 2
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
			yaxis = -abs(yaxis)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			yaxis = abs(yaxis)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
			xaxis = -abs(xaxis)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
			xaxis = abs(xaxis)

	screen.fill(BLACK)
	pygame.draw.rect(screen, RED, square)
	pygame.display.flip()
	
	time.sleep(1/60)
	
	square = square.move(xaxis, yaxis)
	if square.x + square.w >= SIZE[0]:
		xaxis = -abs(xaxis)
	elif square.x <= 0:
		xaxis = abs(xaxis)
	elif square.y + square.h >= SIZE[1]:
		yaxis = -abs(yaxis)
	elif square.y <= 0:
		yaxis = abs(yaxis)
