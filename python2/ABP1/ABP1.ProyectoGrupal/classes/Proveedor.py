class Proveedor:
    

    def __init__(self,__id,rut,nombre_legal,razon_social,pais='chile'):
        self.__id = __id
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.juridico=True

    
    
    def obtener_proveedor(self):
        return self.__dict__
    
 
            
   