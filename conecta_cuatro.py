'''
Juego de Conecta Cuatro

Kevin Susej Garza Aragon, A00833985
Eugenia Ruiz Velasco Olvera, A01177887
Christopher Gabriel Pedraza Pohlenz, A01177767
'''

# Se importan las librerías turtle y math
import turtle
from turtle import *
import math as m

# Se inicializan constantes
# Dimensiones de tablero
ROWS = 8
COLS = 10
# Coordenadas para dibujar tablero
inicia_x = 0
inicia_y = 0
fin_x = COLS
fin_y = ROWS

RADIO_FICHAS = 0.4

# Matriz de tablero
board = []

# Turno del jugador
TURNO = 1

# Diccionario de victorias
marcador = {'jugador 1': 0, 'jugador 2': 0, 'empate':0}


# Función para crear el marcador
def crear_marcador():
    # Cambia color
    titulo1.color('crimson')
    titulo2.color('cyan3')
    titulo3.color('purple')
    # Posiciona marcador y títulos
    score1.goto(2,9)
    score2.goto(8,9)
    score3.goto(5,9)
    titulo1.goto(2,9.5)
    titulo2.goto(8,9.5)
    titulo3.goto(5,9.5)


# Función para agregar 1 al marcador
def cambiar_marcador(ganador):
    if ganador == 0:
        marcador['empate'] += 1
    elif ganador == 1:
        marcador['jugador 1'] += 1
    elif ganador == 2:
        marcador['jugador 2'] += 1
    
    # Se borra y se vuelve a escribir el marcador
    score1.clear()
    score2.clear()
    score3.clear()
    # Establecer el tamaño de la letra y tipografía
    score1.write(marcador ['jugador 1'], font=('Century Gothic',20,"bold"))
    score2.write(marcador ['jugador 2'], font=('Century Gothic',20,"bold"))
    score3.write(marcador ['empate'], font=('Century Gothic',20,"bold"))
    titulo1.write('Jugador 1', font=('Century Gothic',25,"bold"), align="center")
    titulo2.write('Jugador 2', font=('Century Gothic',25,"bold"), align="center")
    titulo3.write('Empate', font=('Century Gothic',25,"bold"), align="center", )


# Función que llenar con ceros la matriz del tablero
def crear_matriz_tablero():
    tempRow = []
    # Se recorren las filas y columnas creando una matriz
    for i in range(ROWS):
        for i in range(COLS):
            tempRow.append(0)

        board.append(tempRow)
        tempRow = []


# Función para transformar las coordenadas del click a posición de la matriz
def get_coordenadas_tablero(x, y):
    new_x = m.floor(x)
    new_y = m.floor(y)
    return new_x, new_y


# Función para dibujar un rectángulo con sus debidos parámetros
def rectangulo (ix, iy, fx, fy, _color):
    # Cambia el color del dibujo
    color(_color)
    # Deja de dibujar
    up()
    # Mueve el puntero
    goto(ix,iy)
    # Comienza a dibujar
    down()
    # Emficha a rellenar lo que se dibuja
    begin_fill()
    
    # Dibuja dos lados a la vez
    for count in range(2):
        # Mueve al puntero hacia adelante
        forward(fx)
        # Gira 90 grados hacia la izquierda
        left(90)
        forward(fy)
        left(90)
    # Termina de rellenar lo que se dibuja
    end_fill()
    

# Función que dibuja al tablero
def dibujar_tablero():
    # Se llama a la función que dibuja al rectángulo
    rectangulo(inicia_x, inicia_y, fin_x, fin_y,'light blue')

    color('white')
    # En cada posición del tablero coloca un círculo
    for x in range(COLS):
        for y in range(ROWS):
            up()
            goto(x+0.5,y+(0.5-RADIO_FICHAS))
            down()
            begin_fill()
            # Crea un círculo de radio (radio_fichas) en la circunferencia completa con 150 líneas 
            circle(RADIO_FICHAS, 360, 150)
            end_fill()


# Función para crear las líneas del tablero
def crear_lineas_tablero():
    color('white')
    # Dibuja las líneas verticales
    for i in range(COLS):
        up()
        goto(i+1, 0)
        down()
        goto(i+1, 8)

    # Dibuja las líneas horizontales
    for i in range(ROWS):
        up()
        goto(0, i+1)
        down()
        goto(10, i+1)


# Función para colocar la ficha del jugador
def dibujar_ficha(x, y, jugador):
    # Asignar color dependiendo de turno
    if jugador == 1:
        color('crimson')
    else:
        color('cyan3')

    # Se dibuja ficha
    up()
    goto(x+0.5,y+(0.5-RADIO_FICHAS))
    down()
    begin_fill()
    circle(RADIO_FICHAS, 360, 150)
    end_fill()


# Función que cambia los valores de la matriz del tablero
def poner_ficha(col, jugador):
    ficha_colocada = False

    # Si se encuentra dentro de los límites
    if col >= 0 and col < COLS:
        # Checar la primera posición inferior disponible de la columna
        for position in range(ROWS):
            if board[position][col] == 0:
                # Cambiar valor de matriz y dibujar ficha correpondiente
                board[position][col] = jugador
                dibujar_ficha(col, position, jugador)
                return True
            # Si no encuentra posición disponible, no se coloca ficha
            else:
                ficha_colocada = False

    return ficha_colocada


# Función que mueve indicador de turno
def cambiar_indicador_turno(turno):
    # Quita el marcador
    indicador_turno.clear()
    indicador_turno.up() 

    # Dependiendo del turno, es la posición del marcador
    if turno == 1:
        indicador_turno.goto(1.95, 8.5) 
    else:
        indicador_turno.goto(7.95, 8.5) 

    # Dibuja el marcador en la posición del turno
    indicador_turno.down() 
    indicador_turno.begin_fill()
    
    # Ciclo por cada uno de los 3 lados del triángulo
    for count in range(3):
        # Se mueve una cantidad hacia adelante y gira 120 grados para hacer un triángulo equilatero
        indicador_turno.forward(0.3)
        indicador_turno.left(120)
        
    # Termina de rellenar la figura
    indicador_turno.end_fill()


# Función que cambia la constante de turno
def set_turno(turno):
    global TURNO

    if turno == 1:
        TURNO = 2
    else:
        TURNO = 1
    
    # Llama a la función para mover el indicador de turno
    cambiar_indicador_turno(TURNO)


# Función que determina la victoria del juego
def determinar_victoria():
    P1 = 1
    P2 = 2

    # Determinar victoria horizontal
    # Se le quitan 3 posiciones a la columna para poder hacer el análisis de la secuendia de izquierda a derecha
    # y revisar esa posición y las tres siguientes
    for c in range(COLS-3):
        for r in range(ROWS):
            if board[r][c] == P1 and board[r][c+1] == P1 and board[r][c+2] == P1 and board[r][c+3] == P1:
                return P1
            elif board[r][c] == P2 and board[r][c+1] == P2 and board[r][c+2] == P2 and board[r][c+3] == P2:
                return P2
            
    # Determinar victoria vertical
    for c in range(COLS):
        # Se le quitan 3 posiciones a las filas para poder hacer el análisis de la secuendia de abajo para arriba
        # y revisar esa posición y las tres siguientes
        for r in range(ROWS-3):
            if board[r][c] == P1 and board[r+1][c] == P1 and board[r+2][c] == P1 and board[r+3][c] == P1:
                return P1
            elif board[r][c] == P2 and board[r+1][c] == P2 and board[r+2][c] == P2 and board[r+3][c] == P2:
                return P2
            
    # Determinar victoria diagonal /
    for c in range(COLS-3):
        for r in range(ROWS-3):
            if board[r][c] == P1 and board[r+1][c+1] == P1 and board[r+2][c+2] == P1 and board[r+3][c+3] == P1:
                return P1
            elif board[r][c] == P2 and board[r+1][c+1] == P2 and board[r+2][c+2] == P2 and board[r+3][c+3] == P2:
                return P2

    # Determinar victoria diagonal \
    for c in range(COLS-3):
        # Comienza en la posición 3, ya que es la posición mínima que se requiere para completar la secuencia de 4 fichas
        # de la diagonal negativa
        for r in range(3, ROWS):
            if board[r][c] == P1 and board[r-1][c+1] == P1 and board[r-2][c+2] == P1 and board[r-3][c+3] == P1:
                return P1
            elif board[r][c] == P2 and board[r-1][c+1] == P2 and board[r-2][c+2] == P2 and board[r-3][c+3] == P2:
                return P2


# Función para checar si el tablero está lleno
def tablero_lleno():
    for row in board:
        for col in row:
            # Si encuentra una posición vacía, el tablero aún no está lleno
            if col == 0:
                return False
    # Si se recorrió todo el tablero, y no encontró posición vacía, si está lleno    
    return True


# Función para restaurar el juego cuando un jugador gana
def restaurar_juego():
    global TURNO
    global board
    TURNO = 1
    board = []

    clear()
    dibujar_tablero()
    crear_lineas_tablero()
    crear_matriz_tablero()
    cambiar_indicador_turno(1)


# Función que se llama cada vez que se da un click en la pantalla.
# Recibe: las coordenadas del click
def play(x, y):
    global TURNO
    
    # Convierte las coordenadas a posición de matriz
    board_x, board_y = get_coordenadas_tablero(x, y)

    # Intenta colocar una ficha y guarda si este movimiento fue exitoso o no
    ficha_colocada = poner_ficha(board_x, TURNO)

    # Si fue exitoso, cambia el turno
    if ficha_colocada:
        set_turno(TURNO)

    # Determinan la victoria y si el tablero está lleno
    victoria = determinar_victoria()
    lleno = tablero_lleno()

    # Dependiendo de los resultados anteriores, determinar al ganador
    if victoria == 1:
        print("El jugador 1 ganó")
        # Agrega uno al marcador de este jugador
        cambiar_marcador(1)
        # Pregunta si desea continuar jugando
        textinput("¿Continuar?", "Presiona <Enter> para continuar")
        # Llama a la función para restaurar constantes y tablero
        restaurar_juego()
    elif victoria == 2:
        print("El jugador 2 ganó")
        cambiar_marcador(2)
        textinput("¿Continuar?", "Presiona <Enter> para continuar")
        restaurar_juego()
    elif lleno:
        print("Empate")
        cambiar_marcador(0)
        textinput("¿Continuar?", "Presiona <Enter> para continuar")
        restaurar_juego()


# Establecer el ancho, largo, y posición inicial en x y y
setup(800, 800, 370, 0)
# Cambia las coordenadas relativas de la venta
setworldcoordinates(-0.5,-0.5,COLS+0.5,ROWS+2.5)
# Esconder el cursor, la tortuga
hideturtle()
# Elimina la animación de la tortuga
tracer(False)

# Crear los marcadores y sus títulos
score1 = turtle.Turtle(visible=False)
score2 = turtle.Turtle(visible=False)
score3 = turtle.Turtle(visible=False)
titulo1 = turtle.Turtle(visible=False)
titulo2 = turtle.Turtle(visible=False)
titulo3 = turtle.Turtle(visible=False)

# Crea el indicador de turno
indicador_turno = turtle.Turtle(visible=False)

# Configura los marcadores
crear_marcador()
# Inicializa los marcadores en cero
cambiar_marcador(-1)
# Dibuja el tablero y posiciona al indicador
restaurar_juego()

# Al haber un click en la pantalla, se llama a esta función, pasando las coordenadas del click
onscreenclick(play)

# Comienza el ciclo de eventos
done()