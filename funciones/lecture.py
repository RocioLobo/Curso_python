# return devuelve valores que podre hacer uso
# crear una funcion que retorne el numero 10 y muestra por terminal si es par
# siempre que el valor que retorne mi funcion se utilize en mas sentencias u operaciones hacer uso de return
def diez():
    return 10
if diez()%2==0:
    print("es par")
else:
    print("es impar")


# print solo muestra por terminal


# return cuando queremos que muestra funcion devuelva o retporne un tipo de dato o un tipo de dato estructurado.


#cear una funcion que me muestre el producto de dos numeros
def procducto(a,b):
    return a*b


#crear una funcion que me retorne una lista de tres  numeros

def lista_numeros():
    return [3,2,6]

# print usaremos cada vez que nuestra funcion retorne un mensaje
# crear una funcion que por parametro reciba un nombre y retorne un mensaje de bienvenida con el nombre

def mensaje(nombre):
    print(f"hola,{nombre},bienvenido al chongo")


# crear una funcion que reciba por parametro una lista de numeros y me devuelva el numero menor ,mostrar por terminal el valor retornado por la funcion.
lista=[4,3,6,78,7]
def Min(l):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minimo=n
    return minimo
print(Min(lista))

# crear una funcion que reciba como parametro el nombre y la edad de una persona mi funcion debera retornar un diccionario con los datos, luego mostrar por terminal el valor de retorno de mi funcion.

nombre="abel"
edad=19
def persona(nom,edad):
    return{
        "nombre":nom,
        "edad":edad
    }
print(persona(nombre,edad))

#1. desempaquetado/Empaquetado de argumentos(tarea)
# vamos a implementar una función para sumar un número variable de valores.
# EMPAQUETANDO
#vamos a hacer uso del * para empaquetar los argumentos posicionales:
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

# DESENPAQUETANDO: _sum(4, 3, 2, 1)
_sum(*values)
values=(4, 3, 2, 1)
# 10

# FUNCIONES INTERNAS EN PYTON.

# en el que extraemos las palabras de un texto que contienen todas las vocales, haciendo uso de una función interior que nos devuelve el número de vocales distintas que tiene cada palabra:

def get_words_with_all_vowels(text: str) -> list[str]:
    VOWELS = 'aeiou'
    def get_unique_vowels(word: str) -> set[str]:
        return set(c for c in word if c in VOWELS)
    result = []
    for word in text.split():
        if len(get_unique_vowels(word)) == len(VOWELS):
            result.append(word)
    return result

get_words_with_all_vowels('La euforia de ver el riachuelo fue inmensa')
['euforia', 'riachuelo']



# (CLASE) EMPAQUETANDO /DESENPAQUETADO DE ARGUMENTOS

#ejemplos
#EMPAQUETANDO 

#def suma(*args):
#    nueva_lista=list(args)
#    nueva_lista[0]=10
#    print(nueva_lista)
# suma(4,7,8,5,2,4) 

# crear una funccion que reciba por argumentos n numeros y retorne una lista con los numeros pares


def num_pares(*args):
    pares=[]
    for n in args:
        if n%2==0:
            pares.append(n)
        return pares
print(num_pares(8,4,16,4,5,4))   


#por compresion
#return [n for n in args if n%2==0]
print(num_pares(8,5,4,7,9,25,4,7,12))



#empaqueta/desempaqueta de argumentos nominales

def alumnos(** kwargs):
    print(kwargs)
alumnos(nombre="miguel",apellido="largo",edad=30)


def alumnos(** kwargs):
    kwargs["nombre"]="abel"
    print(kwargs)
alumnos(nombre="miguel",apellido="largo",edad=30)

## ejemplos de lambda

saludo=lambda:"hola"
print(saludo())

# otro ejemplo

saludo=lambda n:f"hola","{n}" ,"{a}"
print(saludo("ruth", "castillo"))


# crear un programa anonimo que reciba como parametro una lista de 5 numeros y retorne  dos listas una con los numeros pares y otra con numeros impares.


#tarea hacer en una linea mas pequeña utilizando dicconario objetos

lista_num=[4,7,5,3,47,2,10,8,10]
pares=lambda l:[n for n in lista if n%2==0]
impares=lambda l:[n for n in lista if n%2==0]
print(pares(lista))
print(impares(lista))



# otra manera de hacer en linea mas pequeña

separar_pares, separar_impares = lambda lista: [num for num in lista if num % 2 == 0], lambda lista: [num for num in lista if num % 2 != 0]
print(separar_pares(lista), separar_impares(lista))


#ejemplo de callback

int(input())

def mensaje(m:function):
    print(m)
def pedir_nombre():
    nombre=input("ingresa tu nombre")
    return nombre
mensaje(pedir_nombre())

#ejemplos de MAP, FILTER, REDUCE 

# MAP

lista=[4,7,8,5,2]
nueva_lista=list(map(lambda x:x+1,lista))  #por defecto retorna una lista

print(nueva_lista)

#tengo una lista de alumnos que todos ellos han aprovado y pasan al tercer semestre
#problema en mi lista todos estan con el segundo semestre por lo que tendremos  que crear un solucion que cambie el campo de semestre de 2 a 3


lista_alumnos=[
   

{
        "nombre":"abel",
        "edad":36,
        "semestre":2,
        
    },
    {
        "nombre":"antony",
        "edad":40,
        "semestre":2,
        
   
    },
    {
        "nombre":"edith",
        "edad":50,
        "semestre":2,
        

    }
]

def objeto(e):
    if "semestre" in e:
        e["semestre"]=e["semestre"]+1
    return [
        e
    ]
        
        
alumnos_actualizados=list(map(objeto,lista_alumnos))
print(alumnos_actualizados)

def objeto(e):
    if"semestre" in e:
        e["semestre"]=e["semestre"]+1
    e["especialidad"]="APSTI"
    return [
        e
    ]
semestre_actualizados=list(map(objeto,lista_alumnos))
print(semestre_actualizados)

#otra manera de agregar en una lista

def objeto(e):
    e["programa_estudio"]="APSTI"
    return [
        e
    ]
alumnos_actualizados=list(map(objeto,lista_alumnos))
print(alumnos_actualizados)


#FILTER (busca encuentra y devuelve)

#devolvere los numeros pares de una lista

lista=[4,8,2,5,7,10,6,5,3,20]
nueva_lista=list(filter(lambda x:x%2==0,lista))  
print(nueva_lista)

lista_alumnos=[
   

{
        "nombre":"abel",
        "edad":36,
        "semestre":2,
        
    },
    {
        "nombre":"antony",
        "edad":40,
        "semestre":2,
        
   
    },
    {
        "nombre":"edith",
        "edad":50,
        "semestre":2,
        

    }
]


lista_filtrada=list(filter(lambda x:x["edad"]<50,lista_alumnos))  
print(lista_filtrada)