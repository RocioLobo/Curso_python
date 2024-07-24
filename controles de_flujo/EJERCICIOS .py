1.#escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad1=int(input("ingresa primera edad:"))
if edad1>=18:
     print(" es mayor de edad")
else:
    print("menor de edad")


2.#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayusculas y minusculas.

contraseña = "rociolobo"
contraseña = input("Introduce la contraseña: ")
if contraseña == contraseña.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")




3.#Escribir un programa  que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atras desde ese numero hasta cero separados por comas.
numero=int(input("introduce un numero entero positivo:"))
if numero<0:
     print("no se permiten numeros negativos")
else:
     for i in range(numero,-1,-1):
        print(i, end=",")

# crear un programa que me muestra la tabla de multiplicar de 1 hasta 5


#crear un programa  que pida un numero y muestre la tabla de multiplicar de ese numero.

num:int=int(input("ingrese un numero por favor:"))
for n in range(1,12):
    resultado=num*n
    print(f"{numero}x{n}={numero*n}")





