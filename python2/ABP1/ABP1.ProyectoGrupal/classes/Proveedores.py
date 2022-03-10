class Proveedores:
    lista_proveedores = []

    def obtener_clientes(self):
        return self.lista_proveedores

    def agregar_cliente(self, objeto):
        self.lista_proveedores.append(objeto)
    
    def borrar_cliente(self, id_):
        self.lista_proveedores.pop(id_)

