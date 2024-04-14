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
        fun.jugar(lista_tableros[0],lista_tableros[1])
    elif entrada.upper() =="X":
            break
    else:
        continue
    
        