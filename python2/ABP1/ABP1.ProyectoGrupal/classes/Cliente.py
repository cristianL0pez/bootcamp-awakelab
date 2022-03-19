from classes.users import User
#aca solo se genera la clase suficiente para poder instanciar  un cliente
class Cliente(User):
    

    def __init__(self,__id,nombre,correo,Fecha_Registro,__Saldo,code_user=123):
        self.__id = __id
        self.nombre = nombre
        self.correo = correo
        self.Fecha_Registro = Fecha_Registro
        self.__Saldo = __Saldo
        super().__init__(code_user)#herencia desde users con el codigo de usuario

    
    
    def obtener_cliente(self):
        return self.__dict__


    
   



    
 
            
    
      
    
        
   



        



