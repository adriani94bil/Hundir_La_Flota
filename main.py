import Tablero as tabla
import numpy as np
import variables as variable
import time 
import funciones as fun
import os

#Zona ciclo while Juego

while True:
    print("""
    ****************
    HUNDIR LA FLOTA
    ****************
    S) START
    X) SALIR DEL JUEGO
    """)
    entrada = input("Elige una opción: ")
    if entrada.upper() =="S":
        lista_tableros=fun.newGame()
        fun.mostrar_tablero(lista_tableros[0],lista_tableros[1])
        #Ciclo while para no parar de disparar hasta que los aciertos lleggen al objetivo
        while lista_tableros[0].aciertos!=20 and lista_tableros[1].aciertos!=20:
            if lista_tableros[0].aciertos!=20 and lista_tableros[0].aciertos!=20:
                fun.disparo_jugador(lista_tableros[0],lista_tableros[1])
            if lista_tableros[0].aciertos==20:
                print("""
                ****************************
                ¡ENHORABUENA!¡HAS HUNDIDO LA FLOTA ENEMIGA!
                *******
                *********************
                """)
                break
            if lista_tableros[1].aciertos!=20 and lista_tableros[0].aciertos!=20:
                fun.disparo_pc(lista_tableros[0],lista_tableros[1])
            if lista_tableros[1].aciertos==20:
                print("""
                ****************************
                ¡HAN HUNDIDO TU FLOTA!
                GAME OVER
                ****************************
                """)
                break
    elif entrada.upper() =="X":
        break
    else:
        continue
    
        