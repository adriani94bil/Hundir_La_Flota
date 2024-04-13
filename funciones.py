import Tablero
import numpy as np
import variables as variable
import time 

#Métodos 

#Método iniciar los dos objetos que son los tableros

def newGame():
    tablero=Tablero.Tablero(0,np.full ((variable.dimension_X,variable.dimension_y),' '),
                              np.full((variable.dimension_X,variable.dimension_y),'#'),input("Introduce tu nombre jugador:  "),0)
    tablero_pc=Tablero.Tablero(1,np.full ((variable.dimension_X,variable.dimension_y),' '),
                                 np.full((variable.dimension_X,variable.dimension_y),'#'),"PC",0)
    #Una vez inicializados posicionamos los barcos en cada tablaero
    posicionar_barcos_cons(tablero_pc)
    posicionar_barcos(tablero)
    #Play(tablero, tablero_pc)

def Play(user,tablero, tablero_pc, contador, contador_pc):
    mostrar_tablero(user,tablero, tablero_pc)
    #batalla_ataque(tablero_pc, contador)
    #batalla_defensa(tablero, contador_pc)
    if contador==100:
        print("""
        ****************************
        ¡ENHORABUENA!¡FLOTA HUNDIDA!
        ****************************
        """)
    elif contador_pc == 100:
        print("""
        ****************************
        ¡UY!¡TU FLOTA SE HA HUNDIDO!
        ****************************
        """)
    else:
        Play(user,tablero, tablero_pc, contador, contador_pc)
        
#Posicionar barcos del jugador--> WIP

def posicionar_barcos(tablero:Tablero):
    print('''
    ****************
    PREPARA TU FLOTA
    ****************
    ''')
    for barco,longitud in variable.barcos.items():
        print(f"Coloca tu {barco} con {longitud} esloras")
        x = int(input("Introduce coordenada x (horizontal): "))
        y = int(input("y ahora coordenada y (vertical): "))
        if longitud == 1:
            tablero.tabla_op[y,x] = 'O'
            print(tablero.tabla_op)    
        else:
            print("""Define la orientación del barco:
            V) Vertical
            H) Horizontal
            """)
            orien = input("Elige una opción: ").upper()
            if orien=="V":
                z =y+longitud
                tablero.tabla_op[y:z,x]="O"
                print(tablero.tabla_op)
            elif orien=="H": 
                z = x + longitud
                tablero.tabla_op [y,x:z]="O"
                print(tablero.tabla_op)
            else:
                print("Valor no valido")
    return tablero

#Posicionar barcos del PC -----> WIP

def posicionar_barcos_cons(tablero_pc:Tablero):
    
    #En la version 2 hacerlo random con condiciones
    tablero_pc.tabla_op[0,1] = 'O'
    tablero_pc.tabla_op[5,5] = 'O'
    tablero_pc.tabla_op[0,7] = 'O'
    tablero_pc.tabla_op[0,5] = 'O'
    tablero_pc.tabla_op[1:3,2] = 'O'
    tablero_pc.tabla_op[5:7,2] = 'O'
    tablero_pc.tabla_op[3:5,4] = 'O'
    tablero_pc.tabla_op[6:9,4] = 'O'
    tablero_pc.tabla_op[1:4,9] = 'O'
    tablero_pc.tabla_op[9,4:8] = 'O'
    
    return tablero_pc


def mostrar_tablero(tablero:Tablero,tablero_pc:Tablero):
    print(f"""
    * * * * * {tablero.get_nombre_jugador()} * * * * *
    """)
    print(tablero.tabla_op)
    
    #OJO, no mostrar la tabla de operaciones del pc, solo la de visibilidad
    print("""
          * * * * * PC * * * * *
    """)
    print(tablero_pc.tabla_visible)