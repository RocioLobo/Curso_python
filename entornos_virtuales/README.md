# ENTORNOS VIRTUALES
Un entorno virtual es un entorno Python en el que el intérprete Python, `las bibliotecas y los scripts instalados en él están aislados de los instalados en otros entornos virtuales`, y (por defecto) cualquier biblioteca instalada en un «sistema» Python, 
`es decir, uno que esté instalado como parte de tu sistema operativo`.
Un entorno virtual es un árbol de directorios que contiene archivos ejecutables de Python y otros archivos que indican que es un entorno virtual.

#### En otras palabras, cuando un entorno virtual está activo, instalan los paquetes Python en el entorno virtual sin necesidad de que se les diga explícitamente que lo hagan.

`Cuando un entorno virtual está activo (es decir, el intérprete de Python del entorno virtual se está ejecutando),` 

Cuando un entorno virtual está activo, cualquier opción que cambie la ruta de instalación será ignorada de todos los archivos de configuración de distutils para evitar que los proyectos se instalen inadvertidamente fuera del entorno virtual.

## PASOS A SEGUIR CON LOS SIGUIENTES COMANDOS

#### 1.primero ingresaremos en la carpeta creada `entornos_virtuales` con el Ssiguiente comando.
`cd entornos_virtuales.`
#### 2. segundo vamos a listar con el siguiente comando.
`ls`

#### 3. tercero agregaremos el nombre con el siguiente comando.

`pyton -m venv.entornos_virtuales`
#### 4.cuarto ingresaremos al archivo ejecutable con el comando.
`python -m venv .venv`
#### 5.siguiente vamos pasar a activar con el siguiente comando.
`source .venv scripts/activSate`
si esta activado sandra con
`(.venv)`
#### 6.como siguiente vamos a ver la lista de version para instalar actualizar y administrar paquete  con el siguiente comando.
`pip list`
#### 7. pasamos a instalar.
`pip install --upgrade pip`
#### 8.siguiente instalaremos en pyton.
`python -m pip install --upgrade pip`
#### 9. siguiente veremos la lista de version activada e instalada.
`pip list`
#### 10. como seguida veremos la version.
`pip --version`
#### 11. tambien podemos desactivarcon el comando.
`deactivate`
#### 12.pws si queremos activare sera con el siguiente comando.
`source.venv/scripts/activate `

y pws aparecera si esta activado debajo con 
`(.venv)`
#### 13. veremos la instalacion para crear desarrollar facilmente con el siguiente comando:
`pip install flet`
#### 14. siguiente veremos la lista con .
`pip list`

#### 15. pws ultimo es bueno desactivar donde daremos.
`deactivate`
#### 16. y por ultimos si deseas borrar todo damos lo siguiente.
`rm - rf entornos_virtuales`



S