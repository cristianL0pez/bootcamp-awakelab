import uuid
from datetime import datetime
from classes.Cliente import *
from classes.Clientes import *
from classes.Producto import *
from classes.Productos import *
from classes.Vendedor import *
from classes.Vendedores import *

##########################################################################################################
#                                 controller  clase cliente                                              #
##########################################################################################################

def pedir_datos_cliente():
    id = uuid.uuid4()
    id = str(id)
    id = id[1:8]
    print('ingrese nuevo cliente')
    nombre=input('ingrese nombre del cliente: ')
    correo = input('ingrese correo del cliente:  ')
    registrado = datetime.today().strftime('%Y-%m-%d')
    saldo = input('ingrese el saldo inicial del cliente: ')
    cliente = Cliente(id,nombre,correo,registrado,saldo)
    clientes = Clientes()
    clientes.agregar_cliente(cliente.obtener_cliente())

def mostrar_lista_clientes():
    clientes=Clientes()
    for cliente in clientes.lista_clientes:
        print('===============================================================================================================================================')
        print(cliente)
        print('===============================================================================================================================================')
    


##########################################################################################################
#                                 controller  clase producto                                             #
##########################################################################################################


def pedir_datos_producto():
    id = uuid.uuid4()
    id = str(id)
    id = id[1:8]
    print('ingrese nuevo producto')
    nombre=input('ingrese nombre del producto: ')
    categoria = input('ingrese categoria del producto:  ')
    proveedor = input('ingrese el nombre del proveedor')
    stock = input('ingrese el stock: ')
    valor_neto = input('ingrese el valor neto de venta: ')
    producto = Producto(id,nombre,categoria,proveedor,stock,valor_neto)
    productos = Productos()
    productos.agregar_cliente(producto.obtener_cliente())


def mostrar_lista_producto():
    productos = Productos()
    for producto in productos.lista_productos:
        print('===============================================================================================================================================')
        print(producto)
        print('===============================================================================================================================================')
    



##########################################################################################################
#                                 controller clase vendedor                                              #
##########################################################################################################


def pedir_datos_vendedor():
    id = uuid.uuid4()
    id = str(id)
    id = id[1:8]
    print('ingrese nuevo producto')
    run=input('ingrese el run del vendedor')
    nombre=input('ingrese nombre y apellido del vendedor: ')
    seccion = input('ingrese la seccion del vendedor:  ')
    vendedor = Vendedor(id,run,nombre,seccion)
    vendedores = Vendedores()
    vendedores.agregar_cliente(vendedor.obtener_vendedor())


def mostrar_lista_vendedor():
    vendedores = Vendedores()
    for vendedor in vendedores.lista_vendedores:
        print('===============================================================================================================================================')
        print(vendedor)
        print('===============================================================================================================================================')
