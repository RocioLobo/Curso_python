# AVERIGUAR SOBRE MODULOS Y PAQUETES EN PYTON
# MODULOS
Un `módulo  en Python es un fichero .py` que alberga un conjunto de funciones, variables o clases y que puede ser usado por otros módulos. `Nos permiten reutilizar código y organizarlo mejor en namespaces`. Por ejemplo, `podemos definir un módulo mimodulo.py con dos funciones suma() y resta().`

## mimodulo.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

```Una vez definido, dicho módulo puede ser usado o importado en otro fichero, como mostramos a continuación. Usando import podemos importar todo el contenido.```

## otromodulo.py

import mimodulo

print(mimodulo.suma(4, 3))   # 7
print(mimodulo.resta(10, 9)) # 1

`También podemos importar únicamente los componentes que nos interesen como mostramos a continuación.`

from mimodulo import suma, resta

print(suma(4, 3))   # 7
print(resta(10, 9)) # 1

`Por último, podemos importar todo el módulo haciendo uso de *, sin necesidad de usar mimodulo.*.`

from mimodulo import *

print(suma(4, 3))   # 7
print(resta(10, 9)) # 1

## Rutas y Uso de sys.path

Normalmente los módulos que importamos están en la misma carpeta, pero es posible acceder también a módulos ubicados en una subcarpeta. Imaginemos la siguiente estructura:

.
├── ejemplo.py
├── carpeta
│   └── modulo.py
Donde modulo.py contiene lo siguiente:

## modulo.py
def hola():
	print("Hola")
Desde nuestro ejemplo.py, podemos importar el módulo modulo.py de la siguiente manera:

from carpeta.modulo import *
print(hola())
## Hola
Es importante notar que Python busca los módulos en las rutas indicadas por el sys.path. `Es decir, cuando se importa un módulo, lo intenta buscar en dichas carpetas. Puedes ver tu sys.path de la siguiente manera:`

import sys
print(sys.path)

Como es obvio, verás que la carpeta de tu proyecta está incluida, pero `¿y si queremos importar un módulo en una ubicación distinta?` Pues bien, podemos añadir al sys.path la ruta en la que queremos que Python busque.

import sys
sys.path.append(r'/ruta/de/tu/modulo')

`Una vez realizado esto, los módulos contenidos en dicha carpeta podrán ser importados sin problema como hemos visto anteriormente.`

### Cambiando los Nombres con as
Por otro lado, es posible cambiar el nombre del módulo usando as. Imaginemos que tenemos un módulo moduloconnombrelargo.py.

### moduloconnombrelargo.py
hola = "hola"
`En vez de usar el siguiente import, tal vez queramos asignar un nombre más corto al módulo.`

import moduloconnombrelargo
print(moduloconnombrelargo.hola)
Podemos hacerlo de la siguiente manera con as:

import moduloconnombrelargo as m
print(m.hola)

# PAQUETES
Un paquete es una `carpeta que contiene varios módulos`. Siguiendo el ejemplo anterior, podemos diseñar un paquete matematica creando una carpeta con la siguiente estructura.

matematica/
    |-- __init__.py
    |-- aritmetica.py
    |-- geometria.py

Debe contener siempre `un archivo __init__.py (por el momento vacío) para que Python entienda que se trata de un paquete y no de una simple carpeta.` Así, podemos acceder a alguno de los módulos del paquete de la siguiente manera.

`import matematica.aritmetica`

print(matematica.aritmetica.sumar(7, 5))

O bien de la siguiente.

`from matematica import aritmetica`

print(aritmetica.sumar(7, 5))

También, esta otra:

`from matematica.aritmetica import sumar`

print(sumar(7, 5))

# DIFERENCIAS ENTRE MODULOS Y PAQUETES

 ## MODULO. `La pieza más pequeña de software. Puede ser un conjunto de métodos o funciones para usarlo.`

 El módulo es un archivo que contiene funciones de Python, variables globales, etc. No es más que un archivo .py que tiene código / instrucción ejecutable de Python.

Por ejemplo: creemos un archivo user.py

def welcome_message(user_name):  
	return "Welcome " + name 
`Ahora puede importar el módulo foo.py en el intérprete de python u otro archivo py.`

import user 
print user.welcome_message("Quora") 


## PAQUETE. `Colección de módulos.`
El paquete es un `espacio de nombres que contiene múltiples paquetes / módulos.` Es un directorio que contiene un `archivo especial _init_.py`

`Vamos a crear un usuario de directorio. Ahora este paquete contiene múltiples paquetes / módulos para manejar solicitudes relacionadas con el usuario.`

user/ # top level package 
  _init_.py 
  get/ # first subpackage 
     _init_.py 
     info.py 
     points.py 
     transactions.py 
 create/ # second subpackage 
      _init_.py  
      api.py  
      platform.py 

`Ahora puedes importarlo de la siguiente manera`

from user.get import info # imports info module from get package 
from user.create import api #imports api module from create package  
Cuando importamos cualquier paquete, el intérprete de Python busca subdirectorios / paquetes.

## main .py es un archivo de pyton el codigo  dentro del archivo es un scrip