'''
Juego de Conecta Cuatro

<Kevin Susej Garza Aragon>, <A00833985>
Eugenia Ruiz Velasco Olvera, A01177887
Christopher Gabriel Pedraza Pohlenz, A01177767
'''
import turtle
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
state = {'jugador 1': 0, 'jugador 2': 0, 'empate':0}


def crear_marcador():
    titulo1.color('crimson')
    titulo2.color('cyan3')
    titulo3.color('purple')
    score1.goto(2,9)
    score2.goto(8,9)
    score3.goto(5,9)
    titulo1.goto(2,9.5)
    titulo2.goto(8,9.5)
    titulo3.goto(5,9.5)


def cambiar_marcador(ganador):
    
    if ganador == 0:
        state['empate'] += 1
    elif ganador == 1:
        state['jugador 1'] += 1
    elif ganador == 2:
        state['jugador 2'] += 1
    
    score1.clear()
    score2.clear()
    score3.clear()
    score1.write(state ['jugador 1'], font=('Century Gothic',20,"bold"))
    score2.write(state ['jugador 2'], font=('Century Gothic',20,"bold"))
    score3.write(state ['empate'], font=('Century Gothic',20,"bold"))
    
    titulo1.write('Jugador 1', font=('Century Gothic',25,"bold"), align="center")
    titulo2.write('Jugador 2', font=('Century Gothic',25,"bold"), align="center")
    titulo3.write('Empate', font=('Century Gothic',25,"bold"), align="center", )

LOCK = False



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


def determinar_victoria_2():
    P1 = 1
    P2 = 2

    # Checar la horizontal
    for c in range(COLS-3):
        for r in range(ROWS):
            if board[r][c] == P1 and board[r][c+1] == P1 and board[r][c+2] == P1 and board[r][c+3] == P1:
                return P1
            elif board[r][c] == P2 and board[r][c+1] == P2 and board[r][c+2] == P2 and board[r][c+3] == P2:
                return P2
            
    # Checar la vertical
    for c in range(COLS):
        for r in range(ROWS-3):
            if board[r][c] == P1 and board[r+1][c] == P1 and board[r+2][c] == P1 and board[r+3][c] == P1:
                return P1
            elif board[r][c] == P2 and board[r+1][c] == P2 and board[r+2][c] == P2 and board[r+3][c] == P2:
                return P2
            
    # Checar la diagonal /
    for c in range(COLS-3):
        for r in range(ROWS-3):
            if board[r][c] == P1 and board[r+1][c+1] == P1 and board[r+2][c+2] == P1 and board[r+3][c+3] == P1:
                return P1
            elif board[r][c] == P2 and board[r+1][c+1] == P2 and board[r+2][c+2] == P2 and board[r+3][c+3] == P2:
                return P2

    # Checar la diagonal \
    for c in range(COLS-3):
        for r in range(3, ROWS):
            if board[r][c] == P1 and board[r-1][c+1] == P1 and board[r-2][c+2] == P1 and board[r-3][c+3] == P1:
                return P1
            elif board[r][c] == P2 and board[r-1][c+1] == P2 and board[r-2][c+2] == P2 and board[r-3][c+3] == P2:
                return P2


def restaurar_juego():
    global TURNO
    global board
    TURNO = 1
    board = []

    clear()
    dibujar_tablero()
    make_temp_lines()
    crear_matriz_tablero()



def play(x, y):
    global TURNO
    global LOCK
    
    if not LOCK:
        board_x, board_y = get_coordenadas_tablero(x, y)

        pieza_colocada = poner_pieza(board_x, TURNO)

        if pieza_colocada:
            set_turno(TURNO)

        #victoria = determinar_victoria()
        victoria = determinar_victoria_2()

        if victoria == 1:
            print("El jugador 1 ganó")
            cambiar_marcador(1)
            textinput("¿Continuar?", "Presiona <Enter> para continuar")
            restaurar_juego()
        elif victoria == 2:
            print("El jugador 2 ganó")
            cambiar_marcador(2)
            textinput("¿Continuar?", "Presiona <Enter> para continuar")
            restaurar_juego()


setup(800, 800, 370, 0)
setworldcoordinates(-0.5,-0.5,COLS+0.5,ROWS+2.5)
hideturtle()
tracer(False)
dibujar_tablero()
crear_matriz_tablero()
make_temp_lines()

score1 = turtle.Turtle(visible=False)
score2 = turtle.Turtle(visible=False)
score3 = turtle.Turtle(visible=False)
titulo1 = turtle.Turtle(visible=False)
titulo2 = turtle.Turtle(visible=False)
titulo3 = turtle.Turtle(visible=False)

crear_marcador()
cambiar_marcador(-1)

onscreenclick(play)
   
done()
