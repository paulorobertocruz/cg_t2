import sys
import importlib
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

if len(sys.argv) < 2:
	exit("deve ter mais argumentos")

scene_name = sys.argv[1]
Cena = importlib.import_module("scenes."+scene_name)
print(Cena.Scene)

class Viewer():
	window_name = "View"
	window_width = 600
	window_height = 600
	window_ratio = window_width / window_height

	angle = 45

	rotX = rotY = 0
	obsX = obsY = 0
	obsZ = 15.0
	obsX_ini = obsY_ini = obsZ_ini = 0
	x_ini = y_ini = bot = 0
	rotX_ini = rotY_ini = 0

	light = {
		"ambiente" : (0.2,0.2,0.2,1.0),
		"difusa": (0.7,0.7,0.7,1.0),
		"especular": (1.0, 1.0, 1.0, 1.0),
		"position"  : (0.0, 50.0, 50.0, 1.0),
		"especularidade": (1.0,1.0,1.0,1.0),
		"especularidade_material": 60,
	}

	def DefineIluminacao(self):
		glMaterialfv(GL_FRONT,GL_SPECULAR, self.light["especularidade"])

		glMateriali(GL_FRONT,GL_SHININESS,self.light["especularidade_material"])

		glLightModelfv(GL_LIGHT_MODEL_AMBIENT, self.light["ambiente"])

		glLightfv(GL_LIGHT0, GL_AMBIENT, self.light["ambiente"])
		glLightfv(GL_LIGHT0, GL_DIFFUSE, self.light["difusa"] )
		glLightfv(GL_LIGHT0, GL_SPECULAR, self.light["especular"] )
		glLightfv(GL_LIGHT0, GL_POSITION, self.light["position"] )

	def PosicionaObservador(self):
		# Especifica sistema de coordenadas do modelo
		glMatrixMode(GL_MODELVIEW)

		glLoadIdentity()
		self.DefineIluminacao()

		glTranslatef(-self.obsX,-self.obsY,-self.obsZ)
		glRotatef(self.rotX,1,0,0)
		glRotatef(self.rotY,0,1,0)

	def EspecificaParametrosVisualizacao(self):

		glMatrixMode(GL_PROJECTION)

		glLoadIdentity()

		gluPerspective(self.angle,self.window_width/self.window_height,0.5,500)

		self.PosicionaObservador()


	def AlteraTamanhoJanela(self,w, h):

		if h == 0: h = 1

		glViewport(0, 0, w, h)
		self.window_width = w
		self.window_height = h
		self.window_ratio = w/h

		self.EspecificaParametrosVisualizacao()

	def Teclado(self, tecla, x, y):
		if tecla==chr(27): # ESC ?
			sys.exit()

	def TeclasEspeciais(self, tecla, x, y):

		if tecla == GLUT_KEY_HOME:
			if angle>=10:	angle -=5
		elif tecla == GLUT_KEY_END:
			if angle<=150: angle +=5

		self.EspecificaParametrosVisualizacao()
		glutPostRedisplay()


	def GerenciaMouse(self, button, state, x, y):
		self.x_ini, self.y_ini, self.obsX_ini, self.obsY_ini, self.obsZ_ini
		self.rotX_ini, self.rotY_ini, self.bot

		if state == GLUT_DOWN:

			# Salva os par�metros atuais
			self.x_ini = x
			self.y_ini = y
			self.obsX_ini = self.obsX
			self.obsY_ini = self.obsY
			self.obsZ_ini = self.obsZ
			self.rotX_ini = self.rotX
			self.rotY_ini = self.rotY
			self.bot = button;

		else: self.bot = -1;


	def GerenciaMovim (self, x, y):

		SENS_ROT	= 5.0
		SENS_OBS	= 10.0
		SENS_TRANSL	= 10.0

		if self.bot == GLUT_LEFT_BUTTON:

			# Calcula diferen�as
			deltax = self.x_ini - x
			deltay = self.y_ini - y
			# E modifica �ngulos
			self.rotY = self.rotY_ini - deltax/SENS_ROT
			self.rotX = self.rotX_ini - deltay/SENS_ROT

		elif self.bot == GLUT_RIGHT_BUTTON:

			deltaz = self.y_ini - y

			self.obsZ = self.obsZ_ini + deltaz/SENS_OBS

		elif self.bot == GLUT_MIDDLE_BUTTON:

			deltax = self.x_ini - x;
			deltay = self.y_ini - y;

			self.obsX = self.obsX_ini + deltax/SENS_TRANSL
			self.obsY = self.obsY_ini - deltay/SENS_TRANSL

		self.PosicionaObservador()
		glutPostRedisplay()


	def Inicializa(self):

		glClearColor(1.0, 1.0, 1.0, 1.0)

		glEnable(GL_COLOR_MATERIAL)

		glEnable(GL_LIGHTING)

		glEnable(GL_LIGHT0)

		glEnable(GL_DEPTH_TEST)

		glShadeModel(GL_SMOOTH)

	def Desenha(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		self.DefineIluminacao()

		c = Cena.Scene()
		c.draw()				




	def main(self):

		glutInit();

		glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);

		glutInitWindowPosition(1,1)

		glutInitWindowSize(self.window_width,self.window_height)

		glutCreateWindow(self.window_name)

		glutDisplayFunc(self.Desenha)

		glutReshapeFunc(self.AlteraTamanhoJanela)

		glutMouseFunc(self.GerenciaMouse)

		glutMotionFunc(self.GerenciaMovim)

		glutKeyboardFunc(self.Teclado)

		glutSpecialFunc (self.TeclasEspeciais)

		self.Inicializa()

		glutMainLoop()



def main():
	v = Viewer()
	v.main()


if __name__ == "__main__":
	main()
