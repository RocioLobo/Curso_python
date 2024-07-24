# METODOS EN PYTON
# EN NUMEROS, TEXTOS, LISTAS,TUPLAS,DICCIONARIOS.


### **NUMEROS**

# LEN
(154788)
#devuelve la cantidad de digitos
#6



# INPUT()
input() permite obtener texto escrito por teclado. Al llegar a la función, el programa se detiene esperando que se escriba algo y se pulse la tecla Intro, como muestra el siguiente ejemplo:

print("¿Cómo se llama?")
nombre = input()
print(f"Me alegro de conocerle, {nombre}")
¿Cómo se llama?
Pepe
Me alegro de conocerle, Pepe

# SORT()

Ordena automáticamente los ítems de una lista por su valor de menor a mayor:
lista = [5,-10,35,0,-65,100]
lista.sort()
lista
[-65, -10, 0, 5, 35, 100]
# Podemos utilizar el argumento reverse=True para indicar que la ordene del revés:
lista.sort(reverse=True)
lista
[100, 35, 5, 0, -10, -65]


# COPY()
 copea los valores d la lista donde el valor es el elemento que almacena.
lista_original=[1,2,3,4] 
copia_lista=lista_original

lista_original[-1]=15 #esto es lo modificado
print(copia_lista) #copia la referencia modificada






### **TEXTO**



# LEN()
("hola mundo")
 devuelve la cantidad de caracteres
el espacio cuenta tambien como un caracter
10
# UPPER()
Devuelve la cadena con todos sus caracteres a mayúscula:
"Hola Mundo".upper()
'HOLA MUNDO'

# LOWER()
Devuelve la cadena con todos sus caracteres a minúscula:
"Hola Mundo".lower()
'hola mundo'

# CAPITALIZE()
Devuelve la cadena con su primer carácter en mayúscula:
"hola mundo".capitalize()
'Hola mundo'

# TITLE()
Devuelve la cadena con el primer carácter de cada palabra en mayúscula:
"hola mundo".title()
'Hola Mundo'

# COUNT()
Devuelve una cuenta de las veces que aparece una subcadena en la cadena:
"Hola mundo".count('mundo')
1

# FIND()
Devuelve el índice en el que aparece la subcadena (-1 si no aparece):
"Hola mundo".find('mundo')
5
"Hola mundo".find('mundoz')
-1

# RFIND()
Devuelve el índice en el que aparece la subcadena, empezando por el final:
"Hola mundo mundo mundo".rfind('mundo')
17

# ISDIGIT()
Devuelve True si la cadena es todo números (False en caso contrario):
c = "100"
c.isdigit()
True

# ISALNUM()
Devuelve True si la cadena es todo números o carácteres alfabéticos:
c = "ABC10034po"
c.isalnum()
True

# ISALPHA()
Devuelve True si la cadena es todo carácteres alfabéticos:
c = "ABC10034po"
c.isalpha()
False
"Holamundo".isalpha()
True

# ISLOWER()
Devuelve True si la cadena es todo minúsculas:
"Hola mundo".islower()
False

# ISUPPER()
Devuelve True si la cadena es todo mayúsculas:
"Hola mundo".isupper()
False

# ISTITLE()
Devuelve True si la primera letra de cada palabra es mayúscula:
"Hola Mundo".istitle()
True

# ISSPACE()
Devuelve True si la cadena es todo espacios:
"  -  ".isspace()
False

# STARWITCH()
Devuelve True si la cadena empieza con una subcadena:
"Hola mundo".startswith("Mola")
False

# ENDSWITH()
Devuelve True si la cadena acaba con una subcadena:
"Hola mundo".endswith('mundo')
True

# SPLIT()
Separa la cadena en subcadenas a partir de sus espacios y devuelve una lista:

"Hola mundo mundo".split()[0]

 'Hola'
Podemos indicar el carácter a partir del que se separa:


"Hola,mundo,mundo,otra,palabra".split(',')

['Hola', 'mundo', 'mundo', 'otra', 'palabra']

# JOIN()
Une todos los caracteres de una cadena utilizando un caracter de unión:
",".join("Hola mundo")
'H,o,l,a, ,m,u,n,d,o'
" ".join("Hola")
'H o l a'

# STRIP()
Borra todos los espacios por delante y detrás de una cadena y la devuelve:
"   Hola mundo     ".strip()

'Hola mundo'
Podemos indicar el carácter a borrar:


"-----Hola mundo---".strip('-')

'Hola mundo'

# REPLACE()
Reemplaza una subcadena de una cadena por otra y la devuelve:
"Hola mundo".replace('o','0')
'H0la mund0'
Podemos indicar un límite de veces a reemplazar:

"Hola mundo mundo mundo mundo mundo".replace(' mundo','',4)
'Hola mundo'



### **LISTAS**



# LEN(["h","o","l","a"])
 devuelve la cantidad de elementos
el espacio cuenta tambien como un caracter
#4

# APPEND()
Añade un ítem al final de la lista:
lista = [1,2,3,4,5]
lista.append(6)
lista
[1, 2, 3, 4, 5, 6]

# CLEAR()
Vacía todos los ítems de una lista:
lista.clear()
lista
[]

# EXTEND()
Une una lista a otra:
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
l1
[1, 2, 3, 4, 5, 6]

# COUNT()
Cuenta el número de veces que aparece un ítem:
["Hola", "mundo", "mundo"].count("Hola")
1

# INDEX()
Devuelve el índice en el que aparece un ítem (error si no aparece):
["Hola", "mundo", "mundo"].index("mundo")
1

# INSERT()
Agrega un ítem a la lista en un índice específico:
Primera posición (0):
l = [1,2,3]
l.insert(0,0)
l
[0, 1, 2, 3]
Penúltima posición (-1):
l = [5,10,15,25]
l.insert(-1,20) 
l
[5, 10, 15, 20, 25]

# Última posición en una lista con len():
l = [5,10,15,25]
n = len(l)
l.insert(n,30)
l

[5, 10, 15, 20, 25, 30]
# Una posición fuera de rango añade el elemento al final de la lista (999):

l.insert(999, 35)
l

[5, 10, 15, 20, 25, 30, 35]

# POP()
Extrae un ítem de la lista y lo borra:
l = [10,20,30,40,50]
print(l.pop())
print(l)
50
[10, 20, 30, 40]
# Podemos indicarle un índice con el elemento a sacar (0 es el primer ítem):
print(l.pop(0))
print(l)

10
[20, 30, 40]

# REMOVE()
Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos:
l = [20,30,30,30,40]
l.remove(30)
print(l)
[20, 30, 30, 40]

# REVERSE()
Le da la vuelta a la lista actual:
l.reverse()
print(l)
[40, 30, 30, 20]
# Las cadenas no tienen el método .reverse() pero podemos simularlo haciendo unas conversiones:
lista = list("Hola mundo")
lista.reverse()
cadena = "".join(lista)
cadena    
'odnum aloH'

# SORT()
Ordena automáticamente los ítems de una lista por su valor de menor a mayor:
lista = [5,-10,35,0,-65,100]
lista.sort()
lista
[-65, -10, 0, 5, 35, 100]
# Podemos utilizar el argumento reverse=True para indicar que la ordene del revés:
lista.sort(reverse=True)
lista
[100, 35, 5, 0, -10, -65]


### **TUPLAS**

# Las tuplas sólo disponen de dos métodos que son los siguientes:

# INDEX()
Sirve para buscar un elemento y saber su posición en la tupla:
tupla.index(100)
0
tupla.index('Hola')
1
Da error si no se encuentra:
tupla.index('Otro')

# count()
Sirve para contar cuantas veces aparece un elemento en una tupla:
tupla.count(100)
1
tupla.count('Algo')
0
tupla = (100,100,100,50,10)
tupla.count(100)
3
# APPEND() ?
Al ser inmutables, las tuplas no disponen de métodos para modificar su contenido:
tupla.append(10)




## **DICCIONARIOS**



colores = { "amarillo":"yellow", "azul":"blue", "verde":"green" }
# GET()
Busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto:
colores.get('negro','no se encuentra')
'no se encuentra'

# KEYS()
Genera una lista en clave de los registros del diccionario:
colores.keys()
dict_keys(['amarillo', 'azul', 'verde'])

# VALUES()
Genera una lista en valor de los registros del diccionario:
colores.values()
dict_values(['yellow', 'blue', 'green'])

# ITEMS()
Genera una lista en clave-valor de los registros del diccionario:
colores.items()
dict_items([('amarillo', 'yellow'), ('azul', 'blue'), ('verde', 'green')])
for clave, valor in colores.items():
    print(clave, valor)
amarillo yellow
azul blue
verde green

# POP()
Extrae un registro de un diccionario a partir de su clave y lo borra, acepta valor por defecto:
colores.pop("amarillo", "no se ha encontrado")
'yellow'
colores.pop("negro","no se ha encontrado")
'no se ha encontrado'

# CLEAR()
Borra todos los registros de un diccionario:
colores.clear()
colores
{}

