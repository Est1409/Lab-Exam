import pygame
from OpenGL.GLU import *
from OpenGL.GL import *
from pygame.locals import *

pygame.init()

# Variables
screenSet = (800, 600)

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    
    )



edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

# Setting Screen
screen = pygame.display.set_mode(screenSet, DOUBLEBUF | OPENGL)
gluPerspective(45, (screenSet[0] / screenSet[1]),0.1, 50.0)
glTranslatef(0, 0, -5)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
    # draw cube
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
    
    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()