import pygame
import time

SIZE = (1366, 700)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE  = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
stop = 1
move = 2

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("SANIC!")

square = pygame.Rect(640/2 - 100/2, 480/2 - 100/2, 100, 100)
xaxis = 0
yaxis = 0
gravity = 10
jump = False
t_counter = 0

running = True
while running == True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_w and gravity == 0:
			yaxis = -15
			jump = True
		elif jump == True and t_counter != 1:
			t_counter = t_counter + 1
			continue
		elif jump == True and t_counter == 1:
			yaxis = 0
			gravity = 10
			jump = False
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
			if square.x >=0:
				xaxis = xaxis - 10
		elif event.type == pygame.KEYUP and event.key == pygame.K_a:
			xaxis = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
			if square.x + square.w <= SIZE[0]:
				xaxis = xaxis + 10
		elif event.type == pygame.KEYUP and event.key == pygame.K_d:
			xaxis = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			

	
	screen.fill(GREEN)
	pygame.draw.rect(screen, BLUE, square)
	pygame.display.flip()
	
	time.sleep(1/60)
	
	square = square.move(0, gravity)
	square = square.move(xaxis, yaxis)
	if square.y + square.h >= SIZE[1]:
		gravity = 0
	elif square.x + square.w >= SIZE[0]:
		xaxis = 0
	elif square.x <= 0:
		xaxis = 0
