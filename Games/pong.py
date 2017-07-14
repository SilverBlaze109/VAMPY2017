import pygame
import time
import random

WIDTH = 680
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE  = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WAITING = 1
PLAYING = 2
state_time = time.time()
state = WAITING

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Let's play Pong!")

speed_lpaddle = 0
speed_rpaddle = 0
speed_ball_x = 0
speed_ball_y = 0

score_left = 0
score_right = 0

paddle_w = .05 * WIDTH
paddle_h = 5 * paddle_w
ball_w = paddle_w
rect_lpaddle = pygame.Rect(paddle_w, HEIGHT/2 - paddle_h/2, paddle_w, paddle_h)
rect_rpaddle = pygame.Rect(WIDTH - 2*paddle_w, HEIGHT/2 - paddle_h/2, paddle_w, paddle_h)
rect_ball = pygame.Rect(WIDTH/2 - ball_w/2, WIDTH/2 - ball_w/2, ball_w, ball_w)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
			speed_lpaddle = -5
		elif event.type == pygame.KEYUP and event.key == pygame.K_w:
			speed_lpaddle = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			speed_lpaddle = 5
		elif event.type == pygame.KEYUP and event.key == pygame.K_s:
			speed_lpaddle = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			speed_rpaddle = -5
		elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
			speed_rpaddle = 0
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			speed_rpaddle = 5
		elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
			speed_rpaddle = 0
		
	rect_lpaddle.move_ip(0, speed_lpaddle)
	rect_rpaddle.move_ip(0, speed_rpaddle)
	if state == PLAYING:
		rect_ball.move_ip(speed_ball_x, speed_ball_y)
	elif state == WAITING:
		if time.time() - state_time >= 1:
			state = PLAYING
			state_time = time.time()
			speed_ball_x = 2 * random.randint(0, 1) - 1
			speed_ball_y = random.randint(-5, 5)
			speed_ball_x *= 5
	
	
	
	if rect_ball.y <= 0:
		rect_ball.y = 0
		speed_ball_y = abs(speed_ball_y)
	elif rect_ball.y + rect_ball.h >= HEIGHT:
		rect_ball.y = HEIGHT - rect_ball.h
		speed_ball_y = -abs(speed_ball_y)
	
	
	if rect_lpaddle.x <= rect_ball.x and rect_ball.x <= rect_lpaddle.x + rect_lpaddle.w:
		if rect_lpaddle.y <= rect_ball.y and rect_ball.y <= rect_lpaddle.y + rect_lpaddle.h:
			rect_ball.x = rect_lpaddle.x + rect_lpaddle.w
			speed_ball_x = abs(speed_ball_x)
			speed_ball_y = random.randint(-5, 5)
			score_left += 1
	
	if rect_rpaddle.x <= rect_ball.x and rect_ball.x <= rect_rpaddle.x + rect_rpaddle.w:
		if rect_rpaddle.y <= rect_ball.y and rect_ball.y <= rect_rpaddle.y + rect_rpaddle.h:
			rect_ball.x = rect_rpaddle.x - rect_ball.w
			speed_ball_x = -abs(speed_ball_x)
			speed_ball_y = random.randint(-5, 5)
			score_right += 1
	
	if rect_ball.x + rect_ball.w < 0 or rect_ball.x > WIDTH:
		state = WAITING
		state_time = time.time()
		rect_ball.x = WIDTH/2 - rect_ball.w/2
		rect_ball.y = HEIGHT/2 - rect_ball.h/2
		speed_ball_x = 0
		speed_ball_y = 0


	screen.fill(BLACK)
	for i in range(score_left):
		pip = pygame.Rect(rect_ball.w + i*(2 + rect_ball.w/2), rect_ball.w, rect_ball.w/2, rect_ball.w)
		pygame.draw.rect(screen, YELLOW, pip)
	for i in range(score_right):
		pip = pygame.Rect(WIDTH - rect_ball.w - i*(2 + rect_ball.w/2), rect_ball.w, rect_ball.w/2, rect_ball.w)
		pygame.draw.rect(screen, YELLOW, pip)
	
	pygame.draw.rect(screen, RED, rect_lpaddle)
	pygame.draw.rect(screen, BLUE, rect_rpaddle)
	pygame.draw.rect(screen, WHITE, rect_ball)
	pygame.display.flip()
	
	time.sleep(1/60)
