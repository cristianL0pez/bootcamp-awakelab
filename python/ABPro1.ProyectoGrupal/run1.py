"""● Creación de un entorno virtual.
● Identificar la dirección de la carpeta donde están los archivos del entorno virtual.
● Activación del entorno virtual creado.
● Investigar las ventajas que tenemos al utilizar un entorno virtual en el desarrollo de nuestro
proyecto.
Como grupo, deberán definir un listado de 5 productos con su respectivo valor unitario.

● Deberán crear un archivo .py el cual deberá solicitar ingresar una cantidad por cada producto
(definido de la lista).
● Se deberá mostrar en pantalla el total de la suma del pedido el que corresponde al valor neto.
● Se deberá mostrar en pantalla el total del IVA (19%) del total de pedido ingresado.
● Se deberá mostrar en pantalla el total final del pedido (la suma del valor neto + IVA).
 Consideraciones generales
- A modo de entrega se pide enviar un archivo Word, que presente al menos cuatro imágenes que
den cuenta del proceso llevado a cabo y además con la información de investigación correspondiente.
En caso que no tengan instalado Word, pueden apoyarse en GoogleDocs.
- Adjuntar el archivo .py con el pequeño script solicitado.
- El tiempo máximo para resolver la evaluación es el periodo correspondiente a una clase regular.
- Equipos máximos de 4 integrantes.
"""
productos=[['auto1',29],['auto2',117],['auto3',10],['auto4',300],['auto5',1000]]

auto1=input('cuantos auto 1 quiere de 29 : ')
auto2=input('cuantos auto 2 quiere de 117: ')
auto3=input('cuantos auto 3 quiere de 10: ')
auto4=input('cuantos auto 4 quiere de 300: ')
auto5=input('cuantos auto 5 quiere de 1000: ')


uno=productos[0][1]
dos=productos[1][1]
tres=productos[2][1]
cuatro=productos[3][1]
cinco=productos[4][1]



uno = int(auto1) * uno 
dos =  int(auto2)*dos
tres = int(auto3)*tres
cuatro=int(auto4)*cuatro
cinco = int(auto5)*cinco
resutadoNeto= uno+dos+tres+cuatro+cinco


resultadoIva=resutadoNeto*119/100
print(resultadoIva)








