from classes.Producto import Producto
from classes.Cliente import Cliente
from classes.users import User

class Vendedor(User):

    def __init__(self,id,RUN,Nombre,Sección,code_user=123):
        self.__id=id
        self.RUN = RUN
        self.Nombre = Nombre
        self.Sección = Sección
        self.__Comision = 0
        super().__init__(code_user)#herencia desde users con el codigo de usuario

    
    
    def obtener_vendedor(self):
        return self.__dict__


        
    def venta(self):
        cantidad=input('ingrese la cantidad de productos a vender')
        Producto.descontar_producto(cantidad)
        self.__comision(Producto.comision())



        
    



        


    
    
 
        
