import inquirer  # noqa


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
    ]
    question_client = [
        {'value':1,'name':'mostrar saldo'},
        {'value':2,'name':'agregar saldo'},
        {'value':3,'name':'Salir'}
    ]
    question_producto = [
        {'value':1,'name':'agregar producto'},
        {'value':2,'name':'sumar producto'},
        {'value':3,'name':'mostrar producto'},
        {'value':4,'name':'Salir'}
    ]
    question_vendedor = [
        {'value':1,'name':'descontar productos'},
        {'value':2,'name':'descuento producto'},
        {'value':3,'name':'descuento producto'},
        {'value':4,'name':'Salir'}
    ]


    main_questions = [
        inquirer.List('menu',
            message='Que desea hacer?',
            choices=[f"{_['value']}.{_['name']}" for _ in question],
            carousel=True

        ),
        
        
    ]

    return inquirer.prompt(main_questions,)


    

