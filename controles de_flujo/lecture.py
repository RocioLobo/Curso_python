
#ejemplo de for
#imprimir los numeros pares
#entre 1 -20
for n in range(1,21):
    if n%2==0:
        print(n)

#crear un programa que me imprima las 5vocales
vocales:str="aeiou"
for n in range (0,5):
    print(vocales[n])

# crear un programa que me muestre los 8 primeros numeros pares.
contador=0
for n in range (1,17):
    if n%2==0:
        contador+=1
        print(f"{n} es el numero{contador} ")

# crear un programa que pida al usuario escribir una oracion
# y mostrar por terminal la cantidad de vocales a que
# tiene esa oracion
# OJO:SOLO LAS "a" MINUSCULA

oracion:str=input("escribe una oracion: ")
contador:int=0
for n in range(0,len(oracion)):
    if oracion[n]=="a":
        contador=contador+1
        #contador+=1
print(f"la cantidad de letras a que  tengo e es {contador}")

# cear un programa que me comente la cantaidad de comas y me muestre
#sus indices.
#OJO. tiene que pedir al usuario

oracion:str=input("ingrese una oracion:")
contador:int=0
for indice,letra in enumerate(oracion):
    if letra ==",":
        print(f"su indice es {indice}")
        contador+=1
print(f" la cantidad de comas es {contador}")

#escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido(desde 1 hasta su edad).

edad:int=int(input("ingrese edad por favor:"))
for i in range(1,edad+1):
    print("año",i,"cumplido")

#crear un programa que me pida el nombre de tres personas y guarde una variable global la ultima letra de sus nombres.
#mostrar por pantalla la variable global con las tres ultimas letras del nombre de cada persona.
#pedir tres nombres de tres personas
ultima_letra:str=""
for i in range(3):
   nombre:str=input("escribe tu nombre:")
#ultima_letra+=nombre[-1]
   last_letter:str=nombre[-1]
   ultima_letra+=last_letter
#ultima_letra=ultima_letra+last_letter
print(ultima_letra)

#crear un programa que muestre por terminal la siguiente figura:
#a
#ee
##iii
#0000
#uuuuu


# ejemplos de if - else primer ejemplo de if estructurado:

edad:int=int(input("escribe tu edad"))
if edad>18:
    print("eres mayor")
else:
    print("eres menor de edad")


 #EJEMPLOS while
condicion=True
while condicion:
    print("hola")
    

#Ejemplos

condicion=True
while condicion:
    eval=input("desea continuar[s/n]:")
    if eval=="s":
        print("continuas en el bucle")
        continue
    else:
        print("se termino el programa")
        condicion=False
        break

contador=0
while contador<=5:
    print(contador)
    contador+1
print(f"valor final{contador}")

# METODOS DE STRING -array

nombre="jose"
nombre.upper()# convierte el texto en mayuscula

apellidos="alvarez"
apellidos.lower() #convierte el texto en minuscula


segundo_nombre="luis"
print(segundo_nombre.capitalize()) #convierte la primera letra en mayuscula.


# crear un programa que pida la cantidad de notas que se debe registrar luego pedira las  notas e imprimira el promedio.
condicion =True
while condicion:
    cant=input(" igrese la cantidad de notas: ")
    if cant="cant"

