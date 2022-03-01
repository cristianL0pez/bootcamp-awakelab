'''DESARROLLO
● Como se mencionó anteriormente, es necesario mejorar el rendimiento de la empresa. Nuestro
socio se percató que hay mucho código que se repite una y otra vez, lo que dificulta el mantenimiento
de los programas.
###Control de Bodega
Nuestro programa deberá tener las siguientes funciones:
- Crear una bodega virtual con los productos iniciales.
- Almacenar nuevos productos.
- Actualizar el stock de productos en la bodega virtual.
- Mostrar y retornar las unidades disponibles por producto.
- Mostrar y retornar las unidades disponibles de un producto en particular.
- Mostrar y retornar todos los productos de la tienda.
- Mostrar y retornar los productos que tienen más de un número de unidades (el usuario puede
escoger el número de unidades).
###Control de Ventas
Nuestro programa deberá tener las siguientes funciones:
- mostrar y retornar el número de clientes registrados en la tienda.
- Funcionalidad para solicitar compra. Se ingresa el id del cliente, id del producto a comprar y las
unidades a comprar.
- respecto a la funcionalidad anterior, por defecto se comprará una unidad.
- Funcionalidad que verifique si existe stock necesario. Retorna valores booleanos.
- Funcionalidad que autoriza la compra. No es necesario que actualicen el stock de la bodega
virtual.
- Imprimir y retornar un mensaje “Compra aprobada y en camino” en caso que exista el stock
necesario.
- Imprimir y retornar un mensaje “Compra cancelada” en caso que no exista el stock necesario.
● Recuerden comentar debidamente su código.
PRODUCTOS:
ZAPATILLAS: 20 PARES
POLERAS: 10 UNIDADES
ZAPATOS: 15 PARES
POLERÓN: 3 UNIDADES
CHAQUETA: 5 UNIDADES
GUANTES: 4 PARES'''



productos={'ZAPATILLAS':20,'POLERAS':10,'ZAPATOS':15,'POLERÓN':3,'CHAQUETA':5,'GUANTES':4,}
print(productos)

def agregar_productos():
    key=input('ingrese el producto')
    value= int(input('ingrese el producto'))
    productos.update({key: value})


def actualizar_stock(key, unidades_venta):
    productos[key] -= unidades_venta


def mostrar_productos():
    for key,value in productos.item():
        print(f'tenemos {value} unidades del {key}')


def mostrar_productos(key):
    for key, value in productos.item():
        if key == productos.upper():
            print(key, value)

def mostrar_todos_productos():
    for key in productos.keys():
        print(f'tenemos disponibles {key}')


def mostrar_producto_condicional():
    #muestra los producto que cumplen con la condicion de stock
    unidades = int(input('Indique el numero de unidades y le diremos los productos que tienen ese stock: '))
    for key, value in productos.items():
        if value > unidades:
            print(f'Tenemos {value} unidades/pares del {key}')




    







