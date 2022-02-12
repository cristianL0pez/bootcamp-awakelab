# bootcamp-awakelab

bootcamp python awakelab

  

repositorio para guardar codigo, trabajos, tareas etc
## desarrollo web

![](https://1.bp.blogspot.com/-EW9IYLNiqDA/Wv4r4sOGveI/AAAAAAAABUg/lL0B1cIEfCkrVROQXiApi92D6brGMLUPQCLcBGAs/s1600/visual-studio-code.jpg)🧑🏼‍💻

 # instalación de recursos
 # 1. descarga visual studio desde la pagina oficial

[pagina oficial visual studio code ](https://code.visualstudio.com/)

 [video para instalacion](https://www.youtube.com/watch?v=X_Z7d04x9-E&t=163s&ab_channel=Sistematts)
  # 2. descarga python3 desde la pagina oficial
[pagina oficial de python](https://www.python.org/)
![enter image description here](https://www.codigonaranja.com/wp-content/uploads/2019/02/descargar-python.png)
[video para instalacion](https://www.youtube.com/watch?v=m5i-Pq-z9w8&ab_channel=AlexRoelCode)
 
==Muy importante antes de instalar marcar el botón "add python 3.1 to Path" esto es para que python pueda ser invocado desde cualquier ruta o carpeta, todo lo demás se deja por defecto.==
![enter image description here](https://docs.blender.org/manual/es/2.80/_images/about_contribute_install_windows_installer.png)
### Ahora comprobáremos si se instalo correctamente en consola
==windows==
1. Press Win+R
2. Type cmd
3. Press OK or Enter
```
Aca debería mostrarte algo así
```
```python
python --version
Python 3.8.3

python -V
Python 3.8.3
```



==mac==
    -   Click on **Applications**
    -   Go to **Finder**
    -   Choose **Utilities** -> **Terminal**
    ```
Aca debería mostrarte algo así
```python
python --version
Python 3.8.3

python -V
Python 3.8.3

```

==linux==
Open the **terminal** linux
    
    Aca debería mostrarte algo así
   ```python
python --version
Python 3.8.3

python -V
Python 3.8.3
```
  

# 3. Ahora  instalaremos pipenv
Si estas en MacOS, puedes instalar Pipenv fácilmente con Homebrew:
```javascript
// 
brew install pipenv
```
O, si estás usando windows (powershell):
```javascript
// 
pip install pipenv
```
De lo contrario, solo usa pip:
```javascript
// 
pip install pipenv
```
Para comprobar si pipenv se instalo correctamente puedes usar el comando
```javascript
// 
pipenv --help 
check Checks for PyUp Safety security vulnerabilities and against PEP 508 markers provided in Pipfile. clean Uninstalls all packages not specified in Pipfile.lock. graph Displays currently-installed dependency graph information. install Installs provided packages and adds them to Pipfile, or (if no packages are given), installs all packages from Pipfile. lock Generates Pipfile.lock. open View a given module in your editor. run Spawns a command installed into the virtualenv. scripts Lists scripts in current environment config. shell Spawns a shell within the virtualenv. sync Installs all packages specified in Pipfile.lock. uninstall Uninstalls a provided package and removes it from Pipfile. update Runs lock, then sync.
```

# 3. Ahora  instalaremos git/github
### Instalar GIT en Windows

![Instalar GIT en Windows](https://www.hostinger.es/tutoriales/wp-content/uploads/sites/7/2017/04/git-for-windows.png)

En Windows, sólo tienes que descargar el instalador y ejecutarlo. Sigue estos sencillos pasos para hacerlo:

1.  [Descarga](https://git-for-windows.github.io/)  el instalador de GIT para Windows.
2.  Una vez que hayas descargado el instalador, haz doble clic sobre el ejecutable para que comience el proceso de instalación y sigue las instrucciones que te aparecerán en pantalla. Al igual que cualquier otro programa, tendrás que dar  **“Next”** (siguiente) en varias ocasiones hasta que aparezca la opción  **“Finish”** (terminar) para completar la instalación.
3.  Ahora tienes que abrir el símbolo de sistema y escribir los siguientes comandos en la terminal:
   ```javascript
// An highlighted block
    git config --global user.name "Tu nombre"
    
    git config --global user.email "ejemplo@email.com"
```
 Recuerda que debes de cambiar  **Tu Nombre** y  **ejemplo@email.com**  por tu información.
    

¡Y listo! Ya has instalado GIT en Windows.
## Instalar GIT en MacOS

![Instalar GIT en MacOS](https://www.hostinger.es/tutoriales/wp-content/uploads/sites/7/2017/04/git-en-macos.png)

Hay muchas formas de realizar la instalación en un equipo con Mac. De hecho, hay una probabilidad de que GIT ya esté instalado en tu equipo si tienes el XCode instalado. Ejecuta el siguiente comando en la terminal para revisar si ya está instalado:
   ```javascript
// An highlighted block
  
    git - -version
   
```


Si tienes una salida como git versión 2.12.0 (Apple Git-66), entonces estas de suerte. Pero si este no es el caso, sigue los siguientes pasos:

1.  [Descarga](https://sourceforge.net/projects/git-osx-installer/files/)  el instalador oficial par Mac.
2.  Sigue las instrucciones que te aparecerán en el programa de instalación.
3.  Al finalizar el proceso de instalación del instalador, vuelve a revisar usando el comando  **git – -version**  para confirmar si la instalación se ha hecho correctamente.
4.  Ahora ejecuta los siguientes comandos en la terminar para configurar tu correo y el nombre de usuario que están asociados a tu cuenta GIT:
    
   ```javascript
// An highlighted block
    git config --global user.name "Tu nombre"
    
    git config --global user.email "ejemplo@email.com"

```
    
    
  Recuerda reemplazar  **Tu nombre** y  **ejemplo@emial.com**  y agregar la información de tu cuenta.
## Instalar GIT en Linux

Si eres un usuario de Linux, tal vez estés acostumbrado a instalar softwares y paquetes usando los comandos  **apt-get**  o  **yum install**. GIT no es la excepción.

**Para usuarios de Ubuntu/Debian (apt-get):**

1.  Abre la terminal y ejecuta los siguientes comandos:
    
    Sudo apt-get update
    
    Sudo apt-get install git
    
2.  Verifica que la instalación se haya hecho correctamente usando el comando:  **git –version**.
3.  A continuación, ejecuta los siguientes comandos en la terminal para poder configurar tu correo y nombre de usuario que están asociados a tu cuenta GIT:
    
    git config --global user.name "Tu nombre"
    
    git config --global user.email "ejemplo@email.com".
    
    Recuerda cambiar  **Tu nombre** y  **ejemplo@email.com** por los datos de tu cuenta GIT.
    

**Fedora (yum/dnf):**

Puedes instalar los paquetes de GIT usando tanto yum y dnf.

1.  Abre la terminal y ejecuta los siguientes comandos:
    
    Sudo dnf install git
    
    Sudo yum install git
    
2.  Verifica que la instalación se haya hecho correctamente ejecutando el código:  **git –version**.
3.  Ejecuta los siguientes comandos en la terminal para configurar tu correo y tu nombre de usuario asociados a tu cuenta GIT:
          ```javascript
         // An highlighted block
        git config --global user.name "Tu nombre"
        git config --global user.email "ejemplo@email.com"
```
No olvides que debes reemplazar  **Tu nombre**  y  **ejemplo@email.com**  por los datos de tu cuenta.
    

## Conclusión

Listo, así es como se instala GIT en distintos sistemas operativos.
