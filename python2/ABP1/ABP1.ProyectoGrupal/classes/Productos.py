class Productos:
    lista_productos = []

    def obtener_productos(self):
        return self.lista_productos

    def agregar_producto(self, objeto):
        self.lista_productos.append(objeto)
    
    def borrar_producto(self, id_):
        self.lista_productos.pop(id_)

    def descontar_stock_producto(self, SKU,cantidad):
        for producto in self.lista_productos:
            if producto['SKU'] == SKU:
                if producto['stock']>=cantidad:
                    producto['stock']-=cantidad
                else:
                    print(f'Lo sentimos, no hay stock del producto: {producto["nombre"]}')
            else:
                print('ese producto no existe en el inventario!')

                
        

    
