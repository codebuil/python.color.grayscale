import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 4),
    (1, 1, 4),
    (-1, -1, 4),
    (-1, 1, 4)
)

arestas = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

def CuboRetangular():
    glBegin(GL_LINES)
    for aresta in arestas:
        for vertice in aresta:
            glVertex3fv(vertices[vertice])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    
    glTranslatef(0.0, 0.0, -6.0)  # Posicione a câmera no centro do cubo

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Defina a cor de fundo para amarelo
        glClearColor(1.0, 1.0, 0.0, 1.0)

        CuboRetangular()
        pygame.display.flip()
        pygame.time.wait(10)

main()

