from multiprocessing.sharedctypes import Value
import uuid
import inquirer
import time


opcion_bodega1 = '1. agregar productos' 
opcion_bodega2 = '2. sumar productos'
opcion_bodega3 = '3. mostrar todos los productos'
opcion_bodega4 = '4. mostrar productos por stock'
opcion_bodega5 = '5. atras'
opcion_bodega6 = '6. salir'




productos=[{
    '_id':'ea4ead69-4f0f-ee54-80ee-b0f17eff4136',
    'NOMBRE':'vasos',
    'CANTIDAD':500
          },
          {
    '_id':'ea4ead69-4f0f-ee54-43423-b0f17eff4136',
    'NOMBRE':'cucharas',
    'CANTIDAD':450
         },
         {
    '_id':'ea4ead69-4f0f-fsf44-80ee-b0f17eff4136',
    'NOMBRE':'cuchillos',
    'CANTIDAD':400
        },
        {
    '_id':'ea4ead69-4f0f-efsfd-80ee-b0f17eff4136',
    'NOMBRE':'tenedores',
    'CANTIDAD':300
        },]


def agregar_productos():
    nombre=input('ingrese el producto: ').upper()
    cantidad = int(input('ingrese la cantidad de producto: '))
    id = uuid.uuid4()
    id = str(id)
    productos.append({'_id':id,'NOMBRE':nombre,'CANTIDAD':cantidad})
    print('se a ingresado el siguiente producto')
    print(productos[-1])
    

def sum_producto():
    product = input('nombre de producto a sumar: ')
    for producto in productos:
        if product == producto['NOMBRE']:
            print(producto['NOMBRE'],producto['CANTIDAD'])
            sum = int(input('cuantos productos quieres sumar: '))
            producto['CANTIDAD']+=sum
            
def res_producto():
    product = input('nombre de producto a restar: ')
    for producto in productos:
        if product == producto['NOMBRE']:
            print(producto['NOMBRE'],producto['CANTIDAD'])
            res = int(input('cuantos productos quieres restar: '))
            producto['CANTIDAD']-=res  #restar cantidad del producto con el res?

def mostrar_productos_sleep():
    #muestra por consola los productos y su stock disponible
    for producto in productos:
        time.sleep(1.5)
        print('el producto: ',producto['NOMBRE'],'tiene ',producto['CANTIDAD'],'unidades')       

def mostrar_productos():
    #muestra por consola los productos y su stock disponible
    for producto in productos:
        print('el producto: ',producto['NOMBRE'],'tiene ',producto['CANTIDAD'],'unidades')



def verificar_stock():
    #muestra por consola los productos y su stock disponible
    for producto in productos:
        if producto < 400:
            print('el stock es menor a 400')
    







    