class Vendedor:

    def __init__(self,id,RUN,Nombre,Sección):
        self.__id=id
        self.RUN = RUN
        self.Nombre = Nombre
        self.Sección = Sección
        self.__Comision = 0

    
    
    def obtener_vendedor(self):
        return self.__dict__
    
 
        
