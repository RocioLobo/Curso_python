#1.Utilizando operadores de comparación, determina si un numero introducido por el usuario tiene una longitud mayor o igual10
numero_usuario:str=input('ingrese por favor un numero: ')
longitud=len(numero_usuario)
comparar=longitud >= 3 and longitud < 10
print(comparar)


#2.Determinar si un número ingresado por el usuario es par y mayor que 10.
numero_usuario:int=int(input("ingrese numero: "))
#imprimir
print("numero ingresado es par:", numero_usuario %2==0)
print("numero ingresado es impar:", numero_usuario %2==1)
print("numero ingresado mayor que 10:", numero_usuario>10)
print("numero ingresado menor que 10:", numero_usuario<10)