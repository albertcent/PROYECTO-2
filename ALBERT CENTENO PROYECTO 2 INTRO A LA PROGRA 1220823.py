# Albert Centeno 1220823
# Proyecto Final 2 Laboratorio de programación sec 17
# 13/11/2023
# Objetivo: Crear un juego de batalla naval de 2 jugadores
class Tablero:
    def __init__(self):
        self.tablero = [['O' for _ in range(10)] for _ in range(10)]

    def mostrar_tablero(self, ocultar_barcos=False):
        # Aqui se imprimio el tablero
        print("  1 2 3 4 5 6 7 8 9 10")
        for i, fila in enumerate(self.tablero):
            print(chr(65 + i) + " ", end="")
            for casilla in fila:
                if ocultar_barcos and casilla == 'B':
                    print('O', end=" ")
                else:
                    print(casilla, end=" ")
            print()

    def colocar_barco(self, fila, columna, orientacion, tamaño):
        # Aqui se coloca el barco en el tablero
        if orientacion == 'horizontal':
            for i in range(tamaño):
                self.tablero[fila][columna + i] = 'B'
        elif orientacion == 'vertical':
            for i in range(tamaño):
                self.tablero[fila + i][columna] = 'B'


class Jugador:
    def __init__(self, nombre):
        # Se inicia con los atributos
        self.nombre = nombre
        self.barcos_hundidos = 0
        self.puntuacion = 0

    def disparar(self, tablero, fila, columna):
        # Comprobacion si se alcanza el barco o no
        if tablero.tablero[fila][columna] == 'B':
            # Marca que demuestra que se alcanzo el barco
            tablero.tablero[fila][columna] = 'X'
            print(f"¡Has alcanzado un barco, {self.nombre}!")
            self.puntuacion += 1
            return True
        else:
            tablero.tablero[fila][columna] = '*'
            print("Disparo fallido.")
            return False


def validar_coordenada(coordenada):
    if len(coordenada) != 2 or not (65 <= ord(coordenada[0]) <= 74) or not (1 <= int(coordenada[1]) <= 10):
        return False
    return True


def main():
    print("¡Bienvenidos al siguiente juego llamado: Batalla Naval!")
    jugador1_nombre = input("Ingrese el nombre del Jugador 1: ")
    jugador2_nombre = input("Ingrese el nombre del Jugador 2: ")

    tablero_jugador1 = Tablero()
    tablero_jugador2 = Tablero()

    jugador1 = Jugador(jugador1_nombre)
    jugador2 = Jugador(jugador2_nombre)

    # Jugador 1 coloca barcos
    print(f"{jugador1.nombre}, coloca tus barcos:")
    tablero_jugador1.mostrar_tablero(ocultar_barcos=True)
    for _ in range(3):
        while True:
            coordenada = input("Ingrese la coordenada para el barco pequeño (por ejemplo, A1): ").upper()
            if validar_coordenada(coordenada):
                fila = ord(coordenada[0]) - 65
                columna = int(coordenada[1]) - 1
                orientacion = input("Ingrese la orientación del barco (horizontal o vertical): ").lower()
                if orientacion == 'horizontal' or orientacion == 'vertical':
                    if tablero_jugador1.tablero[fila][columna] == 'O':
                        tablero_jugador1.colocar_barco(fila, columna, orientacion, 3)
                        break
                    else:
                        print("¡Ya hay un barco en esa posición! Inténtalo de nuevo.")
                else:
                    print("Orientación inválida. Inténtalo de nuevo.")
            else:
                print("Coordenada inválida. Inténtalo de nuevo.")

    for _ in range(2):
        while True:
            coordenada = input("Ingrese la coordenada para el barco grande (por ejemplo, A1): ").upper()
            if validar_coordenada(coordenada):
                fila = ord(coordenada[0]) - 65
                columna = int(coordenada[1]) - 1
                orientacion = input("Ingrese la orientación del barco (horizontal o vertical): ").lower()
                if orientacion == 'horizontal' or orientacion == 'vertical':
                    if tablero_jugador1.tablero[fila][columna] == 'O':
                        tablero_jugador1.colocar_barco(fila, columna, orientacion, 5)
                        break
                    else:
                        print("¡Ya hay un barco en esa posición! Inténtalo de nuevo.")
                else:
                    print("Orientación inválida. Inténtalo de nuevo.")
            else:
                print("Coordenada inválida. Inténtalo de nuevo.")

    # Jugador 2 coloca barcos
    print(f"{jugador2.nombre}, coloca tus barcos:")
    tablero_jugador2.mostrar_tablero(ocultar_barcos=True)
    for _ in range(3):
        while True:
            coordenada = input("Ingrese la coordenada para el barco pequeño (por ejemplo, A1): ").upper()
            if validar_coordenada(coordenada):
                fila = ord(coordenada[0]) - 65
                columna = int(coordenada[1]) - 1
                orientacion = input("Ingrese la orientación del barco (horizontal o vertical): ").lower()
                if orientacion == 'horizontal' or orientacion == 'vertical':
                    if tablero_jugador2.tablero[fila][columna] == 'O':
                        tablero_jugador2.colocar_barco(fila, columna, orientacion, 3)
                        break
                    else:
                        print("¡Ya hay un barco en esa posición! Inténtalo de nuevo.")
                else:
                    print("Orientación inválida. Inténtalo de nuevo.")
            else:
                print("Coordenada inválida. Inténtalo de nuevo.")

    for _ in range(2):
        while True:
            coordenada = input("Ingrese la coordenada para el barco grande (por ejemplo, A1): ").upper()
            if validar_coordenada(coordenada):
                fila = ord(coordenada[0]) - 65
                columna = int(coordenada[1]) - 1
                orientacion = input("Ingrese la orientación del barco (horizontal o vertical): ").lower()
                if orientacion == 'horizontal' or orientacion == 'vertical':
                    if tablero_jugador2.tablero[fila][columna] == 'O':
                        tablero_jugador2.colocar_barco(fila, columna, orientacion, 5)
                        break
                    else:
                        print("¡Ya hay un barco en esa posición! Inténtalo de nuevo.")
                else:
                    print("Orientación inválida. Inténtalo de nuevo.")
            else:
                print("Coordenada inválida. Inténtalo de nuevo.")

    # Distribucion de los turnos
    turno = 1
    while True:
        if turno % 2 != 0:
            print(f"\nTurno de {jugador1.nombre}")
            tablero_jugador2.mostrar_tablero()
            coordenada = input("Ingrese la coordenada para disparar (por ejemplo, A1): ").upper()
            if validar_coordenada(coordenada):
                fila = ord(coordenada[0]) - 65
                columna = int(coordenada[1]) - 1
                if not jugador1.disparar(tablero_jugador2, fila, columna):
                    turno += 1
        else:
            print(f"\nTurno de {jugador2.nombre}")
            tablero_jugador1.mostrar_tablero()
            coordenada = input("Ingrese la coordenada para disparar (por ejemplo, A1): ").upper()
            if validar_coordenada(coordenada):
                fila = ord(coordenada[0]) - 65
                columna = int(coordenada[1]) - 1
                if not jugador2.disparar(tablero_jugador1, fila, columna):
                    turno += 1

        # Verificar si hay un ganador
        if jugador1.puntuacion == 5:
            print(f"{jugador1.nombre} ha ganado.")
            break
        elif jugador2.puntuacion == 5:
            print(f"{jugador2.nombre} ha ganado.")
            break

if __name__ == "__main__":
    main()

