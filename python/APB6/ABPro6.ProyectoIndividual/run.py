'''DESARROLLO

Como buen desarrollador, para comenzar a poder trabajar de manera óptima, es necesario que debamos
preparar las herramientas necesarias para inicializar nuestro proyecto, esto incluye tener ya nuestro
editor de texto y la versión de Python disponible en nuestro equipo.
En esa ocasión se solicita un programa que:
- Pregunta el nombre de usuario y una contraseña.
- Almacene ambos datos en una variable.
- Que obtenga la edad del usuario a través de la consola. Sólo acepta números enteros.
- Almacene el dato edad a cada usuario.
- Imprima por cada usuario: su edad, y contraseña con un desfase de 5 segundos.
El programa debe reiniciarse cada vez que termina. Sin perder la información anterior, debe continuar
preguntando por nombre y contraseña.
Este loop podrá ser terminado sólo ingresando ‘salir’. Al momento de terminar, el programa debe imprimir
en pantalla la variable completa de datos hasta el momento de recibir la instrucción ‘salir’.'''
import re
import inquirer  # noqa
import time
import os
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))

questions = [
    inquirer.List(
        "size",
        message="elija una opcion",
        choices=["1. Agregar Cliente","2. imprima con desface", "3. salir"],
    ),
]


users = []
pedir = '1. Agregar Cliente'
pedir2 = '2. imprima con desface'
pedir3 = '3. salir'

def add_user():
    nombre = input('ingrese su nombre: ')
    clave = input('ingrese su password: ')
    edad = input('ingrese su edad (solo numeros enteros): ')
    edad = validador(exp_reg(edad),edad)
    users.append({'name': nombre,'clave':clave,'edad':edad})
    return users, edad

def imprima_desface(users):
    print(users)
    return users

def exp_reg(edad):
    reg = "^\d*$"
    pat = re.compile(reg) 
    mat = re.search(pat, edad)
    return mat


def validador(edad, mat = False ):
    while mat == False:
        print('la edad debe ser un numero')
        edad = input('ingresa la edad nuevamente: ')
        mat = exp_reg(edad)
    return edad
       
          
def main():
    opcion = ''
    while opcion != pedir3:
        opcion = inquirer.prompt(questions)['size']
        if opcion == pedir:
            add_user()
            print(users)    
        
        elif opcion == pedir2:
            imprima_desface(users)
           
main()
    





       

   
 
        


    
    



    




                
            

            

    





  
    




    
    
    
    

    







