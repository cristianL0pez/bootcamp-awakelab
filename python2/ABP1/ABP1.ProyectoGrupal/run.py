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
import menus
from Clientes import *
from Vendedor import *
from Productos import *




valor_opcion=lambda funcion, nombre: funcion[nombre]


def main():
    opc=''
    while opc != '4.Salir':
        opc = valor_opcion(menus.menu_principal(),'menu')
        print(opc)    
        if opc =='1.Clientes':
            opc = valor_opcion(menus.menu_cliente(),'menu_client')
        elif opc=='2.Productos':
            opc = valor_opcion(menus.menu_producto(),'menu_producto')
        elif opc=='3.Vendedores':
            opc = valor_opcion(menus.menu_vendedores(),'menu_vendedores')
        else:
            menus.pause()

        


   
    
main()
