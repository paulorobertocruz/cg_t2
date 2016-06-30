import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

W_WIDTH = 600
W_HEIGHT = 600

rotX = rotY = 0
obsX = obsY = 0
obsZ = 150.0
obsX_ini = obsY_ini = obsZ_ini = 0
x_ini = y_ini = bot = 0



class Cube():
	vcolors = (
		(1,0,1),
		(0,1,0),
		(1,1,0),
		(1.0,1.0,1.0),
		(0,0,0),
		(0,0,1),
		(0,1,0),
		(1,0,0),
	)
	fcolors = (
		(1,0,0),
		(0,1,0),
		(0,0,1),
		(1.0,1.0,0),
		(0,1,1),
		(1,0,1),
	)
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
		(0,1,2,3),
		(3,2,7,6),
		(6,7,5,4),
		(4,5,1,0),
		(1,5,7,2),
		(4,0,3,6),
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

		glBegin(GL_QUADS) #desenha cubo em linhas
		f = 0
		for face in self.faces:
			glColor3f(self.fcolors[f][0],self.fcolors[f][1],self.fcolors[f][2],1)
			# if f < len(self.fcolors):
			f = f+1
			for vertex in face:
				# glColor3f(self.fcolors[vertex][0],self.fcolors[vertex][1],self.fcolors[vertex][2],1)
				glVertex3fv(self.verticies[vertex])
		glEnd()

		glBegin(GL_LINES) #desenha cubo em linhas

		for edge in self.edges:
			for vertex in edge:
				glVertex3fv(self.verticies[vertex])
		glEnd()


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

def desenha():

	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	# glMatrixMode(GL_PROJECTION)
	# glPushMatrix()
	# glLoadIdentity()

	# gluOrtho2D(-5, 5, 5, -5)
	# glMatrixMode(GL_MODELVIEW)
	# axis()
	gluPerspective(45, W_WIDTH/W_HEIGHT, 0.1, 50)
	glTranslatef(0,0.2,-5)
	# glRotatef(0,0,0,0)
	glColor3f(1,0,0)
	c = Cube()
	c.draw()
	glRotatef(1,3,1,1)
	# while True:
	# 	glRotatef(1,3,1,1)



	glutSwapBuffers()
	return

def teclado(key,x,y):
	pass
	# k = key.decode("UTF-8")
	# print(str(k))
	# if k == " ":
	# 	print("asdfaa")

def main():
	window_name = "janela tretada"
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE|GLUT_DEPTH|GLUT_RGB)
	glutInitWindowSize(W_WIDTH,W_HEIGHT)
	glutCreateWindow(window_name)

	glClearColor(1,1,1,1)
	glutDisplayFunc(desenha)
	glutKeyboardFunc(teclado)

	glutMainLoop()

if __name__ == "__main__":
	main()
