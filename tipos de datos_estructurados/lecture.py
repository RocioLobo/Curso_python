#LISTA
lista=["abel","antony","2miguel"]
print(lista[1])

#DICCIONARIO
diccionario=diccionario={"nombre":"antonio","edad":15,"sexo":False}
print(diccionario["nombre"])


#SPLIT
texto="hola"
lista_texto=list(texto)
print(lista_texto)

texto="hola"
lista_texto=list(texto)
lista2=[e for e in texto]
print(lista2)

#LIST
texto_largo="hola como estan bienvenidos al salon"
nueva_lista=texto_largo.split(" ")
print(nueva_lista)


#te mostrara solo del 16 para adelante ejm: bienvenidos al salon.
texto_largo="hola como estan bienvenidos al salon"
nuevo_texto=texto_largo[16:]
nueva_lista=nuevo_texto.split(" ")
print(nueva_lista)

#SPLIT
texto_largo="loquitas_.mp4"
nuevo_texto=texto_largo.split(" ")
print(nuevo_texto)


#JOIN al poner las comillas te separa si pones junto las comillas el texto saldra junto.y si pones un espacio el texto saldra con espacio.
texto_largo="loquitas_.mp4"
nuevo_texto=texto_largo.split("_")
print(" ".join(nuevo_texto))

#con texto largo : cuando quieres separar ya sea con comas puntos o espacios.
texto_largo="este es un texto largo chiquititas y chiquititos"
nuevo_texto=texto_largo.split(" ")
print(",".join(nuevo_texto)) 

#DATO PRIMITIVO

nombre="abel"
print(id("abel"))
otro_nombre=nombre
print(id(otro_nombre))

#Dato estructurado
lista_original=[1,2,3,4] 
copia_lista=lista_original

lista_original[-1]=15 #esto es lo modificado
print(copia_lista) #copia la referencia modificada

# crear un programa que reciba una lista desordenada y muestre por terminal una lista ordenada y la lista previa a ser ordenada.
lista=[4,76,1,3,6,8,2]
copia_lista=lista.copy()
copia_lista.sort()
print(lista)
print(copia_lista)



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
alumnos[1]["sexo"]="por definir"
print(alumnos)



# LISTAS Y DICCIONARIOS POR COMPRESION

#  Crear una lista de números enteros del siguiente texto:
texto="1,4,8,9,6"
nueva_lista=[]
for n in texto.split(","):
    nueva_lista.append(int(n))
print(nueva_lista)


#aplicando la tecnica vlc valor bucle y condicion
texto="1,4,8,9,6"
nueva_lista=[int(n)for n in texto.split(",") if int (n)%2==0 ]            
print(nueva_lista)


# diccionarios por compresion

lista_amigos=["abel","antony","edith","ruth"]
diccionario={}
for _,v in enumerate(lista_amigos):
    diccionario[v]=len(v) #te muestra el valor de la lista
print(diccionario)

# aplicando elvlc

lista_amigos=["abel","antony","edith","ruth"]
diccionario={amigo:len(amigo) for amigo in lista_amigos}
print(diccionario)
