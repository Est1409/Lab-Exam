import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

screen = pygame.display.set_mode((900, 700))

run  = True
while run:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.line(screen, red, (50, 50), (250, 250), 3)
    pygame.display.update()
pygame.quit()
