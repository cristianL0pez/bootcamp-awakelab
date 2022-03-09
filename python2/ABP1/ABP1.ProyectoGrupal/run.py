'''DESARROLLO - Continuación del trabajo.
Como parte de este ejercicio se necesita crear clases utilizando sintaxis de Python, para comprender las
ventajas de la programación orientada a objetos.
En base al sistema desarrollado anteriormente en el módulo de Python básico, se solicita actualizar lo
siguiente:

Incorporar la creación de las siguientes clases.
● Clase Cliente.
● Clase Producto.
● Clase Vendedor.
La Clase Cliente deberá contar con los siguientes atributos:
a. ID Cliente
b. Nombre
c. Apellido
d. Correo
e. Fecha Registro
f. __Saldo
La Clase Producto deberá contar con los siguientes atributos:
g. SKU
h. Nombre
i. Categoría
j. Proveedor
k. Stock
l. Valor_Neto
m. __Impuesto = 1.19
La Clase Vendedor deberá contar con los siguientes atributos:
n. RUN
o. Nombre
p. Apellido
q. Sección
r. __Comision = 0

Se solicita que los atributos __Saldo (Cliente), __Impuesto (Producto) y __Comision (Vendedor) se
encuentren encapsulados. Se debe crear métodos en la clase Cliente, lo cual puedan agregar y mostrar saldo.
Como se encuentra trabajando en el desarrollo del módulo de Python Básico, se solicita integrar
correctamente los métodos de las clases en las opciones del menú desarrollado.
Desarrollar 5 instancias de cada clase creada en los puntos anteriores.
Piensen en una forma de graficar las relaciones entre la

'''

from menus import * 
from Clientes import *
from Vendedor import *
from Productos import *
import uuid
import requests

url = 'https://randomuser.me/api/?results=5&inc=name,dob,id,location,email,registered' #url de la api
data =  requests.get(url)                                     #request generica 
users = data.json()['results'] 


clientes=[] 
for user in users:
    name = f"{user['name']['first']} {user['name']['last']}"
    correo = user['email']
    saldo = 0
    registrado = user['registered']['date']
    id1 = uuid.uuid4()
    id1 = str(id1)
    clientes.append({'id': id1,'name': name,'email':correo ,'date':registrado,'saldo':saldo})




def main():
    for user in users:
        c = Clientes(id1, name,correo ,registrado,saldo)
        
        
    
    opcion = ''
    while opcion != opcion4:
        opcion = inquirer.prompt(menu_principal)['menu']
        if opcion == opcion1:
             cliente_ = inquirer.prompt(menu_cliente)['cliente']
             if cliente_ == opcion_cliente1:
                
                 c.mostrar_clientes()

             elif cliente_ == opcion_cliente2:               
                 print('2. agregar_saldo') 
             elif cliente_ == opcion_cliente3:
                 print('3. salir')
                 inquirer.prompt(menu_principal)['menu']
             

        elif opcion == opcion2:
            productos_ = inquirer.prompt(menu_producto)['productos']
            if productos_ == opcion_producto1:
                pass
            elif productos_ == opcion_producto2:
                pass 
            elif productos_== opcion_producto3:
                pass  
            elif productos_ == opcion_producto4:
                 inquirer.prompt(menu_principal)['menu']


        elif opcion == opcion3:
            vendedor_ = inquirer.prompt(menu_vendedor)['vendedor']
            if vendedor_ == opcion_vendedor1:
                pass 
            if vendedor_ == opcion_vendedor2:
                pass 
            if vendedor_ == opcion_vendedor3:
                pass 
            if vendedor_ == opcion_vendedor4:
                inquirer.prompt(menu_principal)['menu']
                
 
                
                 
            
                 
main()

        


   
    

