#1.Diseñar un algoritmo que determine si el primero de dos números es el mayor
numero1:int=19
numero2:int=14
if numero1 > numero2:
    print("el primer numero es mayor que el segundo.") 
else:
        print("el segundo numero es mayor que el primero.")
        

#2.Algoritmo que calcule el promedio de tres números.
#determinar los numeros 
num1:int=15
num2:int=18
num3:int=10
promedio=(num1 + num2 + num3) / 3
print ("el promedio de los 3 numeros es:",promedio)


#3.Algoritmo que valide si un número se encuentra en el rango 1 a 100. 
#Determinar el numero
numero:int=57
if numero >= 1 and numero <= 100:
    print("el numero está dentro del rango 1 a 100.")
else:
        print("el numero no está dentro del rango 1 a 100.")


#4. Algoritmo que calcula el volumen de una esfera:
#determinar la radio de la esfera 
import math
pi =15
volumen = (4/3) * math.pi * pi**3
print("El volumen de la esfera es:", volumen)


#5. Algoritmo que calcula el área de un triángulo:
#ingresar y almacenar la altura y la base de un triángulo
base = int(input("ingrese la base del triangulo :"))
altura = int(input("Ingrese la altura del triangulo : "))
area = (base * altura) / 2
print("El área del triángulo es:", area)


#6. Algoritmo que determina si un viaje de ida y vuelta al sol a una velocidad constante igual a la de la luz:
#determinar la velocidad y distancia hasta el sol
velocidad_luz = 299792  # km/s
distancia_sol = 149.6  # millones de km
tiempo_ida = distancia_sol / velocidad_luz
tiempo_vuelta = distancia_sol /velocidad_luz
if tiempo_ida == tiempo_vuelta:
    print("El viaje de ida y vuelta al sol a la velocidad de la luz es posible.")
else:
    print("El viaje de ida y vuelta al sol a la velocidad de la luz no es posible.")


#7. Algoritmo que valida si un número es primo:
#ingresar un numero
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("el numero no es primo")
if numero % 2 == 1:
    print("el numero es primo")
    
    
#8. Algoritmo que compara si dos números son iguales, diferentes o si uno es el doble del otro:
#ingresar dos numeros
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1 == num2:
    print("Los números son iguales.")
elif num1 * 2 == num2 or num2 * 2 == num1:
    print("Uno de los números es el doble del otro.")
else:
    print("Los números son diferentes y ninguno es el doble del otro.")
    

#9. Algoritmo que calcula el área de un cuadrado:
#ingresar la longitud del cuadrado
lado = float(input("Ingrese la longitud del lado del cuadrado: "))
area = lado ** 2
print("El área del cuadrado es:", area)


#10. Algoritmo que convierte kilómetros a millas:
#ingresar la distancia en km 
kilometros = float(input("Ingrese la distancia en kilómetros: "))
#convertir los km a millas
millas = kilometros * 0.621371
print("La distancia en millas es:", millas)


#11. Algoritmo que dibuja un triángulo:
#ingresar la longitud del triángulo
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))
#dibujar un triangulo
if lado1 == lado2 and lado2 == lado3:
    print("El triángulo es equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
    

triangulo_uno=2*"               ."
print(triangulo_uno)
triangulo_dos=2*"             .   ."
print(triangulo_dos)
triangulo_tres=2*"          .         ."
print(triangulo_tres)
triangulo_cuatro=2*"        .             ."
print(triangulo_cuatro)
triangulo_cinco=2*"       ................."
print(triangulo_cinco)





#1.Escribir un programa que pregunte el nombre del usuario en la consola y un numero entero e imprima por pantalla en lineas distintas el nombre del usuario tantas veces como  el numero introducido.
nombre=input("ingrese su nombre:")
numero=int(input("ingrese un numero entero:"))
print((nombre +"\n")*numero)


#2.Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces.
nombre=input("ingrese su nombre completo por favor: ")
print(nombre)
print(nombre)
print(nombre)


#3.Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
numero_telf=input(" ingrese un numero de telefono con el formato +xx-xxxxxxxxx-xx: ")
print("el numero de telf es",numero_telf [4:-3])


#4.Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
nombre=input(" ingrese su nombre:\n")
sexo=input("ingrese su sexo como M o H:\n")
if sexo=="M":
  	if  nombre.lower()<"m":
  		   print("tu grupo es la A")
  	else:
  		   print("tu grupo es la B")
  	
else:
        if  nombre.lower()>"n":
	  	     print(" tu grupo es  la A")
        else:
	           print("tu grupo es la B")


#5.Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar s/.5 y si es mayor de 18 años, s/.10.
edad= int(input("ingrese edad por favor:\n"))
if edad <=4:
	print("puede entrar gratis")
elif edad >4 and edad<=18:
	print("debe pagar 5€")
else:
	print("debe pagar 10 €")
       