'''
Juego de Conecta Cuatro

<Nombre_1>, <Matrícula_1>
Eugenia Ruiz Velasco Olvera, A01177887
Christopher Gabriel Pedraza Pohlenz, A01177767
'''

from turtle import *

# Hacer tablero

ROWS = 8
COLS = 10
inicia_x = 0
inicia_y = 0
fin_x = 10
fin_y = 8

espacio = 1

def rectangulo (ix, iy, fx, fy, color):
    up()
    goto(ix,iy)
    down()
    begin_fill()
    
    for count in range(2):
        forward(fx)
        left(90)
        forward(fy)
        left(90)
    end_fill()
    

def dibujar_tablero():
    rectangulo(inicia_x, inicia_y, fin_x, fin_y,'light blue')


def circulos(x, y, e, color):
    up()
    goto(x, y-e)
    seth(0)
    down()
    begin_fill()
    circle(x-y)
    end_fill()

def dibujar_circulos():
    circulos(inicia_x, inicia_y, espacio,'white')


setup(800, 800, 370, 0)
setworldcoordinates(-0.5,-0.5,COLS+0.5,ROWS+2.5)
dibujar_tablero()
dibujar_circulos()
done()