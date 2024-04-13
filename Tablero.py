import numpy as np

#Con esta clasa podremos clear los tableros del usuario y de la máquina

class Tablero():
    def __init__(self,id_user:int,tabla_op:np.array,tabla_visible:np.array,nombre_jugador:str,aciertos:int):
        self.id_user=id_user
        self.tabla_op=tabla_op
        self.tabla_visible=tabla_visible
        self.nombre_jugador=nombre_jugador
        self.aciertos=aciertos
        
#Getters y Setters
    def get_tablaOp(self):
        return self.tabla_op
    
    def get_tablavisible(self):
        return self.tabla_visible
    def get_id_user(self):
        return self.id_user
    def get_nombre_jugador(self):
        return self.nombre_jugador
    def get_aciertos_jugador(self):
        return self.aciertos
    #Los setter los centro en las tablas donde haremos las operaciones y los aciertos del jugador
    
    def set_TablaOp(self,tabla_op_mod:np.array):
        self.tabla_op=tabla_op_mod
    def set_TablaVisible(self,tabla_visi_mod:np.array):
        self.tabla_visible=tabla_visi_mod
    def set_aciertos(self,aciertos:int):
        self.aciertos=aciertos
    

