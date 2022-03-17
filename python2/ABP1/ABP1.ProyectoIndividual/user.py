class Usuarios:

    def __init__(self,_id,nombre,edad,direccion,telefono,tipoUsuario):
        self._id = _id
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.tipoUsuario = tipoUsuario


    def get_user(self):
        return self.__dict__
        