import pygame

pygame.init()
screen= pygame.display.set_mode((350,200))
background = pygame.image.load("toy1.jpg") # 1
background.convert_alpha() # 2
screen.blit(background, (0,0)) # 3
while True:
  pygame.display.update()


