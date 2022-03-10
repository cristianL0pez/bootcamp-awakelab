class Clientes:
    lista_clientes = []

    def obtener_clientes(self):
        return self.lista_clientes

    def agregar_cliente(self, objeto):
        self.lista_clientes.append(objeto)
    
    def borrar_cliente(self, id_):
        self.lista_clientes.pop(id_)

