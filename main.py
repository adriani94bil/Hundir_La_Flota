import Tablero as tabla
import numpy as np
import variables as variable
import time 
import funciones as fun

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
        fun.newGame()
        fun.Play()
    elif entrada.upper() =="X":
            break
    else:
        continue
    
        