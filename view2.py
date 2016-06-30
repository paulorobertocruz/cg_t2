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
