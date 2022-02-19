'''● Para desarrollar de mejor forma tu aplicación, requieres conocer mejor a los usuarios que la
utilizarán. Antes de continuar desarrollando, debes elaborar un programa que tiene la funcionalidad de
enviar cuestionarios a grupos particulares de personas.
● Los formularios varían según la edad, el lugar de origen y la afinidad con los deportes que tiene
el usuario.
● El número máximo de cuestionarios a responder es de 3.
● Los usuarios que son originarios de América Latina responden el cuestionario sobre hábitos
alimenticios.
● Los usuarios que NO son originarios de América Latina no responden el cuestionario de hábitos
alimenticios.
● Todos los usuarios entre 18 y 29 años responden el cuestionario de empleabilidad.
● Los usuarios originarios de América Latina entre 30 y 59 años responden el cuestionario de
experiencia laboral.
● Los usuarios originarios de América Latina de 60 años y más responden el cuestionario de
actividades recreativas.
● Todos los usuarios que tienen afinidad por los deportes y que son menores de 60 años responden
el cuestionario de atletismo.
● Los usuarios originarios de América Latina que tienen afinidad por los deportes y que tienen 60
años o más responden el cuestionario de natación.
● Todos los usuarios que no tienen afinidad por los deportes responden un cuestionario de
Deportes en General.
● El usuario debe ingresar por consola sus características (lugar de origen, edad y afinidad por los
deportes).
● Programa un mensaje que indique el número de cuestionarios a responder y cuáles son. 




 18 y 29 años =empleabilidad && mayor 60 años=actividades recreativas  menor 60 años=atletismo 

'''
#preguntas al usuario
edad=int(input('edad: '))
lugar=input('lugar de origen: ')
afinidad=input('afinidad con los deportes: ')
#cuestionarios
cuestAlimen='hábitos alimenticios.'
cuestEmple='empleabilidad'
cuestExpLab='experiencia laboral'
cuestActRec='actividades recreativas'
cuestAtle='atletismo'
#ifs para la solucion
if lugar == 'latam' and edad == 30 and edad < 59:
    print(cuestAlimen,cuestExpLab)
elif edad == 18 or edad < 29:
    print(cuestEmple)
else:
    print('todo bein')


