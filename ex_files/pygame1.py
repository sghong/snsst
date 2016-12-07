import pygame

width = 640
height = 480
radius = 100
fill = 1

pygame.init()

window = pygame.display.set_mode((width, height))
window.fill(pygame.Color(255,255,255))

while True:
    pygame.draw.circle(window,
                       pygame.Color(255,0,0),
                       (width/2, height/2),
                       radius, fill)
    pygame.display.update()
    if pygame.QUIT in [e.type for e in pygame.event.get()]:
        break
