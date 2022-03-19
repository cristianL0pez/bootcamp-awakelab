from classes.Proveedor import Proveedor

class Producto:

    def __init__(self,SKU,nombre,categoria,stock,valor_neto,*args):
        self.proveedor = Proveedor(*args) ##aqui se instancia de proveedor usando composicion
        self.SKU = SKU
        self.nombre = nombre
        self.categoria = categoria
        self.stock = stock
        self.valor_Neto = valor_neto
        self.__Impuesto = 1.19

    @classmethod
    def descontar_producto(self,cantidad):
         return self.stock - cantidad
          
    @classmethod
    def sumar_producto(self,cantidad):
         return self.stock + cantidad
        
        
        
    def obtener_producto(self):
        prov,*resto = self.__dict__.values()
        proveedor=self.obtener_proveedor_producto()# en esta linea se hace uso de la agregacion.
        return {'SKU':resto[0],
        'nombre':resto[1],
        'categoria':resto[2],
        'stock':resto[3],
        'valor neto':resto[4],
        'rut_proveedor':proveedor['rut'],
        'proveedor':proveedor['razon_social']}


    def obtener_proveedor_producto(self):
        return self.proveedor.obtener_proveedor()


    def comision(self):
        comision = self.valor_neto * 0.5
        
        

        