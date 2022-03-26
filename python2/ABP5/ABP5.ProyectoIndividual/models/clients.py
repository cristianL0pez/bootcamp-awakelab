
class Clients:
    _clients = []

    def get_clients(self):
        return self._clients

    def load_data(self, data):
        for d in data:
            self._clients.append(d)

    def add_client(self, data):
        self._clients.append(data)
    
    def remove_client(self, id_):
        self._clients.pop(id_)
