import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 55555))

def draw_board(board):
    for i in range(3):
        print("|", board[3*i], "|", board[3*i + 1], "|", board[3*i + 2], "|")
        if i < 2:
            print("-------------")

def receive_moves():
    while True:
        message = client.recv(1024).decode('ascii')
        if message in ['¡Has ganado!', 'La computadora ha ganado.', 'Es un empate.']:
            print(message)
            break
        elif message == 'Movimiento inválido. Por favor, intenta de nuevo.':
            print(message)
        else:
            boards = message.split(' ')
            draw_board(boards)

def start_game():
    thread = threading.Thread(target=receive_moves)
    thread.start()
    while True:
        move = input("Ingresa tu movimiento (1-9): ")
        client.send(move.encode('ascii'))

print("Conectado al servidor!")
start_game()
