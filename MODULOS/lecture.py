# """practicando pylint""" #cuando es variable especificar el tipo de dato ya sea entero o texto.
# nombre_alumno:str="miguel"

# def suma(a:int,b:int)->int:
#     """funcion para sumar dos numeros"""
#     return a+b
# print(suma(4,7))

# def resta(a,b):
#     """funcion para restar dos numeros"""
#     return a-b
# importacion directa
import operaciones
suma=operaciones.suma(7,8)
msj:str=f"{operaciones.mensaje},como estas"
print(suma,msj)
