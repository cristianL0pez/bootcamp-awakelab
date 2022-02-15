"""● Creación de un entorno virtual.
● Identificar la dirección de la carpeta donde están los archivos del entorno virtual.
● Activación del entorno virtual creado.
● Investigar las ventajas que tenemos al utilizar un entorno virtual en el desarrollo de nuestro
proyecto.
● Como grupo, deberán definir un listado de 5 productos con su respectivo valor unitario.
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
import inquirer 
questions = [
  inquirer.List('autos',
                message="que auto quieres comprar?",
                choices=['audi', 'foton', 'dodge', 'chevrolet', 'bmw',]
            ),
]
answers = inquirer.prompt(questions)
auto = answers
cantidad = input("escriba la cantidad  :")


autos = {
    'nombre':'',
    'precio':00
}

inventario =[]

inventario.append({ 'nombre':'audi','precio': 25,  })
inventario.append({ 'nombre':'foton','precio':20,  })
inventario.append({ 'nombre':'dodge','precio': 23,  })
inventario.append({ 'nombre':'chevrolet','precio': 18,  })
inventario.append({ 'nombre':'bmw','precio': 35,  })


for p in inventario:
    print('___________')
    print('\t nombre:',p['nombre'])
    print('\t precio:',p['precio'])





