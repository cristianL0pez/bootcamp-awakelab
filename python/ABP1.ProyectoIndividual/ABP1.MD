"""Es momento de preparar nuestro entorno de trabajo.
● Creación de un entorno virtual.
● Identificar la dirección de la carpeta donde están los archivos del entorno virtual.
● Activación del entorno virtual creado.
● Investigar las ventajas que tenemos al utilizar un entorno virtual en el desarrollo de nuestro
proyecto.
● ¿Qué consecuencia puede traer no realizar nuestro programa con un entorno virtual?
Ya reflexionamos sobre una tienda virtual, pero ¿qué pasa con otros sitios? ¿las páginas web con otras
finalidades siguen una lógica similar? """





![enter image description here](img/Captura.PNG)

"""Introducción
Un entorno de desarrollo virtual python o simplemente entorno virtual python es un mecanismo que me permite gestionar programas y paquetes python sin tener permisos de administración, es decir, cualquier usuario sin privilegios puede tener uno o más "espacios aislados" (ya veremos más adelante que los entornos virtuales se guardan en directorios) donde poder instalar distintas versiones de programas y paquetes python. Para crear los entornos virtuales vamos a usar el programa virtualenv o el módulo venv y para instalar paquetes python vamos a usar el programa pip . Antes de empezar a crear nuestros entornos, deberíamos hacernos las siguientes preguntas:

¿Para qué se usan los entornos virtuales?
Puede haber varios motivos en que su uso es conveniente e incluso necesario:

 Podemos tener necesidad de utilizar versiones de paquetes python que no son las que vienen empaquetadas oficialmente en nuestra distribución linux. La versión que se instala con nuestro gestor de paquetes, por ejemplo con apt en GNU/Linux Debian no corresponde con nuestras necesidades. Una solución puede ser usar pip como administrador: esta solución nos puede dar muchos problemas, ya que podemos romper las dependencias entre las versiones de nuestros paquetes python instalados en el sistema y algún paquete puede dejar de funcionar. En este caso sería necesario la utilización de un entorno virtual.
 En el caso del desarrollo y despliegue de aplicaciones web, cada vez es más importante acercar los entornos de desarrollo, prueba y producción, es decir, que estos tres entornos sean los más parecidos posible, para no tener "sorpresas" a la hora de desplegar la aplicación en producción. Utilizando entornos virtuales conseguimos que las dependencias entre paquetes que necesita nuestra aplicación estén satisfechas en todos los entornos, además es muy sencillo distribuir la configuración del entorno virtual, así como automatizar su creación, entre los distintos miembros del equipo de trabajo, consiguiendo que todos trabajen bajo el mismo escenario.
 Los ciclos de desarrollo de aplicaciones modernos en lenguajes como python son cada vez más rápidos, esto puede suponer que en una misma máquina podamos tener aplicaciones que utilicen diferentes dependencias y versiones de un mismo paquete. Por ejemplo, podemos tener dos aplicaciones web en producción, una que esté desarrollada con django 1.8 y otra con django 1.10. En este caso es imprescindible la utilización de entornos virtuales diferenciados, que sean la base de cada aplicación.
Además los entornos virtuales son una herramienta que favorecen las nuevas metodologías de trabajo que se denominan DevOps, que tratan de gestionar y automatizar la configuración. Es muy sencillo distribuir la configuración de nuetro en torno virtual y automatizar la creación de ellos en diferentes infraestructuras y escenarios.

¿Los entornos virtuales son propios sólo del lenguaje python?
No, existen herramientas parecidas en distintos lenguajes que nos ofrecen una funcionalidad parecida:

phpenv para php
plen y perlbrew para perl
rbenv y RVM para ruby
nodeenv , nvm , n y nave para node.js
¿Qué programa necesito para crear un entorno virtual con python 3?
Tradicionalmente hemos utilizado la herramienta virtualenv para crear nuestros entornos virtuales. Sin embargo, desde la versión 3.3 de python tenemos a nuestra disposición un módulo del sistema venv que podemos utilizar para crear nuestro entorno virtual. Por lo tanto debemos diferenciar los distintos paquetes que podemos utilizar:

virtualenv es un software que podemos encontrar en el Python Package Index o PyPI , que es el repositorio de paquetes de software oficial para aplicaciones de terceros en el lenguaje de programación Python.
venv es un módulo oficial del lenguaje que a partir de la versión 3.3 nos permite crear entornos virtuales.
pip : Independientemente de la manera en que creamos el entorno virtual, utilizando una de las dos herramientas anteriores, vamos a utilizar este sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python que se encuentran alojados en el repositorio PyPI .
Creando entornos virtuales con virtualenv
Podemos utilizar este software para trabajar con cualquier distribución de python, pero evidentemente es obligatorio si estamos trabajando con python 2.x o python 3.x (una versión anterior a la 3.3).

Instalación de los paquetes necesarios
En este manual se va a realizar la instalación y configuración en una distribución GNU/Linux Debian Jessie, en otra versión del sistema u otra distribución puede haber algunas diferencias.

Instalamos los paquetes necesarios como root:

# apt-get install python-virtualenv
Ahora ya como un usuario sin privilegio podemos crear un entorno virtual con el interprete python 2.7:

$ virtualenv entorno1
Running virtualenv with interpreter /usr/bin/python2
New python executable in entorno1/bin/python2
Also creating executable in entorno1/bin/python
Installing setuptools, pip...done.
Si queremos crear un entorno virtual con python3:

$ virtualenv -p /usr/bin/python3 entorno2
Already using interpreter /usr/bin/python3
Using base prefix '/usr'
New python executable in entorno2/bin/python3
Also creating executable in entorno2/bin/python
Installing setuptools, pip...done.
La opción -p nos permite indicar el interprete que se va a utilizar en el entorno.

En los dos casos se ha creado un directorio, donde se instalarán posteriormente los paquetes que necesitemos:

$ cd entorno2
$ ls
bin  lib
Activando nuestro entorno virtual
Independientemente el interprete que utilicemos en nuestro entorno para activarlo tenemos que ejecutar la siguiente instrucción:

$ source entorno2/bin/activate
(entorno2)$
Podemos observar que nuestro prompt ha cambiado, a partir de ahora estamos en nuestro entorno aislado, los paquetes python instalados en el sistema no serán visibles y podremos instalar paquetes en él utilizando la herramienta pip .

Desactivando nuestro entono virtual
Para salir del entorno que estamos ejecutando simplemente ejecutamos la siguiente instrucción:

(entorno2)$ deactivate
$
Creando entornos virtuales con venv
A partir de la versión 3.3 de python podemos utilizar el módulo venv para crear el entorno virtual.

Instalación de los paquetes necesarios
Instalamos el siguiente paquete para instalar el módulos:

# apt-get install python3-venv
Ahora ya como un usuario sin privilegio podemos crear un entorno virtual con python3:

$ python3 -m venv entorno3
La opción -m del interprete nos permite ejecutar un módulo como si fuera un programa. En este caso, a diferencia de usar la herramienta virtualenv , tenemos otra estructura de directorios en nuestro entorno virtual:

$ cd entorno3
$ ls
bin  include  lib  lib64  pyvenv.cfg
Activando y desactivando nuestro entorno virtual
La activación y la desactivación del entorno se realiza de forma similar a la explicada anteriormente:

$ source entorno3/bin/activate
(entorno3)$ deactivate
$
Instalando paquetes en nuestro entorno virtual
Independientemente del sistema utilizado para crear nuestro entorno virtual, una vez que lo tenemos activado podemos instalar paquetes python en él utilizando la herramienta pip (que la tenemos instalada automáticamente en nuestro entorno). Partiendo de un entorno activado, podemos, por ejemplo, instalar la última versión de django:

(entorno3)$ pip install django
Downloading/unpacking django
  Downloading Django-1.10.5-py2.py3-none-any.whl (6.8MB): 6.8MB downloaded
Installing collected packages: django
Successfully installed django
Cleaning up...
Podemos comprobar que efectivamente hemos instala la última versión de django:

(entorno3) $ django-admin --version
1.10.5
Si queremos ver los paquetes que tenemos instalados con sus dependencias:

(entorno3)$ pip list
Django (1.10.5)
pip (1.5.6)
setuptools (5.5.1)
Si necesitamos buscar un paquete podemos utilizar la siguiente opción:

(entorno3)$ pip search requests
Si a continuación necesitamos instalar una versión determinada del paquete, que no sea la última, podemos hacerlo de la siguiente manera:

(entorno3)$ pip install requests=="2.12"
Downloading/unpacking requests==2.12
  Downloading requests-2.12.0-py2.py3-none-any.whl (574kB): 574kB downloaded
Installing collected packages: requests
Successfully installed requests
Cleaning up...
Si necesitamos borrar un paquete podemos ejecutar:

(entorno3)$ pip uninstall requests
Y, por supuesto para instalar la última versión, simplemente:

(entorno3)$ pip install requests
Para terminar de repasar la herramienta pip , vamos a explicar como podemos guardar en un fichero (que se suele llamar requirements.txt ) la lista de paquetes instalados, que nos permite de manera sencilla crear otro entorno virtual en otra máquina con los mismos paquetes instalados. Para ello vamos a usar la siguiente opción de pip :

(entorno3)$ pip freeze
Django==1.10.5
requests==2.13.0
Y si queremos guardar esta información en un fichero que podamos distribuir:

(entorno3)$ pip freeze &gt; requirements.txt
De tal manera que otro usuario, en otro entorno, teniendo este fichero pude reproducirlo e instalar los mismos paquetes de la siguiente manera:

(entorno4)$ pip install -r requirements.txt"""