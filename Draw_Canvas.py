import pygame

pygame.init()

white = (255, 255, 255)
screen = 0
def main():
    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption('Main Canvas')
    screen.fill(white)

run  = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == K_F1:
                run = False
    main()
    pygame.display.update()
pygame.quit()
