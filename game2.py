#!/usr/bin/env python3.9
import pygame
import sys

test = False
screen_size = width, height = (700, 700)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
super_green = (144, 255, 92)
super_purple = (231, 128, 214)
radius = 30

# Initialization
pygame.init()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Moving circles')
fps = pygame.time.Clock()
paused = False

cx = [
 #| x | y |count|increase/decrease|color
  [[50, 50], 1, False, white],
  [[width, 150], 2, True, blue],
  [[50, 250], 5, True, red],
  [[width, 350], 10, False, green],
]

cy = [
  [[200, 50], 3, False, super_green],
  [[400, height], 6, True, super_purple],
]  

def movex():
  for v in cx:
    coo, count, action, color  = v 
    if action:
      v[0][0] -= count
    else:
      v[0][0] += count
    if coo[0] > width:
      v[2] = True 
    elif coo[0] <= 0:
      v[2] = False
    cx[cx.index(v)] = v

def movey():
   for v in cy:
    coo, count, action, color  = v 
    if action:
      v[0][1] -= count
    else:
      v[0][1] += count
    if coo[1] > height:
      v[2] = True 
    elif coo[1] <= 0:
      v[2] = False
    cy[cy.index(v)] = v 

def update_pos(): 
  movex()
  movey()

def draw():
  for i in cx+cy:
    pygame.draw.circle(screen, i[3], i[0], radius, 0)

def render():
  screen.fill(black)
  draw()
  pygame.display.update()
  fps.tick(60)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  update_pos()
  render()
