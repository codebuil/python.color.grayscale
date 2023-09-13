import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, -1, -1),
    (0, 1, 0)  # Ponto superior (vértice do triângulo)
)

linhas = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 4),  # Linhas do triângulo
    (1, 4),
    (2, 4),
    (3, 4)
)


def TrianguloBase():
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Defina a cor de fundo para amarelo
        glClearColor(1.0, 1.0, 0.0, 1.0)

        TrianguloBase()
        pygame.display.flip()
        pygame.time.wait(10)


main()

