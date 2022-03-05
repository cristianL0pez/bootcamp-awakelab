
'''
DESARROLLO - Continuación del trabajo.
Como parte de este ejercicio se necesita crear clases utilizando sintaxis de Python, para comprender las
ventajas de la programación orientada a objetos.
En vista a nuestro sistema desarrollado anteriormente se solicita lo siguiente:
Agregar una clase BodegaPrincipal con los siguientes atributos:
a. Dirección
b. Mts2 ( metros cuadrados )
c. Stock
La clase BodegaPrincipal, deberá contar con las funciones de despachar_producto, la que descontará un
valor desde su stock y luego sumará a una sucursal (aumentando su cantidad de stock) y otra función con
el nombre de recepcionar_producto que sumará valor al stock.
Se deberá agregar una clase Sucursal la cual hereda de la clase BodegaPrincipal y el método
despachar_producto deberá descontar stock de la sucursal y agregarlo al stock de la clase
BodegaPrincipal.
El atributo stock de la clase producto, pasará de ser un valor a una Composición de la clase Sucursal y esta
contará con un límite de stock de 500 productos, lo cual si se agrega o sobrepasa ese límite (de 500) este
deberá emitir un mensaje de despacho del producto y sumarlo directamente en el atributo Stock de la clase
BodegaPrincipal.
Pensando en su tienda virtual, identifique casos en los que la técnica del polimorfismo solucionaría
problemas de herencia de métodos y atributos..
Definan la utilidad de MRO para determinados ejercicios de herencia. '''