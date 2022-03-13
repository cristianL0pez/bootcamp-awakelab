class Proveedores:
    lista_proveedores = []

    def obtener_proveedores(self):
        return self.lista_proveedores

    def agregar_proveedor(self, objeto):
        self.lista_proveedores.append(objeto)
    
    def borrar_proveedor(self, id_):
        self.lista_proveedores.pop(id_)

