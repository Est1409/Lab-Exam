import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
purple = (100, 0, 255)

trig1Cordinate = [(450, 100), (350, 300), (550, 300)]
trig2Cordinate = [(350, 300), (250, 500), (450,500)]
trig3Cordinate = [(550, 300), (450 ,500), (650, 500)]
screen = pygame.display.set_mode((900, 700))


run  = True
while run:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.polygon(screen, blue, trig1Cordinate)
    pygame.draw.polygon(screen, blue, trig2Cordinate)
    pygame.draw.polygon(screen, blue, trig3Cordinate)
    pygame.draw.circle(screen, purple, (450, 350), 3)
    pygame.display.update()
pygame.quit()