#Esquivel Victoriano Alvaro Jared
import math

board = [' ' for _ in range(9)] # Inicializamos el tablero

# Función para dibujar el tablero de juego
def draw_board(board):
    for i in range(3):
        print("|", board[3*i], "|", board[3*i + 1], "|", board[3*i + 2], "|")
        if i < 2:
            print("-------------")

# Función para realizar el movimiento del jugador
def player_move(board):
    while True:
        position = int(input("Ingresa tu movimiento (1-9): ")) - 1
        if board[position] == ' ':
            board[position] = 'O'
            break
        else:
            print("Movimiento inválido. Por favor, intenta de nuevo.")

# Función para verificar si alguien ha ganado
def has_won(board, player):
    win_positions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# Implementación del algoritmo Minimax
def minimax(board, depth, is_maximizing):
    if has_won(board, 'X'):
        return {'score': 1, 'position': None}
    elif has_won(board, 'O'):
        return {'score': -1, 'position': None}
    elif ' ' not in board:
        return {'score': 0, 'position': None}

    if is_maximizing:
        best_score = -math.inf
        move = None
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)['score']
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i
        return {'score': best_score, 'position': move}

    else:
        best_score = math.inf
        move = None
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)['score']
                board[i] = ' '
                if score < best_score:
                    best_score = score
                    move = i
        return {'score': best_score, 'position': move}

# Función para realizar el movimiento de la computadora
def computer_move(board):
    move = minimax(board, 0, True)['position']
    board[move] = 'X'

# Juego principal
while True:
    draw_board(board)
    if has_won(board, 'O'):
        print("¡Has ganado!")
        break
    elif has_won(board, 'X'):
        print("La computadora ha ganado.")
        break
    elif ' ' not in board:
        print("Es un empate.")
        break
    player_move(board)
    if ' ' not in board:
        print("Es un empate.")
        break
    computer_move(board)
