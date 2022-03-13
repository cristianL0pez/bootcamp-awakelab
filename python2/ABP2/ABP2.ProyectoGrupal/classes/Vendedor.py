from classes.Producto import Producto
from classes.Cliente import Cliente

class Vendedor:

    def __init__(self,id,RUN,Nombre,Sección):
        self.__id=id
        self.RUN = RUN
        self.Nombre = Nombre
        self.Sección = Sección
        self.__Comision = 0

    
    
    def obtener_vendedor(self):
        return self.__dict__


    @classmethod    
    def venta(self):
        id_cliente=input('ingrese el id del cliente! ')
        id_producto=input('ingrese el id del producto! ')
        cantidad=input('ingrese la cantidad de productos a vender')
        Producto.descontar_producto(cantidad)
        
    



        


    
    
 
        
