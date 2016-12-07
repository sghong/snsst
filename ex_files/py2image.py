import pygame

pygame.init()
screen= pygame.display.set_mode((450,350))
background = pygame.image.load("toy1.jpg").convert_alpha() 
theremin = pygame.image.load("toy2.jpg").convert_alpha() 

screen.blit(background, (0,0)) 
screen.blit(theremin, (135,50)) 

while True:
  pygame.display.update()


