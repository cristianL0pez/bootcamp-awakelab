'''
DESARROLLO
Como parte de este ejercicio se necesita crear clases utilizando sintaxis de Python, para comprender las
ventajas de la programación orientada a objetos.
En base al sistema desarrollado anteriormente en el módulo de Python básico, se solicita actualizar lo
siguiente:

Identifica tres tipos de usuarios de su aplicación.
Identifica tres atributos por tipo de usuario.
Identifica tres acciones que pueden desarrollar cada tipo de usuario. Las acciones se deben ejecutar de
forma interna en nuestra aplicación. Por ejemplo, acceder a datos sensibles, registrar nuevos usuarios,
enviar solicitudes de información adicional.
● Piense en nuevos atributos y acciones que pueden realizar los objetos.
Piensen en una forma de graficar las relaciones entre las diferentes clases, puede ser un diagrama o
gráfica. Desarrollen el ejercicio de forma intuitiva.
'''






#diagrama uml para clases
#https://lucid.app/lucidchart/f51fcaa5-5fce-4e1e-9af5-25ba435b1f71/edit?invitationId=inv_2f85c63b-4007-4248-b5b0-cbff33bc5055
''' 

        Clientes
        atributos
    +_id : string {id}
    +nombre : string
    +edad : int
    +direccion: string
    +telefono: int
    +registrado: bool

    Metodos
    agregar_usuario()
    validar_edad()
    carrito_compra()
    comprar_producto()
    debolucio_producto()
    '''

''' 

        Bodegero
        atributos
    +_id : string{_id}
    +nombre : string
    +rol : string
    +sueldo: string

        Metodos
    agregar_producto():
    sumar_producto():
    mostrar_productos():
     



''' 
'''
        Vendedor
       atributos
    +_id : string{_id}
    +nombre : string
    +sucursal:string
        metodos
    descontar_productos():
    descuentos_productos():
    guardar_clientes():
        

'''
