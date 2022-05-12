'''
Juego de Conecta Cuatro

<Nombre_1>, <Matrícula_1>
Eugenia Ruiz Velasco Olvera, A01177887
Christopher Gabriel Pedraza Pohlenz, A01177767
'''

from turtle import *
import math as m

# Hacer tablero

ROWS = 8
COLS = 10
inicia_x = 0
inicia_y = 0
fin_x = 10
fin_y = 8

espacio = 1

board = []

def create_board_matrix():
    tempRow = []
    for i in range(ROWS):
        for i in range(COLS):
            tempRow.append(0)

        board.append(tempRow)
        tempRow = []

def get_board_coordinates(x, y):
    new_x = m.floor(x)
    new_y = m.floor(y)
    return new_x, new_y

def play(x, y):
    new_x, new_y = get_board_coordinates(x, y)
    print(new_x, new_y)

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
onscreenclick(play)
done()