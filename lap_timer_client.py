# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer


def main():
    # TODO: Pedir el nombre del archivo al usuario usando input()
    filename = input("Ingrese el nombre del archivo con los tiempos de vuelta: ")
    # TODO: Abrir el archivo y leer el numero de vueltas n
    f = open(filename)
    n = int(f.readline())
    # TODO: Crear el cronometro usando lap_timer.init(n)
    timer = lap_timer.init(n)
    # TODO: Leer los n tiempos de vuelta y agregarlos con lap_timer.add_lap()
    for i in range(n):
        tiempo = float(f.readline())
        lap_timer.add_lap(timer, tiempo)
    f.close()
    # TODO: Imprimir la racha decreciente mas larga
    #       usando lap_timer.longest_decreasing_streak()
    print(lap_timer.longest_decreasing_streak(timer))
    
    


if __name__ == "__main__":
    main()
