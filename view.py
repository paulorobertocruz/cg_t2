"""###################################################
#Para instalar a biblioteca basta fazer (no ubuntu): sudo apt-get install python-opengl
#
# Exemplo3DComIluminacao.py
# Um programa OpenGL simples que abre uma janela GLUT,
# desenha um "torus" com ilumina��o, permite fazer
# zoom in e zoom out com as teclas Home e End, e
# mover a posi��o do observador com o mouse
#
# Marcelo Cohen e Isabel H. Manssour
# Este c�digo acompanha o livro
# "OpenGL - Uma Abordagem Pr�tica e Objetiva"
#
###################################################"""

import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from vamos_desenhar_2_cubo import Cube

# Inicializa a vari�vel que especifica o �ngulo da proje��o
# perspectiva
angle=45.0

# Inicializa vari�vel com a rela��o de aspecto da janela
fAspect = 1.0

# Inicializa as vari�veis utilizadas para alterar
# a posi��o do observador
rotX = rotY = 0
obsX = obsY = 0
obsZ = 15.0
obsX_ini = obsY_ini = obsZ_ini = 0
x_ini = y_ini = bot = 0

# Fun��o respons�vel pela especifica��o dos par�metros de ilumina��o
def DefineIluminacao():
	luzAmbiente  = (0.2,0.2,0.2,1.0)
	luzDifusa	= (0.7,0.7,0.7,1.0)		# "cor"
	luzEspecular = (1.0, 1.0, 1.0, 1.0)		# "brilho"
	posicaoLuz   = (0.0, 50.0, 50.0, 1.0)

	# Capacidade de brilho do material
	especularidade = (1.0,1.0,1.0,1.0)
	especMaterial = 60

	# Define a reflet�ncia do material
	glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade)
	# Define a concentra��o do brilho
	glMateriali(GL_FRONT,GL_SHININESS,especMaterial)

	# Ativa o uso da luz ambiente
	glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)

	# Define os par�metros da luz de n�mero 0
	glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa )
	glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular )
	glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz )

def Desenha():
	# Limpa a janela de visualiza��o com a cor
	# de fundo definida previamente
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	# Chama a fun��o que especifica os par�metros de ilumina��o
	DefineIluminacao()

	# Altera a cor do desenho para azul
	glColor3f(0.0, 0.0, 1.0)

	# glutSolidTorus(20.0, 35.0, 20, 40)

	c = Cube()
	c.draw()

	glPushMatrix()
	glTranslatef(1, 1, 1.0)
	glColor3f(0.0, 1.0, 0.0)
	glutSolidSphere(1,20, 20)
	glPopMatrix()
	glFlush()
	glutSwapBuffers()

# Fun��o usada para especificar a posi��o do observador virtual
def PosicionaObservador():
	# Especifica sistema de coordenadas do modelo
	glMatrixMode(GL_MODELVIEW)
	# Inicializa sistema de coordenadas do modelo
	glLoadIdentity()
	DefineIluminacao()
	# Especifica posi��o do observador e do alvo
	glTranslatef(-obsX,-obsY,-obsZ)
	glRotatef(rotX,1,0,0)
	glRotatef(rotY,0,1,0)

# Fun��o usada para especificar o volume de visualiza��o
def EspecificaParametrosVisualizacao():
	# Especifica sistema de coordenadas de proje��o
	glMatrixMode(GL_PROJECTION)
	# Inicializa sistema de coordenadas de proje��o
	glLoadIdentity()

	# Especifica a proje��o perspectiva(angulo,aspecto,zMin,zMax)
	gluPerspective(angle,fAspect,0.5,500)

	PosicionaObservador()

# Fun��o callback chamada para gerenciar eventos de teclas normais (ESC)
def Teclado (tecla, x, y):
	if tecla==chr(27): # ESC ?
		sys.exit()

# Fun��o callback chamada para gerenciar eventos de teclas especiais
def TeclasEspeciais (tecla, x, y):
	global angle

	if tecla == GLUT_KEY_HOME:
		if angle>=10:	angle -=5
	elif tecla == GLUT_KEY_END:
		if angle<=150: angle +=5

	EspecificaParametrosVisualizacao()
	glutPostRedisplay()

# Fun��o callback chamada quando o tamanho da janela � alterado
def AlteraTamanhoJanela (w, h):
	global fAspect

	# Para previnir uma divis�o por zero
	if h == 0: h = 1

	# Especifica as dimens�es da viewport
	glViewport(0, 0, w, h)

	# Calcula a rela��o de aspecto
	fAspect = float(w)/h;

	EspecificaParametrosVisualizacao()

# Fun��o callback para eventos de bot�es do mouse
def GerenciaMouse (button, state, x, y):
	global x_ini, y_ini, obsX_ini, obsY_ini, obsZ_ini
	global rotX_ini, rotY_ini, bot

	if state == GLUT_DOWN:

		# Salva os par�metros atuais
		x_ini = x
		y_ini = y
		obsX_ini = obsX
		obsY_ini = obsY
		obsZ_ini = obsZ
		rotX_ini = rotX
		rotY_ini = rotY
		bot = button;

	else: bot = -1;

# Fun��o callback chamada para eventos de movimento do mouse
def GerenciaMovim (x, y):
	global rotX,rotY,obsX,obsY,obsZ

	SENS_ROT	= 5.0
	SENS_OBS	= 10.0
	SENS_TRANSL	= 10.0

	# Bot�o esquerdo ?
	if bot == GLUT_LEFT_BUTTON:

		# Calcula diferen�as
		deltax = x_ini - x
		deltay = y_ini - y
		# E modifica �ngulos
		rotY = rotY_ini - deltax/SENS_ROT
		rotX = rotX_ini - deltay/SENS_ROT

	# Bot�o direito ?
	elif bot == GLUT_RIGHT_BUTTON:

		# Calcula diferen�a
		deltaz = y_ini - y
		# E modifica dist�ncia do observador
		obsZ = obsZ_ini + deltaz/SENS_OBS

	# Bot�o do meio ?
	elif bot == GLUT_MIDDLE_BUTTON:

		# Calcula diferen�as
		deltax = x_ini - x;
		deltay = y_ini - y;
		# E modifica posi��es
		obsX = obsX_ini + deltax/SENS_TRANSL
		obsY = obsY_ini - deltay/SENS_TRANSL

	PosicionaObservador()
	glutPostRedisplay()

# Fun��o respons�vel por inicializar par�metros e vari�veis
def Inicializa():

	# Define a cor de fundo da janela de visualiza��o como branca
	glClearColor(1.0, 1.0, 1.0, 1.0)

	# Habilita a defini��o da cor do material a partir da cor corrente
	glEnable(GL_COLOR_MATERIAL)
	# Habilita o uso de ilumina��o
	glEnable(GL_LIGHTING)
	# Habilita a luz de n�mero 0
	glEnable(GL_LIGHT0)
	# Habilita o Z Buffer
	glEnable(GL_DEPTH_TEST)

	# Habilita o modelo de coloriza��o de Gouraud
	glShadeModel(GL_SMOOTH)

# Programa principal
if (__name__ == '__main__'):

	glutInit();
	# Define o modo de opera��o da GLUT
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);

	# Especifica a posi��o inicial da janela GLUT
	glutInitWindowPosition(5,5)

	# Especifica o tamanho inicial em pixels da janela GLUT
	glutInitWindowSize(450,450)

	# Cria a janela passando como argumento o titulo da mesma
	glutCreateWindow("View")

	# Registra a fun��o callback de redesenho da janela de visualiza��o
	glutDisplayFunc(Desenha)

	# Registra a fun��o callback de redimensionamento da janela de visualiza��o
	glutReshapeFunc(AlteraTamanhoJanela)

	# Registra a fun��o callback para eventos de bot�es do mouse
	glutMouseFunc(GerenciaMouse)

	# Registra a fun��o callback para eventos de movimento do mouse
	glutMotionFunc(GerenciaMovim)

	# Registra a fun��o callback para tratamento das teclas normais
	glutKeyboardFunc (Teclado)

	# Registra a fun��o callback para tratamento das teclas especiais
	glutSpecialFunc (TeclasEspeciais)

	# Chama a fun��o respons�vel por fazer as inicializa��es
	Inicializa()

	# Inicia o processamento e aguarda intera��es do usu�rio
	glutMainLoop()
