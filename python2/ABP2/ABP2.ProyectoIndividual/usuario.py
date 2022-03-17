class usuarios(object):
    def __init__(self, identificacion, nombre, apellido):
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
   
#crear validaciones correspondientes en esta clase 
    def get_user(self):
       return self.__dict__