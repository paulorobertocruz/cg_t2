import sys
import math
import numpy
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
class Sphere():
	def loadTex(self):
		img = Image.open("scenes/soro.jpg")
		img_data = numpy.array(list(img.getdata()), numpy.int8)

		id = glGenTextures(1)
		glPixelStorei(GL_UNPACK_ALIGNMENT,1)
		glBindTexture(GL_TEXTURE_2D, id)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
		return id

	def draw(self):
		tex = self.loadTex()

		glEnable(GL_TEXTURE_2D)
		glBindTexture(GL_TEXTURE_2D, tex)
		glutSolidSphere(1,10,10)



class Scene():
	def draw(self):
		s = Sphere()
		s.draw()
		glColor3f(1,0,0)
		glPushMatrix()
		glutSolidSphere(1,10,10)
		glTranslatef(3, 2, 1.0)
		glColor3f(0.0, 1.0, 0.0)
		glutSolidSphere(1,10,10)
		glPopMatrix()
		glFlush()

		glutSwapBuffers()
