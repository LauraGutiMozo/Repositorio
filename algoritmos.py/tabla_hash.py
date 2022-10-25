class TablaHash:
    def __init__ (self, tamaño_tabla:int, cargar_factor:int |None =None, cargar.limite:float |None ==None,)->None:
        self.tamaño_tabla_Hash = tamaño_tabla
        self.valores = [None]*self.tamaño_tabla

        
