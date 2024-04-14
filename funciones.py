import Tablero
import numpy as np
import variables as variable
import time 

#Métodos 

#Método que inicia los dos objetos que son los tableros y lso devuelve en una lista al programa princiapal

def newGame():
    tablero=Tablero.Tablero(0,np.full ((variable.dimension_X,variable.dimension_y),' '),
                              np.full((variable.dimension_X,variable.dimension_y),' '),input("Introduce tu nombre jugador:  "),0)
    tablero_pc=Tablero.Tablero(1,np.full ((variable.dimension_X,variable.dimension_y),' '),
                                 np.full((variable.dimension_X,variable.dimension_y),' '),"PC",0)
    #Una vez inicializados posicionamos los barcos en cada tablaero
    posicionar_barcos_cons(tablero_pc)
    posicionar_barcos(tablero)
    return [tablero,tablero_pc]
       
#Posicionar barcos del jugador--> WIP  Todavía no reconoce si te pasas de limite de tablero

def posicionar_barcos(tablero:Tablero):
    print('''
    ****************
    PREPARA TU FLOTA
    ****************
    ''')
    for barco,longitud in variable.barcos.items():
        print(f"Coloca tu {barco} con {longitud} esloras")
        x = int(input("Introduce fila: "))
        y = int(input("Introduce columna: "))
        if longitud == 1:
            tablero.tabla_op[x,y]="O"
            print(tablero.tabla_op)    
        else:
            print("""Define la orientación del barco:
            N) NORTE
            S) SUR
            E) ESTE
            W) OESTE
            """)
            orien = input("Elige una opción: ").upper()
            if orien=="E":
                z =y+longitud
                tablero.tabla_op[x,y:z]="O"
                time.sleep(0.5)
                print(tablero.tabla_op)
            elif orien=="S":
                z = x + longitud
                tablero.tabla_op [x:z,y]="O"
                time.sleep(0.5)
                print(tablero.tabla_op)
            elif orien=="W":
                z =y-longitud
                tablero.tabla_op[x,z+1:y+1]="O"
                time.sleep(0.5)
                print(tablero.tabla_op)
            elif orien=="N":
                z=x-longitud
                tablero.tabla_op[z+1:x+1,y]="O"
                time.sleep(0.5)
                print(tablero.tabla_op)
            else:
                print("Valor no valido")
    return tablero

#Posicionar barcos del PC -----> WIP

def posicionar_barcos_cons(tablero_pc:Tablero):
    
    #En la version 2 hacerlo random con condiciones
    tablero_pc.tabla_op[0,0]="O"
    tablero_pc.tabla_op[5,5]="O"
    tablero_pc.tabla_op[0,7]="O"
    tablero_pc.tabla_op[0,5]="O"
    tablero_pc.tabla_op[1:3,2]="O"
    tablero_pc.tabla_op[5:7,2]="O"
    tablero_pc.tabla_op[3:5,4]="O"
    tablero_pc.tabla_op[6:9,4]="O"
    tablero_pc.tabla_op[1:4,9]="O"
    tablero_pc.tabla_op[9,4:8]="O"
    
    return tablero_pc

#Metodo auxliar que muestra los tableros
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
    
def disparo_jugador(tablero:Tablero, tablero_pc:Tablero):
    print('''
    ****************
    ATACA AL PC
    ****************
    ''')
    while tablero.aciertos!=20:
        print("Introduce las cordenadas y dispara")
        x = int(input("Introduce fila : "))
        y = int(input("Introduce columna: "))
        if tablero_pc.tabla_op[x,y]=='O':
            print('¡Tocado!')
            tablero_pc.tabla_op[x,y]='X'
            tablero_pc.tabla_visible[x,y]='X'
            tablero.aciertos+=1
            print(f"El jugador {tablero.nombre_jugador} lleva {tablero.aciertos} aciertos")
            time.sleep(0.75)
            mostrar_tablero(tablero,tablero_pc)
        else:
            tablero_pc.tabla_op[x,y]='-'
            tablero_pc.tabla_visible[x,y]='-'
            print('¡Agua!')
            time.sleep(0.75)
            mostrar_tablero(tablero,tablero_pc)
            return tablero,tablero_pc

def disparo_pc(tablero:Tablero, tablero_pc:Tablero):
    while tablero_pc.aciertos!=20:
        x = np.random.randint(0,10)
        y = np.random.randint(0,10)
        if tablero.tabla_op[x,y]=='O':
           tablero.tabla_op[x,y]='X'
           tablero_pc.aciertos+=1
           print(f"Tocado,  el ordenador lleva {tablero_pc.aciertos} aciertos")
           time.sleep(0.75)
           mostrar_tablero(tablero,tablero_pc)
        else:
            tablero.tabla_op[x,y]='-'
            print("¡Agua! No te han dado")
            mostrar_tablero(tablero,tablero_pc)
            time.sleep(0.75)
            return tablero,tablero_pc