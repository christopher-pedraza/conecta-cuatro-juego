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
fin_x = COLS
fin_y = ROWS

espacio = 1

board = []

TURNO = 1

RADIO_FICHAS = 0.4


def crear_matriz_tablero():
    tempRow = []
    for i in range(ROWS):
        for i in range(COLS):
            tempRow.append(0)

        board.append(tempRow)
        tempRow = []


def get_coordenadas_tablero(x, y):
    new_x = m.floor(x)
    new_y = m.floor(y)
    return new_x, new_y


def rectangulo (ix, iy, fx, fy, _color):
    color(_color)
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

    color('white')
    for x in range(COLS):
        for y in range(ROWS):
            up()
            goto(x+0.5,y+(0.5-RADIO_FICHAS))
            down()
            begin_fill()
            circle(RADIO_FICHAS, 360, 150)
            end_fill()


def make_temp_lines():
    color('white')
    for i in range(COLS):
        up()
        goto(i+1, 0)
        down()
        goto(i+1, 8)

    for i in range(ROWS):
        up()
        goto(0, i+1)
        down()
        goto(10, i+1)


def dibujar_pieza(x, y, jugador):
    if jugador == 1:
        color('crimson')
    else:
        color('cyan3')

    up()
    goto(x+0.5,y+(0.5-RADIO_FICHAS))
    down()
    begin_fill()
    circle(RADIO_FICHAS, 360, 150)
    end_fill()


def poner_pieza(col, jugador):
    pieza_colocada = False

    if col >= 0 and col < COLS:
        for position in range(ROWS):
            if board[position][col] == 0:
                board[position][col] = jugador

                dibujar_pieza(col, position, jugador)

                return True
            else:
                pieza_colocada = False

    return pieza_colocada


def set_turno(turno):
    global TURNO

    if turno == 1:
        TURNO = 2
    else:
        TURNO = 1


def play(x, y):
    board_x, board_y = get_coordenadas_tablero(x, y)

    global TURNO

    pieza_colocada = poner_pieza(board_x, TURNO)

    if pieza_colocada:
        set_turno(TURNO)


setup(800, 800, 370, 0)
setworldcoordinates(-0.5,-0.5,COLS+0.5,ROWS+2.5)
hideturtle()
tracer(False)
dibujar_tablero()
crear_matriz_tablero()

make_temp_lines()

onscreenclick(play)
done()
