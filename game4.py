#!/usr/bin/env python3.9
import pygame
from random import randint
import sys
import math
import time

BLACK = (0, 0, 0)
RED = (252, 104, 82)
GREEN = (144, 255, 92)

pygame.init()
clock = pygame.time.Clock()
SIZE = width, height = 800, 600
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Circle game')
score = 0

# Text settings
font = pygame.font.SysFont(None, 38) 

# Circle settings
c_x = randint(50, width-60)
c_y = randint(50, height-60)
x_speed = 10
y_speed = 10

radius = 30
center = [50, 50]
pygame.draw.circle(screen, RED, center, radius)

# Line settings
isKeyDown = False
lastValue = 0
l_x = 50
l_height = 200
l_start = 100
line = [[l_x, l_start], [l_x, l_start+l_height]]
pygame.draw.line(screen, GREEN, line[0], line[1], 3)

def showText(text='hello', coo=(width-200, 50)):
  img = font.render(text, True, GREEN)
  screen.blit(img, coo)

# Move circle
def move(x, y):
  pygame.draw.circle(screen, RED, (x, y), radius)

# Move line
def moveline(count=0):
  line[0][1] += count
  line[1][1] += count
  pygame.draw.line(screen, GREEN, line[0], line[1], 3)

def gameOver():
  screen.fill(BLACK)
  showText('Game over!', (width//2-50, height//2))
  pygame.display.update()

while 1:
  # Clear screen
  screen.fill(BLACK)
  showText('Score: {0}'.format(score))
  # Change circle position
  if (c_x + radius >= width) or (c_x <= 0): 
    x_speed = -x_speed
  if (c_y + radius >= height) or (c_y <= 0): 
    y_speed = -y_speed
  # Checking for contact between the ball and the line
  if math.isclose(c_x, l_x + radius, abs_tol=3) and c_y >= line[0][1] and c_y <= line[1][1]:
    score += 1
    #y_speed = -y_speed
    x_speed = -x_speed
  c_x += x_speed
  c_y += y_speed
  move(c_x, c_y)
  # If key (w or s) down keep moving line.
  if isKeyDown:
    moveline(lastValue)
  else:
    moveline()
  pygame.display.update()
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameOver() 
      break
    # Move platform on button click
    if event.type == pygame.KEYDOWN:
      lastValue = 0
      isKeyDown = True
      pressed = pygame.key.get_pressed()
      if pressed[pygame.K_w]:
        lastValue = -10
        moveline(lastValue)  
      if pressed[pygame.K_s]:
        lastValue = 10
        moveline(lastValue)  
    if event.type == pygame.KEYUP:
      isKeyDown = False
  else: continue
  break

time.sleep(1)
pygame.quit()
sys.exit()
