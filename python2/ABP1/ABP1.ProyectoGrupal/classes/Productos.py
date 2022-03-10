class Productos:
    lista_productos = []

    def obtener_clientes(self):
        return self.lista_productos

    def agregar_cliente(self, objeto):
        self.lista_productos.append(objeto)
    
    def borrar_cliente(self, id_):
        self.lista_productos.pop(id_)
