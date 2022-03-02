'''DESARROLLO
Como buen desarrollador, para comenzar a poder trabajar de manera óptima, es necesario que debamos
preparar las herramientas necesarias para inicializar nuestro proyecto, esto incluye tener ya nuestro
editor de texto y la versión de Python disponible en nuestro equipo.
Familiarizado ya con estos componentes debemos prepararnos para realizar las siguientes acciones,
para simular el funcionamiento de tu aplicación.



Diseñe 7 diccionarios, donde el nombre de cada diccionario es el nombre de un usuario de su aplicación.
En cada diccionario, integre características como: edad, género y otras características particulares de su
aplicación.


Por ejemplo, si la aplicación se enfoca en Juntas de Vecinos integrar dirección y número telefónico.
Integre al menos cinco características.
Guarde estos diccionarios en una lista. En el caso de ejemplo, podría ser nombrada “JJVV”.
A continuación, recorra su lista e imprima toda la información que posee la estructura de datos sobre
cada usuario (en el caso de ejemplo: de cada junta de vecinos).
¿Qué problemas encontró con esta forma de almacenar la información?
Vuelva al inicio del problema y diseñe una estructura de datos unificada que permita almacenar todas
las juntas de vecinos.
Agregue para cada usuario los campos nombre_usuario, id_unico, antigüedad, fecha de incorporación.
Imprima en pantalla la fecha de incorporación de todos los usuarios.'''

import time
import requests
import json
import uuid
import os
import sys
###from pprint import pprint

'''sys.path.append(os.path.realpath("."))
import inquirer  # noqa

questions = [
    inquirer.List(
        "size",
        message="elija una opcion",
        choices=["1. Agregar Cliente", "2. Agregar Producto", "3. Mostrar Clientes:", "4. Mostrar Producto", "5. Elimine clientes", "6. Elimine productos","7. Elimine 4 ultimos",'8. agregar _piloto','9. mostrar ids','10. mostrar valores','11. mostrar keys'],
    ),
]

answers = inquirer.prompt(questions)

pprint(answers)'''


url = 'https://randomuser.me/api/?results=7&inc=name,dob,id,location,phone,registered' #url de la api
data =  requests.get(url)                                     #request generica 
users = data.json()['results']                                #tranformo data en json
####################################################################
#creo la lista usuarios y vacia
jjvv = []                                                
for user in users:
    name = f"{user['name']['first']} {user['name']['last']}"
    age = user['dob']['age']
    direccion = user['location']['street']
    telefono = user['phone']
    registrado = user['registered']['date']
    id1 = uuid.uuid4()
    id1 = str(id1)
    jjvv.append({'name': name, 'age': age, 'id': id1,'street':direccion,'phone': telefono,'date':registrado})
    print(jjvv)

for d in jjvv:
    print('________________')
    print(d)
    print('________________')

for d in jjvv:
    print('registro')
    print('______________')
    print(d['name'])
    print(d['date'])
    
    

