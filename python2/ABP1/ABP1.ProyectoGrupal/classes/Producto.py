class Producto:

    def __init__(self,SKU,Nombre,Categoría,Proveedor,Stock,Valor_Neto) -> None:
        self.SKU = SKU
        self.Nombre = Nombre
        self.Categoría = Categoría
        self.Proveedor = Proveedor
        self.Stock = Stock
        self.Valor_Neto = Valor_Neto
        self.__Impuesto = 1.19
        
    def obtener_cliente(self):
        return self.__dict__
    

