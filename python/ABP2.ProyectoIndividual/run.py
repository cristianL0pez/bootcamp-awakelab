""" En base al contexto: Piensa en una aplicación web que busque solucionar una problemática.
● Esta aplicación debe entregar la posibilidad de iniciar sesión con un perfil individual.
● Generalmente, uno ingresa a su cuenta personal en una página, ésta te saluda y te reconoce
● Intentemos replicar esto. Crea un string con el nombre de al menos 7 usuarios de tu aplicación.
● Ahora piensa en tres de ellos. Búscalos en la lista con el método adecuado.
● ¿Qué problemas pueden surgir si otra persona quiere buscar a un usuario e ingresa manualmente
su nombre? ¿Cómo solucionarías este problema?
● Convierte tu string en una lista, en la cual cada elemento es un usuario.
● Imprima en pantalla la cantidad usuarios que tiene tu aplicación.
● Imprima en pantalla un mensaje de saludo a los diferentes usuarios. ¿Qué técnica puedes utilizar
para realizar esto?"""










users='cristian,carlos,patricia,claudio,patricio,anibal'
users=users.split(',')
#users=['cristiancarlospatriciaclaudiopatricioanibal']
nombre=input('busca un usuario: ')
print('el total de usuarios es: ',len(users))
for b in users:
    if nombre==b:
        print(b)

for i in users:
    print('hola',i)