





class Cliente:
    lista_clientes=[]    


    def __init__(self,__id,nombre,correo,Fecha_Registro,__Saldo,):
        self.__id = __id
        self.nombre = nombre
        self.correo = correo
        self.Fecha_Registro = Fecha_Registro
        self.__Saldo = __Saldo
        
        
    def obtener_cliente(self):
        return self.__dict__
    
    def guardar_lista_cliente(self):
         Cliente.lista_clientes.append(self.__dict__)

    
         

cliente1=Cliente('adjakshld','adjakshld','adjakshld','adjakshld','adjakshld')
print(cliente1.obtener_cliente())
cliente1.guardar_lista_cliente()
print( Cliente.lista_clientes)

 
            
    
      
    
        
   



        



