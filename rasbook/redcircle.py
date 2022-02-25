import pygame
from pygame.locals import *  #

width, height = 640, 640
radius = 0
mouseX, mouseY = 0, 0  #2

pygame.init()
window = pygame.display.set_mode((width, height))
window.fill(pygame.Color(255, 255, 255))

fps = pygame.time.Clock()  #3

while True: #4
  for event in pygame.event.get():  #5
    if event.type == MOUSEMOTION:  #6
      mouseX, mouseY = event.pos
    if event.type == MOUSEBUTTONDOWN:  #7
      window.fill(pygame.Color(255, 255, 255))
  radius = (abs(width/2 - mouseX)+abs(height/2 - mouseY))/2 + 1  #8
  pygame.draw.circle(window, pygame.Color(255, 0, 0), (mouseX, mouseY), radius, 1)  #9
  pygame.display.update()
  fps.tick(30)  #10



