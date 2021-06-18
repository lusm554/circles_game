import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((900, 900))
radius = 10
white = (255, 255, 255)
black = (0, 0, 0)

def circle(coordinates):
  pygame.draw.circle(screen, black, coordinates, radius)

line = []
isDraw = False

while 1:
  for event in pygame.event.get():
    if event.type == pygame.MOUSEMOTION:
      screen.fill(white)
      x, y = pygame.mouse.get_pos()
      circle((x, y))
      if isDraw:
        line.append([(x, y)])
    # Add circle to screen
    if event.type == pygame.MOUSEBUTTONDOWN:
      isDraw = True
      x, y = pygame.mouse.get_pos()
      circle((x, y))
      line.append([(x, y)])
    if event.type == pygame.MOUSEBUTTONUP:  
      isDraw = False
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  for c in line:
    circle(c[0])
  pygame.display.update()

