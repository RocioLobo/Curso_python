# FUNCIONES
## CONCEPTO
matematicamente una funcion es una operacion
que toma uno o mas valores llamados
```argumentos``` y produce un valor denominado
`resultado`.
>[!NOTE]
> Todos los lenguaes de programacion tiene funciones incorporadas(`funciones internas`),y funciones creadas por el usuario (`funciones externas`)

En programacion una funcion es un subprograma, es una
estructura que nos permite agrupar codigo y sus principales  objetivoss son:
-`NO REPETIR` fragmentos de codigo
-`REUTILIZAR` el codigo en distintos escenarios
## Estructura de una funcion
Una funcion tiene por `definida` por un `nombre`, sus
 `parametros` y su valor de `retorno`.
 una vez creada la funcion podremos solicitar su ejecucion
 `invocando` la funcion por su `nombre`

## Definir una funcion en pyton
Para deinir una funcion en pyton primero utilizaremos
la palabra reservada `def` segida por el `nombre` de la 
funcion.A continuacion especificaremos sin parametos, `(a)` si es
una funcion con parametros, si se tuviera mas de un
parametros iran separados por `,`, finalizaremos la
linea con `:` , en la siguiente linea sin olvidar el
 identado , comenzara el `cuerpo` de la funcion (micro
 programa) que puede contener 1 a mas
  sentencias , finalmente devera `retornar` un resultado con la palabra
  reservada `return`.
  >[!NOTE]
  > como retorno tambien se puede utilizar la `funcion interna`, `print ()`
  ,para depuracion de codigo no es recomendable usarlo en produccion.
  [observacion]
  `print` dentro de una funcion es una herramienta que nos permite comprobar

  **ejemplo**


  def saludo():
      saludo="hola chivo"
      saludo_dos="como estas"
      return saludo+ saludo_dos # concatenacion
      ## tambien 
      return f"{saludo},{saludo_dos}"
      saludo()
      print(saludo())
      # saludo()
    
## Invocar una funcion
para invovar, (o llamar, ejecutar)una funcion solo tendremos que
escribir el `nombre` de la funcion seguido por `()` parentesis.


def saludo():
     print("hola")
#  invocando la funcion
saludo()

## Retornar un valor
Las funciones pueden retornar (o devolver )un valor

def uno ():
    return
    uno()

>[!WARNING]
> No confundir `print()` con `return`. el valor retornado por
`return` nos permite usarlo fuera de su contexto. y `print()` solo 
mostrara el literal por terminal.

**ejemplo**
* en el archivo `lecture.py`

## Retornando multiples valores
El secreto es hacerlo mediante un tipo de tado estructurado

def varios ():
     return 2,3,4
varios()
# retorna(2,3,4)
def lista():
    return ["hola",45]
# retorna["hola",45]
def dicc():
     return{"nombre":"jose","edad":45}


## parametros y argumentos
 si una funcion no disposiera de valores de entrada estaria limitada en su actuacion.
 Es por ello que los `parametros` no permiten variar los datos que consume una funcion para obtener distintos resultados
 **ejemplo**
 *crear una funcion que recibe un valor numerico y retorna su raiz cuadrada
 
def sqrt(valor):
    return valor**(1/2)
# NOTA: en este caso, el valor 4 es un argumento de la funcion
sqrt(4)

cuando llamamos a na funcion con `argumentos`, los valores de estos argumentos se copian en los correspondientes
`parametros` dentro de la funcion

def ejm(a,b,c):
    return a+b+c
ejm(4,5,6)

### Argumentos nominales
en esta aproximacion los argumentos no son copiados en un orden especifico sino que 
**se asignan por nombre a cada parametro**.ello nos permite evitar el problema de
conocer o recordar cual es el orden de los parametros en la definicion de la funcion.
para utilizarlo, basta con realizar una asignacion de cada argumento en la propia llamada a la funcion.
**ejemplo**

def build_cpu(familia,num_core,recuencia):
    print(f"""
        la cpu de la familia {familia},
        con {num_core} cores y con una
        frecuencia de {frecuencia}
    """)

# haciendo uso de argumentos nominales
los argumentos son copiados en orden especifico, en este  caso debemos conocer o recordar cual es el orden de los parametros
build_cpu(num_core=4,familia="intel",frecuencia=2.7)


### Argumentos posicionales
build_cpu("intel",4,2,7)

### Parametros por defecto

es posible especificar **valores por defecto** en los parametros de una funcion , en
el caso de que no se proporcione un valor al argumento en la llamada a la funcion , el
parametro correspondiente tomara el valor definido por defecto.
**ejemplo**

def alumnos(nom,app,estado="aprobado"):

alumnos("ruth","castillo")
alumno("antony","crucez","desaprobado")

# desempaquetado/Empaquetado de argumentos(tarea)

Python nos ofrece la posibilidad de **empaquetar y desempaquetar argumentos** cuando estamos invocando a una función, tanto para argumentos posicionales como para argumentos nominales.

Y de esto se deriva el hecho de que podamos utilizar un número variable de argumentos en una función, algo que puede ser muy interesante según el caso de uso que tengamos.

### Empaquetar/Desempaquetar argumentos posicionales
Si utilizamos el operador `*` delante del nombre de un parámetro posicional, estaremos indicando que los argumentos pasados a la función se **empaqueten** en una tupla.

#### Vamos  a ver un ejemplo en el que vamos a implementar una función para sumar un número variable de valores. La función que tenemos disponible en Python no cubre este caso:
sum(4, 3, 2, 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum() takes at most 2 arguments (4 given)


Para superar esta «limitación» vamos a hacer uso del * para empaquetar los argumentos posicionales:
## EMPAQUETANDO

def _sum(*values):
    print(f'{values=}')
    result = 0
    for value in values:  # values es una tupla
        result += value
    return result
_sum(4, 3, 2, 1)
values=(4, 3, 2, 1)
10

###### Existe la posibilidad de usar el asterisco * en la llamada a la función para **desempaquetar** los argumentos posicionales:

values = (4, 3, 2, 1)

_sum(values)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in _sum
TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'


## Desempaquetado: _sum(4, 3, 2, 1)
_sum(*values)
values=(4, 3, 2, 1)
# 10

## Empaquetar/Desempaquetar argumentos nominales

Si utilizamos el operador ** delante del nombre de un parámetro nominal, estaremos indicando que los argumentos pasados a la función se **empaqueten en un diccionario.**

#### Supongamos un ejemplo en el que queremos encontrar la persona con mayor calificación de un examen. Haremos uso del ** para empaquetar los argumentos nominales:

def best_student(**marks):
    print(f'{marks=}')
    max_mark = -1
    for student, mark in marks.items():  # marks es un diccionario
        if mark > max_mark:
            max_mark = mark
            best_student = student
    return best_student



## Convenciones
En muchas ocasiones se utiliza **args** como nombre de parámetro para **argumentos posicionales** y **kwargs** como nombre de parámetro para argumentos nominales. Esto son únicamente convenciones, no hay obligación de utilizar estos nombres. Así, podemos encontrar funciones definidas de la siguiente manera:

def func(*args, **kwargs):
    # TODO
    pass
### Forzando modo de paso de argumentos
Si bien Python nos da flexibilidad para pasar argumentos a nuestras funciones en modo nominal o posicional, existen opciones para forzar que dicho paso sea obligatorio para una determinada modalidad.

### Argumentos sólo nominales
A partir de Python 3.0 se ofrece la posibilidad de obligar a que determinados parámetros de la función sean pasados sólo por nombre.

Para ello, en la definición de los parámetros de la función, tendremos que incluir un parámetro especial * que delimitará el tipo de parámetros. Así, todos los parámetros a la derecha del separador estarán obligados a ser nominales:


Separador para especificar parámetros sólo nominales

**Ejemplo**:

def sum_power(a, b, *, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b

sum_power(3, 4)
7

sum_power(a=3, b=4)
7

sum_power(3, 4, power=True)
25

sum_power(3, 4, True)

### Argumentos sólo posicionales
A partir de Python 3.8 se ofrece la posibilidad de obligar a que determinados parámetros de la **función sean pasados sólo por posición**.

Para ello, en la definición de los parámetros de la función, tendremos que incluir un parámetro especial / que delimitará el tipo de parámetros. Así, todos los parámetros a la izquierda del delimitador estarán **obligados a ser posicionales:**


Separador para especificar parámetros sólo posicionales

**Ejemplo:**

def sum_power(a, b, /, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b


sum_power(3, 4)
7

sum_power(3, 4, True)
25

sum_power(3, 4, power=True)
25

sum_power(a=3, b=4)
arguments: 'a, b'

## Fijando argumentos posicionales y nominales
Si mezclamos las dos estrategias anteriores podemos forzar a que una función reciba argumentos de un modo concreto.

Continuando con el **ejemplo** anterior, podríamos hacer lo siguiente:

def sum_power(a, b, /, *, power=False):
    if power:
        a **= 2
        b **= 2
    return a + b


sum_power(3, 4, power=True)  # Único modo posible de llamada

#
## FUNCIONES INTERNAS DE PYTON (tarea)
Funciones interiores
Está permitido definir una función dentro de otra función. Es lo que se conoce como función interior.

### tenemos lista de funciones internas

#### Sum(). 
Una función muy interesante que facilita la suma de valores de una lista o tupla en Python (siempre hablando de números como valores).
#### Min().
 Con esta función se puede hallar el número más pequeño dentro de una lista, tupla o dos o más argumentos.
Max(). 
La función contraria a Min() que, en lugar del número más pequeño, devuelve el valor más grande o mayor.
#### Range().
 Función de Python para generar una sucesión de números enteros de forma personalizada.
#### Round(). 
Cuando se trabaja con números matemáticos es importante disponer de una función capaz de realizar redondeos después de la coma, siendo esta la función de Python que se encarga de este proceso.
#### Hex ().
 Esta función que se incorporó a partir de la versión 3 de Python, convierte un número entero en una cadena hexadecimal con prefijo “0x”.
#### Abs().
 Al utilizar esta función sobre un número se obtiene su valor absoluto.
#### Id().
 Se trata de una función nativa que muestra un número entero que es único para cada objeto en memoria.
#### Bin().
 Convierte un número entero en una cadena binaria incluyendo el prefijo “0b”.


## AVERIGUAR
# Tipos de funciones
### Funciones anonimas (Funciones lambda)
 son para ejercicios rapidos  
una funcion que no tiene nombre lambda es una palabra reservada.
lambda:"hola"

#### normal tiene nombre y no tiene return
def saludo

### Funciones clousure
una funcion que dentro tiene otra funcion
`def saludo(nombre):
    print(f"bienvenido {nombre}")

### Funciones callback
Funciones que reciben por parametro otra funcion
funciones callback son ejemplo:
`print` y
`int(input("ingrese un numero:"))` son callback

ejemplo callback:

int(input())

def mensaje(m:function):
    print(m)

##### funcion normal

def pedir_nombre():
    nombre=input("ingresa tu nombre")
    return nombre
mensaje(pedir_nombre())



### Programacion funcional
es la programacion  funcional no requiere que sepas como se desarrollo y ejecuta el procesamiento de la informacion
**ejemplo**
```pyton

# programacion iterativa

lista=[5,7,8,4,1]
def num_minimo(l):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minimo=n
    return minimo

# programacion funcional

minaa(lista)

```


## averiguar sobre map(),filter(),reduce() (TAREA) cada uno con informacion y ejemplos


# MAP()  

`retorna los elementos si hay 10 te devuelve 10`
 
La función map() en Python `aplica una función a cada uno de los elementos de una lista`.

`map(una_funcion, una_lista)`

Imagina que tienes una lista de enteros y quieres obtener una nueva lista con el cuadrado de cada uno de ellos.

Seguramente, lo primero que se te ha ocurrido es algo similar a lo siguiente:

enteros = [1, 2, 4, 7]
cuadrados = []
for e in enteros:
    cuadrados.append(e ** 2)
     
print(cuadrados)
[1, 4, 16, 49]

### Sin embargo, podemos usar una función anónima en combinación con map() para obtener el mismo resultado de una manera mucho más simple:

enteros = [1, 2, 4, 7]
cuadrados = list(map(lambda x : x ** 2, enteros))
print(cuadrados)
[1, 4, 16, 49]

La cosa se vuelve todavía más interesante cuando, en lugar de una lista de valores, pasamos como segundo parámetro una lista de funciones:

enteros = [1, 2, 4, 7]
def cuadrado(x):
    return x ** 2
def cubo(x):
    return x ** 3
funciones = [cuadrado, cubo]
for e in enteros:
    valores = list(map(lambda x : x(e), funciones))
    print(valores)
[1, 1]
[4, 8]
[16, 64]
[49, 343]

# FILTER()

La función filter() `filtra una lista de elementos para los que una función devuelve True`.

`filter(una_funcion, una_lista)`

Imagina que quieres filtrar una lista de números para obtener solo los valores pares.

De nuevo, una primera aproximación podría ser como la siguiente:

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
print(pares)
[2, 4, 6, 8]

### No obstante, podemos usar la función filter() y una función lambda para obtener el mismo resultado con una sola línea de código:

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda x : x % 2 == 0, valores))
print(pares)
[2, 4, 6, 8]

# REDUCE()

 Esta ultima  función se utiliza principalmente para llevar a cabo un ``cálculo acumulativo sobre una lista de valores y devolver el resultado.``

La función reduce() está incluida en el módulo functools.

En este caso, la función que se pasa como primer parámetro recibe dos argumentos.

Imagina que quieres obtener el resultado de sumar todos los elementos de una lista.

Como en las veces anteriores, la suma la puedes calcular de la siguiente manera:

valores = [2, 4, 6, 5, 4]
suma = 0
for el in valores:
    suma += el
print(suma)
21

### Pero también usando la función reduce() en combinación con una función lambda:

from functools import reduce
suma = reduce(lambda x, y: x + y, valores)
print(suma)
21

