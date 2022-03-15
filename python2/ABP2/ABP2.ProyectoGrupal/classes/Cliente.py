


class Cliente:
    lista_clientes = []
    


    def __init__(self,__id,nombre,correo,Fecha_Registro,__Saldo):
        self.__id = __id
        self.nombre = nombre
        self.correo = correo
        self.Fecha_Registro = Fecha_Registro
        self.__Saldo = __Saldo
        
        

        
  
        
        

    
    def guardar_lista_cliente(self):
        for cliente in Cliente.lista_clientes:
            print(cliente)

        



    def obtener_cliente(self):
        return self.__dict__

    

cliente1=Cliente('adjakshld','adjakshld','adjakshld','adjakshld','adjakshld',)
cliente1.guardar_lista_cliente()

 
            
    
      
    
        
   



        



