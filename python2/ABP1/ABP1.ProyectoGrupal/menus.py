import inquirer  # noqa
import os
import sys
from pprint import pprint
sys.path.append(os.path.realpath("."))
'''
def pause():
    key_input = [inquirer.Text(name = 'pause', message='presione enter para continuar!')]
    return inquirer.prompt(key_input)


def menu_principal():
    print('=================================')
    print('     Menu principal       ')
    print('=================================')

    question = [
        {'value':1,'name':'Clientes'},
        {'value':2,'name':'Productos'},
        {'value':3,'name':'Vendedores'},
        {'value':4,'name':'Salir'}


    main_questions = [
        inquirer.List('menu',
            message='Que desea hacer?',
            choices=[f"{_['value']}.{_['name']}" for _ in question],
            carousel=True

        ),
        
        
    ]

    return inquirer.prompt(main_questions,)

'''
opcion1 = '1. clientes'
opcion2 = '2. productos'
opcion3 = '3. vendedor'
opcion4 = '4. salir'
###########################################
opcion_cliente1 = '1. mostrar saldo' 
opcion_cliente2 = '2. agregar_saldo'
opcion_cliente3 = '3. salir'
##########################################
opcion_vendedor1 = '1. descontar productos'
opcion_vendedor2 = '2. descuentos_productos'
opcion_vendedor3 = '3. guardar clientes'
opcion_vendedor4 = '4. salir'
############################################
opcion_producto1 = '1. agregar_producto'
opcion_producto2 = '2. sumar_producto'
opcion_producto3 = '3. mostrar_productos'
opcion_producto4 = '4. salir'



menu_principal = [
    inquirer.List(
        "menu",
        message="elija una opcion",
        choices=["1. clientes","2. productos","3. vendedor","4. salir"],
    ),
    
]
menu_cliente = [
    inquirer.List(
        "cliente",
        message="elija una opcion",
        choices=["1. mostrar saldo","2. agregar_saldo","3. salir"],
    ),
]
menu_vendedor = [
    inquirer.List(
        "vendedor",
        message="elija una opcion",
        choices=["1. descontar productos","2. descuentos_productos","3. guardar clientes","4. salir"],
    ),

]
menu_producto = [
    inquirer.List(
        "producto",
        message="elija una opcion",
        choices=["1. agregar_producto","2. sumar_producto","3. mostrar_productos","4. salir"],
    ),
    
]

