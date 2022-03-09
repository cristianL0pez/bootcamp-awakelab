class Clientes:
    
    def __init__(self,_id,nombre,correo,Fecha_Registro,__Saldo):
        self._id = _id
        self.nombre = nombre
        self.correo = correo
        self.Fecha_Registro = Fecha_Registro
        self.__Saldo = __Saldo
       

    
        


    def mostrar_saldo(self):
        print('el saldo es: ')

   
    def agregar_saldo(self):
        print('saldo agregado')
    
    def mostrar_clientes(self):
        print(f"el nombre de cliente es: ",self.nombre,"   su correo es: ",self.correo,"  y se registir en ",self.Fecha_Registro)
        

    