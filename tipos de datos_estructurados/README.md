# tipos de datos estructurados(TDA - Tipos de datos abstractos) tenemos como la lista.
#lista 
- sus valores o elementos se pueden  actualizar, eliminar
lista=["abel",20,5.2,.5,false,["texto",.2]]
```pyton
#tupla
- sus valores o elementos no pueden ser modificados o eliminados.
tupla=("abel",20,5.2,False,[])
#diccionarios
 se e conoce como objetos

# los diccionarios almacenan los datos con clave y valor y te muestran el valor al imprimir 
diccionario={"nombre":"antonio","edad":15,"sexo":False}
```
-[!TIP]
-**obsercvacion:** que los tipos de datos estructurados pueden alamacenar en su interior otros tipos de datos estructurados

```pyton
lista_alumnos=[
   

{
        "nombre":"abel",
        "edad":20,
        "amigos":["no tiene"]
    },{
        "nombre":"ruth",
        "edad":18,
        "amigos":["flor","rocio"]

    },{
        "nombre":"jose ma",
        "edad":50,

    },{
        "nombre":"luz",
        "apellido":"jimenez",
        "edad":19,

    },{
        "nombre":"Rony",
        "edad":15,
        
    }
]

## METODOS
###1. convertir texto a lista
```pyton

#METODO LIST

te canbia los textos cortos.
texto="hola"2
list(texto)
#["h","o","l","a"]

# METODO SPLIT

son para textos largos , trosea texto  en una lista atravez de un limitador y lo separa como comas, puntos eslash etc.
texto="hola como estan alumnitos lindo"
texto.split(",")

texto_largo="loquitas_.mp4"
nuevo_texto=texto_largo.split(" ")
print(nuevo_texto)


#METODO JOIN
#con texto largo
texto_largo="este es un texto largo chiquititas y chiquititos"
nuevo_texto=texto_largo.split(" ")
print(",".join(nuevo_texto))

### 2.Agregar elementos al final de una lista
```pyton

# METODO APPEND - es un metodo que me permite agregar elementos al final de una lista
lista=["hola"]
lista.append("mundo")
print(lista)
#["Hola","mundo"]

#METODO INSERT -es el metodo que me permite agregar elementos en cualquier ubicacion de li lista
lista_nombres=["edith","ruth","LUZ"]
lista_nombres.insert(0,"antony")

### 3.Eliminar elementos de una lista
```pyton

#METODO POP - es el metodo que elimina el ultimo elemento de una lista es el contrario de append.

lista_nombres=["edith","ruth","LUZ"]
lista_nombres.pop() eliminara el ultimo nombre

#primera manera -METODO REMOVE -este metodo elimina el por el nombre el elemento que coincida dentro de mi lista.

lista_nombres=["edith","ruth","LUZ"]
lista_nombres.remove(edith) eliminara el nombre que coincida y escojas remove lo ase

#segunda opcion -METODO POP- al pasarle por parametro u n indice este lo eliminara de la lista.

lista_nombres=["edith","ruth","LUZ"]
lista_nombres.pop(0) eliminara por indice como 0 1 2 depende donde corresponde si no pones el indice automaticamente eliminara el ultimo.


### 4. Buscar un elemento en una lista

lista_nombres=["edith","ruth","LUZ"]
indice=lista_nombres.index("ruth")
print(lista_nombres[indice])  te mostrara el indice del nombre seleccionado.

pertenencia="edith" in lista_nombres #true False

```pyton

### 5. Comparación de listas: Podemos hacer uso de los operadores de comparación para comparar listas.
*Ejem:
```python
Comparar==[1,2,3]>[1,2,4]    # Se compara un elemento de la lista 1 con los elementos de la lista 2.
# El 1 no lo evalúa por que son iguales en ammbas listas.
# El dos no lo evalúa por que los elementos son iguales en ambas listas.
# El 3 si evalúa por que es menor que 4.
# Entonces la primera lista es menor que la segunda lista.
print(compara)
# Salida

### 6.cuidado con las copias


###7. FE DE ERRATAS (ACTUALIZAR LISTAS)
```
lista=[1,2,3,4,5,6]
lista[0]=2
print(lista)
te mostrara [2,3,4,5,6]

#modificando lista con diccionario
alumnos=[
    {
        "nombre":"abel",
        "edad":15
    },
    {
        "nombre":"antony",
        "edad":29

    }
]

alumnos[0]["edad"]=30
alumnos[0]={"nombre":"mafer","edad":15}
alumnos[1]["sexo"]="por definir
print(alumnos)



### 8. Listas y diccionarios por compreción:
 Es una técnica pythonica que nos permite crear listas y diccionarios en una sola línea combinando bucles y decisiones.
> [!NOTE]
> *VLC*
#  Crear una lista de números enteros del siguiente texto:
texto="1,4,8,9,6"
nueva_lista=[]
for n in texto.split(","):
    nueva_lista.append(int(n))
print(nueva_lista)
# aplicando la tecnica vlc valor bucle y condicion
texto="1,4,8,9,6"
nueva_lista=[int(n)for n in texto.split(",") if int (n)%2==0 ]            
print(nueva_lista)

# diccionarios por compresion

lista_amigos=["abel","antony","edith","ruth"]
diccionario={}
for _,v in enumerate(lista_amigos):
    diccionario[v]=len(v)
print(diccionario)

# aplicando elvlc

lista_amigos=["abel","antony","edith","ruth"]
diccionario={amigo:len(amigo) for amigo in lista_amigos}
print(diccionario)





