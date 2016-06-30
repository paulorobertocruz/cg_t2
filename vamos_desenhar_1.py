import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def rectangulo(x,y,width, height, color):

    x, y, width, height = x/10, y/10, width/10, height/10

    glBegin(GL_QUADS)

    glColor3f(color[0],color[1],color[2])

    #verticies
    glVertex3f(x, y, 0)
    glVertex3f(x + width, y, 0)
    glVertex3f(x + width, y - height, 0)
    glVertex3f(x, y - height, 0)

    glEnd()



def quadrado_gradiente(x = 0, y = 0, c1 = (255, 0, 0), c2 = (255,255,0)):
    x = x/10
    y = y/10
    glBegin(GL_QUADS)
    #vermelho
    glColor3f(c1[0],c1[1],c1[2])
    #verticies
    glVertex3fv((0 + x,0.5 + y, 0 ))
    glVertex3fv((0 + x,0 + y, 0 ))
    #amarelo
    glColor3f(c2[0],c2[1],c2[2])
    #verticies
    glVertex3fv((0.5 + x, 0 + y, 0 ))
    glVertex3fv((0.5 + x, 0.5 + y, 0 ))
    glEnd()

def boneco_palito(x = 0, y = 0):
    #cabeça
    rectangulo(-6, -1 , 2, 2, (0,0,0))
    #pescoço
    rectangulo(-5.25, -3 , 0.5, 0.5, (0,0,0))
    #tronco
    rectangulo(-6, -3.5 , 2, 3, (0,0,0))

    #braços
    rectangulo(-6.5, -3.5 , 0.4, 2.87, (0,0,0))
    rectangulo(-3.9, -3.5 , 0.4, 2.87, (0,0,0))

    #ombros
    rectangulo(-6.2, -3.5 , 0.4, 0.5, (0,0,0))
    rectangulo(-4.1, -3.5 , 0.4, 0.5, (0,0,0))

    #pernas
    rectangulo(-6, -6.5 , 0.5, 3, (0,0,0))
    rectangulo(-4.5, -6.5 , 0.5, 3, (0,0,0))


def casa():
    pass

def triangulo(x = 0, y = 0, scala = 1, cor = (0,0,0) ):
    x = x/10
    y = y/10
    glBegin(GL_TRIANGLE_STRIP)

    glColor3f(cor[0],cor[1],cor[2])

    glVertex3fv((0 + x, 0 + y, 0))
    glVertex3fv((0.3 * scala + x, 0 + y, 0))
    glVertex3fv(((0.3 * scala)/2 + x, 0.3 * scala + y, 0))

    glEnd()

def axis():
    glBegin(GL_LINES);
    # // draw line for x axis
    glColor3f(1.0, 0.0, 0.0);
    glVertex3f(0.0, 0.0, 0.0);
    glVertex3f(1.0, 0.0, 0.0);
    # // draw line for y axis
    glColor3f(0.0, 1.0, 0.0);
    glVertex3f(0.0, 0.0, 0.0);
    glVertex3f(0.0, 1.0, 0.0);
    # // draw line for Z axis
    glColor3f(0.0, 0.0, 1.0);
    glVertex3f(0.0, 0.0, 0.0);
    glVertex3f(0.0, 0.0, 1.0);
    glEnd();

def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    quadrado_gradiente(2,3)

    triangulo(-2,-3,1,(255,0,0))

    triangulo(2,-3,1,(0,0,255))

    #casa
    triangulo(-9.7, 3, 2.2, (255,0,0))
    quadrado_gradiente(-9,-2, (0,1,0), (0,1,0))

    #palito
    boneco_palito()

    glutSwapBuffers()
    return


def main():
    window_name = "janela tretada"
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_DEPTH|GLUT_RGB)
    glutInitWindowSize(600,600)
    glutCreateWindow(window_name)

    glClearColor(255.0,255.0,255.0,1)
    glutDisplayFunc(desenha)

    glutMainLoop()

if __name__ == "__main__":
    main()
