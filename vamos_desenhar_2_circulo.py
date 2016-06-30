import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def triangulo(x = 0, y = 0, scala = 1):
    glBegin(GL_TRIANGLE_STRIP)

    glVertex3fv((0 + x, 0 + y, 0))
    glVertex3fv((3 + x, 0 + y, 0))
    glVertex3fv((3/2 + x, 3 + y, 0))

    glEnd()

def circulo(cx, cy, r, num_segments):
	# glBegin(GL_LINE_LOOP)
	glBegin(GL_POLYGON)
	for ii in range(num_segments):

		theta = 2.0 * 3.1415926 * ii / num_segments

		x = r * math.cos(theta)
		y = r * math.sin(theta)

		glVertex3f(x + cx, y + cy, 0)

	glEnd();

def quadrado(x, y, width, height):
	glBegin(GL_POLYGON)
	glVertex3f(x, y, 0)
	glVertex3f(x + width, y, 0)
	glVertex3f(x + width, y - height, 0)
	glVertex3f(x, y - height, 0)
	glEnd()

def axis():
	glBegin(GL_LINES);
	# // draw line for x axis
	glColor3f(25.0, 0.0, 0.0);
	glVertex3f(0.0, 0.0, 0.0);
	glVertex3f(25.0, 0.0, 0.0);
	# // draw line for y axis
	glColor3f(0.0, 25.0, 0.0);
	glVertex3f(0.0, 0.0, 0.0);
	glVertex3f(0.0, 25.0, 0.0);
	# // draw line for Z axis
	glColor3f(0.0, 0.0, 25.0);
	glVertex3f(0.0, 0.0, 0.0);
	glVertex3f(0.0, 0.0, 25.0);
	glEnd();

def desenha():

	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	# glMatrixMode(GL_PROJECTION)
	# glPushMatrix()
	# glLoadIdentity()
	gluOrtho2D(-5, 5, 5, -5)
	# glMatrixMode(GL_MODELVIEW)
	# axis()

	glColor3f(1,1,0)
	quadrado(-10,10,20,20)

	glColor3f(1,0,0)
	circulo(0,0,8.5,20)

	glColor3f(1,1,1)
	triangulo(0,0)



	glutSwapBuffers()
	return


def main():
	window_name = "janela tretada"
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE|GLUT_DEPTH|GLUT_RGB)
	glutInitWindowSize(600,600)
	glutCreateWindow(window_name)

	glClearColor(1,1,1,1)
	glutDisplayFunc(desenha)

	glutMainLoop()

if __name__ == "__main__":
	main()
