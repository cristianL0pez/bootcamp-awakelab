'''DESARROLLO
● Guarde en una variable la siguiente información:
●
● Información de clientes: nombre, edad, identificador único.
● Información de productos: nombre, precio, identificador único y color.
● Información de la compra de cada cliente.
Debe crear 10 clientes y 5 productos.
La forma en que se organiza la información es a criterio del equipo. Es decir, ustedes definen el número
de variables y tipo de datos.
Sin definir funciones, utilice métodos necesarios para:
● Agregar Cliente.
● Agregar Producto
● Mostrar Clientes: Muestra el listado de clientes.
● Mostrar Producto: Muestra el listado de productos.
● Elimine clientes. ¿Qué información requiere para eliminar un cliente al azar?
● Elimine productos. ¿Qué información requiere para eliminar el último producto agregado?
En el caso que la información se esté guardando en un diccionario.
- Imprima todas las claves con un delay de 2 segundos.
- Luego imprima los valores con un delay de 3 segundos.
El código siempre debe estar debidamente comentado. Esto les ayudará a comprenderlo en el futuro y
ayudará a otras personas a comprender su código.
¿Lo lograron?
Imprima en pantalla un listado que contenga los ID de los usuarios.
Modifique todos los ID. Agregue la siguiente cadena de caracteres: “_piloto” al final de cada ID.
Imprima en pantalla los nuevos ID.
Elimine los últimos cuatro ID_clientes en el listado.'''

import time
import requests
import json
import uuid
import os
import sys
from pprint import pprint

sys.path.append(os.path.realpath("."))
import inquirer  # noqa

questions = [
    inquirer.List(
        "size",
        message="elija una opcion",
        choices=["1. Agregar Cliente", "2. Agregar Producto", "3. Mostrar Clientes:", "4. Mostrar Producto", "5. Elimine clientes", "6. Elimine productos","7. Elimine 4 ultimos",'8. agregar _piloto','9. mostrar ids','10. mostrar valores','11. mostrar keys'],
    ),
]

answers = inquirer.prompt(questions)

pprint(answers)

#https://randomuser.me/documentation#howto documentacion api


url = 'https://randomuser.me/api/?results=10&inc=name,dob,id' #url de la api
data =  requests.get(url)                                     #request generica 
users = data.json()['results']                                #tranformo data en json
####################################################################
#creo la lista clients y productos vacia
clients = []  
productos = [{'name': 'auto', 'id': ''}]                                               
for user in users:
    name = f"{user['name']['first']} {user['name']['last']}"
    age = user['dob']['age']
    id1 = uuid.uuid4()
    id1 = str(id1)
    clients.append({'name': name, 'age': age, 'id': id1})


    

######################################################################
#agregando mostrando y borrando
opcion = answers['size']
oadd1='1. Agregar Cliente'
oadd2='2. Agregar Producto'
oadd3='3. Mostrar Clientes:'
oadd4='4. Mostrar Producto'
oadd5='5. Elimine clientes'
oadd6='6. Elimine productos'
oadd7='7. Elimine 4 ultimos'
oadd8='8. agregar _piloto'
oadd9='9. mostrar ids'
oadd10='10. mostrar valores'
oadd11='11. mostrar keys'

if opcion == oadd1:
   nameadd = input('ingrese el nombre: ')
   id = uuid.uuid4()
   id_str = id
   str(id_str)
   clients.append({'name': nameadd, 'age': age, 'id': id})
   print(clients[-1])

elif oadd2 == opcion:
   nameadd = input('ingrese el nombre del producto ')
   id = uuid.uuid4()
   id_str = id
   str(id_str)
   productos.append({'name': nameadd, 'id': id_str})
   print(productos)

elif oadd3 == opcion:
     print(clients)

elif oadd4 == opcion:
    print(productos)

elif oadd5 == opcion:
    print(clients.pop())
  

elif oadd6 == opcion:
    print(productos.pop())

elif oadd7 == opcion:
    eliminar = len(clients) - (4 + 1)
    for index, client in enumerate(clients):
         if index > eliminar:
            del client['id']
            print(clients)

elif oadd8 == opcion:
    for client in clients:
        client['id'] += '_piloto'
        print(client)

elif oadd9 == opcion:
    for client in clients:
        print(client['id'])

elif oadd10 == opcion:
    for client in clients:
        for value in client.values():
            print(value)

elif oadd11 == opcion:
    for key in clients[0].keys():
        print(key)
    

 















        


   



















                                           






































