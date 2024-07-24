#controles de flujo
todos los programas trabajan a travez de instrucciones ordenadas.
existen maneras de romper con el flujo normal de los programas creando `bifurcaciones` o creando `repeticion` de instrucciones.
## decisiones
## la sentencia if
la sentencia de decicion en pyton es `if` .en su estructura debemos añadir una **exprecion de comparacion** terminando con `:` al final de la linea
> ejemplo:

```python
if true:
    print("es verdad")
```
`>else - elif`

```pyton
edad:int=(input("escribe tu edad"))
if edad>=18:
print("eres mayor")
else:
    print("eres menor de edad")
    
```
## segundo ejemplo if almacena do en variables:
```python
edad_dos:int=int(input("escribe tu edad:"))
respuesta:str="eres mayor" if edad_dos>=18 else "eres menor"
print(respuesta)
```


## ciclos
son los controles de flujo que repiten codigo
y sintaxis en la siguiente
### for

> para for:
``` pyton
# este codigo imprime los numeros
# del 1 al 10
for n in range (1;11):
    print(n)

## ejemplo
## for n in  "aeiou" te permite mostrar las letras
    print(n)
## for i,l inenumerate("aeiou") permite mostrar el indice y la letra
       print(f" el indice es{i} y la letra es {l}")

# espacios de memoria qe ocupan
##`range` es el que ocupa menos memoria
## oraciones medianas en **in** es mas lenta pero menos memoria
## enumerate cuando las oraciones son pequeñas mas memoria
## enumerate en oraciones largas  ocupa  menos memoria


```
>### para while
Es un mecanismo que usa `pyton` para repetir instrucciones, la semantica es la sentencia es: `mientras se cumpla la condicion has algo` 
```
pyton
while():true  siempre imprimira verdad
    print("hola")
    
> 

