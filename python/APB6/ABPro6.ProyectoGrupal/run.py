'''DESARROLLO
● Como se mencionó anteriormente, es necesario mejorar el rendimiento de la empresa. Nuestro
socio se percató que hay mucho código que se repite una y otra vez, lo que dificulta el mantenimiento
de los programas.
###Control de Bodega
Nuestro programa deberá tener las siguientes funciones:
- Crear una bodega virtual con los productos iniciales.
- Almacenar nuevos productos.
- Actualizar el stock de productos en la bodega virtual.
- Mostrar y retornar las unidades disponibles por producto.
- Mostrar y retornar las unidades disponibles de un producto en particular.
- Mostrar y retornar todos los productos de la tienda.
- M).
###Control de Ventas
Nuestro programa deberá tener las siguientes funciones:
- mostrar y retornar el número de clientes registrados en la tienda.
- Funcionalidad para solicitar compra. Se ingresa el id del cliente, id del producto a comprar y las
unidades a comprar.
- respecto a la funcionalidad anterior, por defecto se comprará una unidad.
- Funcionalidad que verifique si existe stock necesario. Retorna valores booleanos.
- Funcionalidad que autoriza la compra. No es necesario que actualicen el stock de la bodega
virtual.
- Imprimir y retornar un mensaje “Compra aprobada y en camino” en caso que exista el stock
necesario.
- Imprimir y retornar un mensaje “Compra cancelada” en caso que no exista el stock necesario.
● Recuerden comentar debidamente su código.
PRODUCTOS:
ZAPATILLAS: 20 PARES
POLERAS: 10 UNIDADES
ZAPATOS: 15 PARES
POLERÓN: 3 UNIDADES
CHAQUETA: 5 UNIDADES
GUANTES: 4 PARES'''

import uuid
import requests
import re
import inquirer  # noqa
import time
import os
import sys
from pprint import pprint
######################################################################################################################
#                                                                                                                    #
#                                              inquirer                                                              #                                                                                                                 
#                                                                                                                    #
###################################################################################################################### 

sys.path.append(os.path.realpath("."))

menu_principal = [
    inquirer.List(
        "menu",
        message="elija una opcion",
        choices=["1. Control de Bodega","2. Control de Ventas","3. atras","4. salir"],
    ),
    
]
menu_bodega = [
    inquirer.List(
        "bodega",
        message="elija una opcion",
        choices=["1. agregar productos","2. actualizar stock","3. mostrar productos","4. mostrar todos los productos","5. mostrar productos por stock","6. atras","7. salir"],
    ),
]
menu_ventas = [
    inquirer.List(
        "ventas",
        message="elija una opcion",
        choices=["1. agregar clientes","2. mostrar clientes","3. solicitar compra","4. verificar stock","5. autorizar compra","6. atras","7. salir"],
    ),
]


#answers = inquirer.prompt(menu_principal)


#print(menu_principal['menu'])



######################################################################################################################
#                                                                                                                    #
#                                         Control de Bodega                                                          #                                                                                                                 
#                                                                                                                    #
###################################################################################################################### 

productos=[{
    '_id':'ea4ead69-4f0f-ee54-80ee-b0f17eff4136',
    'NOMBRE':'ZAPATILLAS',
    'CANTIDAD':20
          },
          {
    '_id':'ea4ead69-4f0f-ee54-43423-b0f17eff4136',
    'NOMBRE':'POLERAS',
    'CANTIDAD':10
         },
         {
    '_id':'ea4ead69-4f0f-fsf44-80ee-b0f17eff4136',
    'NOMBRE':'ZAPATOS',
    'CANTIDAD':15
        },
        {
    '_id':'ea4ead69-4f0f-efsfd-80ee-b0f17eff4136',
    'NOMBRE':'POLERÓN',
    'CANTIDAD':3
        },
        {
    '_id':'ea4ead69-4f0f-effff4-80ee-b0f17eff4136',
    'NOMBRE':'CHAQUETA',
    'CANTIDAD':5
    },
    {
    '_id':'ea4fdd69-4f0f-esdfs4-80ee-b0f17eff4136',
    'NOMBRE':'GUANTES',
    'CANTIDAD':4
    
}]


def agregar_productos():
    nombre=input('ingrese el producto: ').upper()
    cantidad = int(input('ingrese la cantidad de producto: '))
    id = uuid.uuid4()
    id = str(id)
    productos.append({'_id':id,'NOMBRE':nombre,'CANTIDAD':cantidad})
    print('se a ingresado el siguiente producto')
    print(productos[-1])
    

def actualizar_stock():
    print('stock actualizado')
        

def mostrar_productos():
    #muestra por consola los productos y su stock disponible
    for producto in productos:
        print('el producto: ',producto['NOMBRE'],'tiene ',producto['CANTIDAD'],'unidades')
    


def mostrar_producto_particular():
    #busca un producto en especifico en la DATA segun el argumento y los muestra 
    produc_particular = input('ingrese el nombre del producto para el que quiere saber su cantidad: ').upper()
    for producto in productos:
        if producto == produc_particular:
            print('el producto ingresado tiene: ',producto['CANTIDAD'])

def mostrar_solo_productos():
    #muestra todos los productos
    for producto in productos:
        print('Tenemos disponibles: ',producto['NOMBRE'])


def mostrar_producto_condicional():
    #muestra los producto que cumplen con la condicion de stock
    unidades = int(input('Indique el numero de unidades y le diremos los productos que tienen ese stock: '))
    for producto in productos:
        if producto['CANTIDAD'] > unidades:
            print(f'Tenemos', producto['CANTIDAD'],'unidades/pares del', producto['NOMBRE'])



######################################################################################################################
#                                                                                                                    #
#                                         Control de Ventas                                                          #                                                                                                                 
#                                                                                                                    #
######################################################################################################################                                                                                                                     
url = 'https://randomuser.me/api/?results=7&inc=name,dob,id,location,phone,registered' #url de la api
data =  requests.get(url)                                     #request generica 
users = data.json()['results'] 


clientes=[] 
for user in users:
    name = f"{user['name']['first']} {user['name']['last']}"
    age = user['dob']['age']
    direccion = user['location']['street']
    telefono = user['phone']
    registrado = user['registered']['date']
    id1 = uuid.uuid4()
    id1 = str(id1)
    clientes.append({'name': name, 'age': age, 'id': id1,'street':direccion,'phone': telefono,'date':registrado})
     

def add_user():
    nombre = input('ingrese su nombre: ')
    clave = input('ingrese su password: ')
    edad = input('ingrese su edad (solo numeros enteros): ')
    clientes.append({'name': nombre,'clave':clave,'edad':edad})
    return users, edad


# mostrar y retornar el número de clientes registrados en la tienda
def mostrar_clientes():
    for cliente in clientes:
        print('------------------------------------------')
        print(cliente)
        print('------------------------------------------')



# Funcionalidad para solicitar compra. Se ingresa el id del cliente, id del producto a comprar y las
# unidades a comprar
def solicitar_compra():
    print('__________solicitar compra_____________')
    id_client = input('ingrese el id del cliente: ')
    id_producto = int(input('ingrese el id del producto que quiere comprar: '))
    unidades = input('ingrese cantidad de productos: ')
    soli_compra = input('desea solicitar la compra? (si/no): ')
    if soli_compra == 'si':
        for producto in productos:
            if producto['CANTIDAD'] == 0:
                print('la cantidad del stock es 0')
                print('compra cancelada')
            elif producto['CANTIDAD'] > 0:
                print(f'Tenemos', producto['CANTIDAD'])
                print('“Compra aprobada y en camino')
    else:
        print('compra cancelada')
        

    return id_client, id_producto, unidades
    #print(f'Tenemos', producto['CANTIDAD'],'unidades/pares del', producto['NOMBRE'])
    

    


# Funcionalidad que verifique si existe stock necesario. Retorna valores booleanos.

def verifica_stock():
    pass
    


# Funcionalidad que autoriza la compra. No es necesario que actualicen el stock de la bodega
# virtual.
def autorizar_compra():
    pass



# Imprimir y retornar un mensaje “Compra aprobada y en camino” en caso que exista el stock necesario
# Imprimir y retornar un mensaje “Compra cancelada” en caso que no exista el stock necesario.

 
opcion1 = '1. Control de Bodega'
opcion2 = '2. Control de Ventas'
opcion3 = '3. atras'
opcion4 = '4. salir'
opcion_bodega1 = '1. agregar productos' 
opcion_bodega2 = '2. actualizar stock'
opcion_bodega3 = '3. mostrar productos'
opcion_bodega4 = '4. mostrar todos los productos'
opcion_bodega5 = '5. mostrar productos por stock'
opcion_bodega6 = '6. atras'
opcion_bodega7 = '7. salir'


opcion_ventas1 = '1. agregar clientes'
opcion_ventas2 = '2. mostrar clientes'
opcion_ventas3 = '3. solicitar compra'
opcion_ventas4 = '4. verificar stock'
opcion_ventas5 = '5. autorizar compra'
opcion_ventas6 = '6. atras'
opcion_ventas7 = '7. salir'


def main():
    opcion = ''
    while opcion != opcion4:
        opcion = inquirer.prompt(menu_principal)['menu']
        if opcion == opcion1:
             bodega_ = inquirer.prompt(menu_bodega)['bodega']
             if bodega_ == opcion_bodega1:
                 agregar_productos()
             elif bodega_ == opcion_bodega2:               
                 actualizar_stock() 
             elif bodega_ == opcion_bodega3:
                 mostrar_productos()
             elif bodega_ == opcion_bodega4:
                 mostrar_solo_productos()
             elif bodega_ == opcion_bodega5:
                 mostrar_producto_condicional()
             elif bodega_ == opcion_bodega6:
                  inquirer.prompt(menu_principal)['menu']

        elif opcion == opcion2:
            ventas_ = inquirer.prompt(menu_ventas)['ventas']
            if ventas_ == opcion_ventas1:
                 add_user()
            elif ventas_ == opcion_ventas2:
                 mostrar_clientes()
            elif ventas_ == opcion_ventas3:
                 solicitar_compra()
            elif ventas_ == opcion_ventas4:
                 verifica_stock()
            elif ventas_ == opcion_ventas5:
                 autorizar_compra()
            elif ventas_ == opcion_ventas6:
                  inquirer.prompt(menu_principal)['menu']
 
main()





    







