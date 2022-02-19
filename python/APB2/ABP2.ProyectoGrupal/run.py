'''Formulen un programa que:
i. A una variable se le asigne un mensaje motivador que incluya los nombres de todos los
integrantes. ¿Qué tipo de dato puede ser?
ii. Se asegure que todos su caracteres estén en mayúscula.
iii. Elabore una lista con cada palabra del string.
iv. Cada integrante del grupo debe reconocer en qué índice está su nombre.
v. Indique cuántas palabras tenía el string.
vi. Imprima una tupla con todas las palabras del string.
vii. ¿Con qué función podrían obtener el mensaje por teclado al ejecutar el programa? Implementarlo!.
- Discutan ¿Qué es un dato booleano? ¿Qué utilidad puede tener para el desarrollo de un
programa?
- Investigar qué significa que python sea un lenguaje de tipado dinámico.
- Investigar y documentar sobre la creación de Módulos en Python.
- Investigar y documentar sobre la creación de Paquetes en Python.
- Investigar e implementar el uso del archivo __init__.py'''

busqueda=input('busque al usuario: ')

def implement(busqueda):
    users='cristian,carlos,patricia,claudio,patricio,anibal,be happy'
    users=users.upper()
    users=users.split(',')
    tupla=tuple(users)
    print(tupla)
    print('el indice del nombre es : ',users.index(busqueda))
    print('el total de palabras en el string es de: ',len(users))
implement(busqueda)