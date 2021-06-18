import pygame
import random

pygame.init()
screen = pygame.display.set_mode([900,900])
keep_going = True

GREEN = (0,255,0)
WHITE = (255, 255, 255)
RED = (255,0,0)
ORANGE = (255,127,80)
BLUE = (30,144,255)
colors = [GREEN, WHITE, RED, ORANGE, BLUE]

def circle(color, coordinates, radius=50):
  pygame.draw.circle(screen, color, coordinates, radius)

def clear_screen():
  screen.fill((112, 60, 247))

# default circles
circles = [[RED, (100, 100)], [WHITE, (200, 100)], [ORANGE, (300, 100)]]

while keep_going:
  for event in pygame.event.get():
    # Change circle position when user move cursor
    if event.type == pygame.MOUSEMOTION:
      clear_screen()
      x, y = pygame.mouse.get_pos()
      circle((128,128,128), (x, y))
    # Add circle to screen
    if event.type == pygame.MOUSEBUTTONDOWN:
      x, y = pygame.mouse.get_pos()
      current_color = random.choice(colors)
      circle(current_color, (x, y))
      circles.append([current_color, (x, y)])
    if event.type == pygame.QUIT:
      keep_going = False
  for c in circles:
    circle(c[0], c[1])
  pygame.display.update()

pygame.quit()
