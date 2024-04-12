import numpy as np

#Con esta clasa podremos clear los tableros del usuario y de la máquina

class Tablero():
    def __init__(self,id_user:int,tabla_op:np.array,tabla_visible:np.array,nombre_jugador:str):
        self.id_user=id_user
        self.tabla_op=tabla_op
        self.tabla_visible=tabla_visible
        self.nombre_jugador=nombre_jugador

