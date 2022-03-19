from classes.users import User
class Proveedor(User):
    

    def __init__(self,__id,rut,nombre_legal,razon_social,pais='chile',code_user=123):
        self.__id = __id
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.juridico=True
        super().__init__(code_user)#herencia desde users con el codigo de usuario

    
    
    def obtener_proveedor(self):
        return self.__dict__
    
 
            
   