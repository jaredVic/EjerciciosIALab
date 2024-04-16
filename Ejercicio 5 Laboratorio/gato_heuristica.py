#Esquivel Victoriano Alvaro Jared
import random

def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
    print("")

def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if all(posicion == jugador for posicion in fila):
            return True
    # Verificar columnas
    for columna in range(3):
        if all(tablero[fila][columna] == jugador for fila in range(3)):
            return True
    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)):
        return True
    return False

def movimiento_valido(fila, columna, tablero):
    return 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == " "

def generar_movimientos(tablero):
    movimientos = []
    for fila in range(3):
        for columna in range(3):
            if movimiento_valido(fila, columna, tablero):
                movimientos.append((fila, columna))
    return movimientos

def estado_del_juego(tablero):
    if verificar_ganador(tablero, "X"):
        return "Humano"
    elif verificar_ganador(tablero, "O"):
        return "Computadora"
    elif all(" " not in fila for fila in tablero):
        return "Empate"
    else:
        return "En juego"

def jugar():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador = "X"
    maquina = "O"
    while True:
        imprimir_tablero(tablero)
        fila = int(input("Ingrese la fila (0, 1, 2): "))
        columna = int(input("Ingrese la columna (0, 1, 2): "))
        if movimiento_valido(fila, columna, tablero):
            tablero[fila][columna] = jugador
            print("Movimientos posibles: ", generar_movimientos(tablero))
            estado = estado_del_juego(tablero)
            print("Estado del juego: ", estado)  # Imprimir el estado del juego
            if estado == "Humano":
                imprimir_tablero(tablero)
                print("¡Felicidades! ¡Has ganado!")
                break
            elif estado == "Empate":
                imprimir_tablero(tablero)
                print("¡Es un empate!")
                break
            else:
                print("Tu movimiento:")
                imprimir_tablero(tablero)
                print("Turno de la máquina:")
                # Movimiento aleatorio de la máquina
                while True:
                    fila_maquina = random.randint(0, 2)
                    columna_maquina = random.randint(0, 2)
                    if movimiento_valido(fila_maquina, columna_maquina, tablero):
                        tablero[fila_maquina][columna_maquina] = maquina
                        print("Movimientos posibles: ", generar_movimientos(tablero))
                        estado = estado_del_juego(tablero)
                        print("Estado del juego: ", estado)  # Imprimir el estado del juego
                        if estado == "Computadora":
                            imprimir_tablero(tablero)
                            print("¡La máquina ha ganado!")
                            break
                        break
        else:
            print("Movimiento inválido. Inténtelo de nuevo.")

if __name__ == "__main__":
    jugar()
