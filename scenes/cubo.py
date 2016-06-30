
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

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

	def draw(self):
		# glBegin(GL_QUADS)
		# glEnd()
		print("asdfasdf")
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
