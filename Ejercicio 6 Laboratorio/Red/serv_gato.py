#Esquivel Victoriano Alvaro Jared
import socket
import threading
import math

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 55555))
server.listen()

clients = []
boards = [' ' for _ in range(9)]

def has_won(board, player):
    win_positions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def minimax(board, depth, is_maximizing, alpha, beta):
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
                score = minimax(board, depth + 1, False, alpha, beta)['score']
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return {'score': best_score, 'position': move}

    else:
        best_score = math.inf
        move = None
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True, alpha, beta)['score']
                board[i] = ' '
                if score < best_score:
                    best_score = score
                    move = i
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return {'score': best_score, 'position': move}

def handle_client(client):
    while True:
        if clients.index(client) == 0:
            while True:
                move = client.recv(1024).decode('ascii')
                position = int(move)
                if boards[position] == ' ':
                    boards[position] = 'O'
                    break
                else:
                    client.send('Movimiento inválido. Por favor, intenta de nuevo.'.encode('ascii'))
        else:
            move = minimax(boards, 0, True, -math.inf, math.inf)['position']
            boards[move] = 'X'
        for c in clients:
            c.send(' '.join(boards).encode('ascii'))
        if has_won(boards, 'O'):
            for c in clients:
                c.send('¡Has ganado!'.encode('ascii'))
            break
        elif has_won(boards, 'X'):
            for c in clients:
                c.send('La computadora ha ganado.'.encode('ascii'))
            break
        elif ' ' not in boards:
            for c in clients:
                c.send('Es un empate.'.encode('ascii'))
            break

def start_game():
    while True:
        client, addr = server.accept()
        print(f"Conexión establecida con {addr}!")
        clients.append(client)
        client.send(' '.join(boards).encode('ascii'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print("El servidor está corriendo...")
start_game()
