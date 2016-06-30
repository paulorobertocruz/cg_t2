import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Cube():
    color = (0,0,0)
    verticies = [
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, -1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, -1, 1],
        [-1, 1, 1],
    ]

    edges = (
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
        (5, 7),
    )

    faces = (

    )
    def __init__(self):
        for v in self.verticies:
            pass
            # v[0] =  v[0]/2
            # v[1] = v[1]/2
            # v[2] = v[2]/2

    def draw(self):
        # glBegin(GL_QUADS)
        # glEnd()

        glBegin(GL_LINES) #desenha cubo em linhas

        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.verticies[vertex])
        glEnd()

def desenha():

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    cube = Cube()
    cube.draw()

    glutSwapBuffers()
    return


def main():
    window_name = "janela tretada"
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_DEPTH|GLUT_RGB)
    glutInitWindowSize(600,600)
    glutCreateWindow(window_name)

    glClearColor(0,0,0,1)
    glutDisplayFunc(desenha)

    glutMainLoop()

if __name__ == "__main__":
    main()
