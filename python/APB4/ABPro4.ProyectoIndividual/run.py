'''Familiarizado ya con estos componentes debemos prepararnos para realizar las siguientes acciones,
para simular el funcionamiento de tu aplicación.
OPCIÓN 1:
Nuestra aplicación tendrá la siguiente particularidad. Al momento de crear un usuario, este debe ingresar
una contraseña que esté acorde a nuestros criterios de seguridad.
En este sentido, la contraseña debe contar con al menos 8 caracteres, con mayúsculas, minúsculas y
cifras.
Nuestro programa debe indicarle al usuario qué criterios le faltan para disponer de una contraseña
segura.
La contraseña debe ingresarse carácter por carácter en el terminal. Luego de escribir cada carácter, el
programa envía un mensaje con los criterios aún incumplidos.
OPCIÓN 2:
¿Recuerdan que en el ejercicio pasado asignamos cuestionarios particulares para cada perfil? Acá un
pequeño recordatorio: Para desarrollar de mejor forma tu aplicación, requieres conocer mejor a los
usuarios que la utilizarán. Antes de continuar desarrollando, debes elaborar un programa que tiene la
funcionalidad de enviar cuestionarios a grupos particulares de personas.
Nuestro socio consideró que los cuestionarios diferenciados estaban impactando negativamente en la
información obtenida.
En este sentido, nos pidió que distribuyamos los cuestionarios de forma aleatoria, sin tomar en
consideración la información personal.
Esta vez tomamos una serie de decisiones para facilitar el proceso:
Solo 7 personas responderán cuestionarios.
Tendremos los mismos cuestionarios del ejercicio anterior:
● Hábitos alimenticios, experiencia laboral, actividades recreativas, atletismo, natación y deportes
en general.
Los requisitos son:
● Los cuestionarios se envían de forma aleatoria.
● Los cuestionarios se envían uno después del otro con un desfase de 3 segundos para no
sobrecargar el servidor.
● El número máximo de formularios que una persona puede recibir es de 5.
Almacene el nombre del formulario que va a contestar cada persona.'''


import re 
usuarios=[]
print('a continuacion puedes crear tu usuario y password ')
print('la contraseña debe contar con al menos 8 caracteres, con mayúsculas, minúsculas y cifras.!')
nombre=input('escribe tu usuario : ')
passwd=input('elige la clave : ')
usuarios.append(nombre)
usuarios.append(passwd)
print(usuarios)
def validador(passwd): 
    passwd 
    print(passwd)
    reg = "^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$"#patron regex. Dígitos, minúsculas y mayúsculas y tamano minimo de 8 hasta 16
    pat = re.compile(reg) #El método del módulo Regex crea un objeto Regex, lo que hace posible ejecutar funciones regex en la variable pat
    mat = re.search(pat, passwd)#Luego verificamos si el patrón definido por pat va seguido de la cadena de entrada passwd 
    if mat: 
        print("La Password es valida.") 
    else: 
        print("la contraseña esta acorde a nuestros criterios de seguridad !!")
        print("la contraseña debe contar con al menos 8 caracteres, con mayúsculas, minúsculas y cifras.!")  
  
if __name__ == '__main__': 
    validador(passwd) 