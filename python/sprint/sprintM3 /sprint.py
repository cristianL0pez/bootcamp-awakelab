# importar archivos o modulos necesarios
from models.client import Client
from models.clients import Clients
from models.products import *
from models.envio import *
from services import users
from helpers import inquirer, uuid_generator


def opt_value(value, name='opcion'):
    # Recibe un valor de un diccionario y lo transforma a minuscula. Para ocupar con inquirer
    opcion = value[name].lower()
    return opcion


def run():
    # funcion principal
    clients_db = users.get()
    clients = Clients()
    if clients_db:
        clients.load_data(clients_db)
    opt = ''
    while opt != 'salir':
        opt = opt_value(inquirer.inquirer_menu())
        if opt == 'bodega':
             otp_bodega = inquirer.product_menu()['opcion']
             if otp_bodega == opcion_bodega1:
                 agregar_productos()
             elif otp_bodega == opcion_bodega2:
                 sum_producto()
                 mostrar_productos()
             elif otp_bodega == opcion_bodega3:
                 res_producto()
                 mostrar_productos()
             elif otp_bodega == opcion_bodega4:
                 mostrar_productos_sleep()
                
        elif opt == 'clientes':
            opt_clients = opt_value(inquirer.customer_menu())
            if opt_clients == 'agregar cliente':
                client_ = inquirer.add_client()
                client_ = Client(uuid_generator.create(8), client_['name'], client_['last'], client_['age'], client_['pass'])
                clients.add_client(client_.get_client())
                users.post(clients.get_clients())
                print(f'Se agrego un nuevo cliente con los datos: \n {client_.get_client()}')
            elif opt_clients == 'eliminar cliente':
                name_delete = inquirer.list_client_to_delete(clients.get_clients())['clientes']
                item = [client for client in clients.get_clients() if (f"{client['name']} {client['last']}") == name_delete][0]
                index = clients.get_clients().index(item)
                inquirer.confirm_remove_client()
                clients.remove_client(index)
                users.post(clients.get_clients())
            elif opt_clients == 'mostrar clientes':
                for client in clients.get_clients():
                    print(client)

        elif opt == 'envio':
            print(f'Elegiste el menu {opt}')
            otp_envio = inquirer.envio_menu()['opcion']
            if otp_envio =='1. rapido':
                print('elegiste envio rapido para distancias  menores a 1000 km ')
                envios()
            elif otp_envio == "2. largo":
                print('elegiste envio largo para distancias  mayores a 1000 km ')
                envios()


        else:
            print('Nos vemos')
        if opt != 'salir':
            inquirer.pause();


if __name__ == '__main__':
    run()