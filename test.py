import pygame

background_colour = (234,212,252)

screen=pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("I'm Mark")

screen.fill(background_colour)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
