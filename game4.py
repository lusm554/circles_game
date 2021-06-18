#!/usr/bin/env python3.9
import pygame
from random import randint
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
SIZE = width, height = 800, 600
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Circle game')

# Circle settings
x = randint(50, width-60)
y = randint(50, height-60)
x_speed = 2.5
y_speed = 2.5

radius = 30
center = [50, 50]
circle = pygame.draw.circle(screen, WHITE, center, radius)

# Move circle
def move(x, y):
  pygame.draw.circle(screen, WHITE, (x, y), radius)

while 1:
  # Clear screen
  screen.fill(BLACK)
  # Change circle position
  if (x + radius >= width) or (x <= 0): 
    x_speed = -x_speed
  if (y + radius >= height) or (y <= 0): 
    y_speed = -y_speed
  x += x_speed
  y += y_speed
  move(x, y)
  pygame.display.update()
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
