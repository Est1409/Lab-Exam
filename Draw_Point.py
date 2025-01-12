import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
purple = (100, 0, 255)
screen = pygame.display.set_mode((900, 700))

run  = True
while run:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.circle(screen, purple, (50, 50), 3)
    pygame.draw.rect(screen, purple, (100, 100, 400, 200))
    pygame.display.update()
pygame.quit()
