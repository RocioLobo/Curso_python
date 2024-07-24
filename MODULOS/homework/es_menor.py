"""modulo es menor"""
def f_es_menor(lista:list): #las anotaciones son importantes
    """funcion para saber el numero de una lista"""
    menor=lista[0]
    for n in lista:
        if n < menor:
            menor=n
    return menor

