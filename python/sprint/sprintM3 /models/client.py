class Client:

    def __init__(self, _id, name, last, age, passw):
        self.id = _id
        self.name = name
        self.last = last
        self.age = age
        self.passw = passw
        self.cart = []
    
    def get_client(self):
        return self.__dict__
    
    def add_cart(self, item):
        self.cart.append(item)