class Clientes:
    lista_clientes = []

    def obtener_clientes(self):
        return self.lista_clientes

    def agregar_cliente(self, objeto):
        self.lista_clientes.append(objeto)
    
    def borrar_cliente(self, id_):
        self.lista_clientes.pop(id_)

    def descontar_saldo_cliente(self,id,precio_total):
        for cliente in self.lista_clientes:
            if cliente['id'] == id:
                if cliente['_Cliente__Saldo']>=precio_total:
                    cliente['_Cliente__Saldo']-=precio_total
                else:
                    print(f'El cliente no tiene saldo: {cliente["nombre"]}')
            else:
                print('el cliente no existe en la db')

