# bootcamp-awakelab
bootcamp python  awakelab

repositorio para guardar codigo, trabajos, tareas etc

### desarrollo web
   
![](https://1.bp.blogspot.com/-EW9IYLNiqDA/Wv4r4sOGveI/AAAAAAAABUg/lL0B1cIEfCkrVROQXiApi92D6brGMLUPQCLcBGAs/s1600/visual-studio-code.jpg)🧑🏼‍💻

# instalación de recursos

|  |
| :---: |
| Created | <time>@January 18, 2022 11:57 PM</time> |
| Status |  |
| pertenece a | [📚Fundamentos del Desarrollo Web](https://www.notion.so/Fundamentos-del-Desarrollo-Web-75aeaa9367144c9e956fd1490236def9) |

* <details>**1. descarga visual studio desde la pagina oficial** [Gracias por descargar Visual Studio - Visual Studio Gracias por descargar Visual Studio - Visual Studio ![](https://visualstudio.microsoft.com/wp-content/uploads/2017/02/Microsoft-favicon.png) https://visualstudio.microsoft.com/es/thank-you-downloading-visual-studio/?sku=Community&rel=17![](https://visualstudio.microsoft.com/wp-content/uploads/2020/07/Facebook.png)](https://visualstudio.microsoft.com/es/thank-you-downloading-visual-studio/?sku=Community&rel=17) [https://www.youtube.com/watch?v=X_Z7d04x9-E&t=163s&ab_channel=Sistematts](https://www.youtube.com/watch?v=X_Z7d04x9-E&t=163s&ab_channel=Sistematts)

***

</details>

***

* <details>[Download Python Information about specific ports, and developer info Source and binary executables are signed by the release manager or binary builder using their OpenPGP key.![](https://www.python.org/static/favicon.ico) https://www.python.org/downloads/![](https://www.python.org/static/opengraph-icon-200x200.png)](https://www.python.org/downloads/)⚠️<mark>Muy importante</mark> antes de instalar  marcar el botón <mark>"add python 3.1 to Path"</mark> esto es para que python pueda ser invocado desde cualquier ruta o carpeta, todo lo demás se deja por defecto.**2. Ahora comprobáremos si se instalo correctamente en consola**
  - <details>
    + Press **Win+R**
    + Type **powershell**
    + Press **OK** or **Enter**</details>
  - <details>
    + Click on **Applications**
    + Go to **Finder**
    + Choose **Utilities** -> **Terminal**</details>**Linux**
  - Open the **terminal** window Aca debería mostrarte algo así

```
python --version
Python 3.8.3

python -V
Python 3.8.3
```</details>

***

* <details>**por que pipenv?**Los problemas que Pipenv busca resolver son multifacéticos
  - No necesitas usar más `pip` y `virtualenv` separados. Trabajan juntos.
  - Manejar un archivo `requirements.txt` [puede ser problemático](https://www.kennethreitz.org/essays/a-better-pip-workflow), por eso Pipenv usa en su lugar `Pipfile` y `Pipfile.lock`, que son superiores para usos básicos
  - Los Hashes se usan en todas partes, siempre. Seguridad. Automáticamente expone vulnerabilidades de seguridad.
  - Te da una vista de tu árbol de dependecias (e.g. `$&#xA0;pipenv&#xA0;graph`).
  - Coordina el flujo de desarrollo cargando archivos `.env`.**¡Instala hoy Pipenv!** Si estas en MacOS, puedes instalar Pipenv fácilmente con Homebrew:

```
 brew install pipenv
```

O, si estás usando windows <mark>(powershell)</mark>:

```
 pip install pipenv
```

De lo contrario, solo usa pip:

```
 pip install pipenv
```

Para comprobar si pipenv se instalo correctamente puedes usar el comando

```
pipenv --help

check      Checks for PyUp Safety security vulnerabilities and against PEP
             508 markers provided in Pipfile.
  clean      Uninstalls all packages not specified in Pipfile.lock.
  graph      Displays currently-installed dependency graph information.
  install    Installs provided packages and adds them to Pipfile, or (if no
             packages are given), installs all packages from Pipfile.
  lock       Generates Pipfile.lock.
  open       View a given module in your editor.
  run        Spawns a command installed into the virtualenv.
  scripts    Lists scripts in current environment config.
  shell      Spawns a shell within the virtualenv.
  sync       Installs all packages specified in Pipfile.lock.
  uninstall  Uninstalls a provided package and removes it from Pipfile.
  update     Runs lock, then sync.
```

</details>

***

* <details>
  1. Primero instalaremos git desde la pagina oficial [Downloads Git comes with built-in GUI tools ( git-gui, gitk), but there are several third-party tools for users looking for a platform-specific experience. View GUI Clients → Various Git logos in PNG (bitmap) and EPS (vector) formats are available for use in online and print projects.![](https://git-scm.com/favicon.ico) https://git-scm.com/downloads![](https://git-scm.com/images/logo@2x.png)](https://git-scm.com/downloads)procedemos a la instalación (en este punto solo marcamos este componente)y damos a next en esta parte configuramos el editor de código que usaremos con git por defecto en este caso visual studio code si usas otro aquí se configura y damos a next ⚠️todo lo demás quedara por defecto. Para saber si git se instalo de manera correcta usaremos el siguiente comando

```
git version
```

debería imprimir algo así git version 2.33.0.windows.1
  1. ahora descargaremos GitHub desktop para windows ⚠️Por temas de avanzar en este proyecto lo haremos con github desktop (el entorno de escritorio) lo ideal seria aprender a usar git desde la consola ya que el entorno grafico solo te dará mas dudas de como funciona git y cual es su funcionamiento correcto te recomiendo aprender mas de git y GitHub hay miles de cursos en YouTube  incluso dentro de este proyecto también hay documentación, te recomendamos ver información <mark>[aqu](https://www.notion.so/recursos-programaci-n-para-aprender-ee5d54db68b6433d825047ac7f38cdc1)</mark><mark>í</mark>
  1. Instalaremos GitHub desktop desde la pagina oficial [GitHub Desktop Checkout branches with pull requests and view CI statuses See all open pull requests for your repositories and check them out as if they were a local branch, even if they're from upstream branches or forks. See which pull requests pass commit status checks, too!![](https://github.githubassets.com/favicon.ico) https://desktop.github.com/![](https://desktop.github.com/images/upgrade/pr-checks.png)](https://desktop.github.com/)⚠️luego de instalar GitHub desktop deberán logearse con la cuenta  de GitHub que crearon anteriormente, si no se han creado una cuenta pueden crearla <mark>[aca](https://www.notion.so/cuentas-y-recursos-26582820141c4cd2a5f62ea2cbeb1c22)</mark></details>
