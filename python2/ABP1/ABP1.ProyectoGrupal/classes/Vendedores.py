class Vendedores:
    lista_vendedores = []

    def obtener_clientes(self):
        return self.lista_vendedores

    def agregar_cliente(self, objeto):
        self.lista_vendedores.append(objeto)
    
    def borrar_cliente(self, id_):
        self.lista_vendedores.pop(id_)

