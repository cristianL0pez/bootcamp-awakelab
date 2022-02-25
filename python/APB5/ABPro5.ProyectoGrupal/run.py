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
Elimine los últimos cuatro ID_clientes en el listado.

● Información de clientes: nombre, edad, identificador único.
● Información de productos: nombre, precio, identificador único y color.
● Información de la compra de cada cliente.'''
''' Agregar Cliente.
● Agregar Producto
● Mostrar Clientes: Muestra el listado de clientes.
● Mostrar Producto: Muestra el listado de productos.
● Elimine clientes. ¿Qué información requiere para eliminar un cliente al azar?
● Elimine productos. ¿Qué información requiere para eliminar el último producto agregado?'''


import requests
import json


#https://randomuser.me/documentation#howto documentacion api
#https://fakestoreapi.com/docs

url = 'https://randomuser.me/api/?results=10&inc=name,dob,id' #url de la api
data =  requests.get(url)                                     #request generica 
users = data.json()['results']                                #tranformo data en json


#url2 = ""
#data2 = requests.get(url2)
#products = data2.json()


#productos = []                                                
#for producto in products:
   # title = f"{productos['title']}"
   # productos.append({'title': title,})


clients = []                                                
for user in users:
    name = f"{user['name']['first']} {user['name']['last']}"
    age = user['dob']['age']
    id = user['id']['value']
    clients.append({'name': name, 'age': age, 'id': id})
    
    

print(clients[0])
print(clients)
































