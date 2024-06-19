## Delcaración de Variables

## Declaración de Variables Simples (number,string,float,boolean)
x = 10
nombre = "Cristo Jesús"
pi= 3.14
es_mayor = True
print(x,nombre,pi,es_mayor)
info_completa = f"numer:{x}, nombre:{nombre}, pi:{pi}, boolean:{es_mayor}"
print(info_completa)

## Asignación de valores a múltiples variables en una sola línea
a, b, c = 1, 2, 3
print(a,b,c)

## Asignar el mismo valor a múltiples variables simultáneamente.
x = y = z = 0
print(x)

## Asignar elementos de una colección (como una lista o una tupla) a variables individuales
valores = (1,2,3)
x,y,z = valores
print(valores)

numeros =[4,5,6]
a,b,c = numeros
print(numeros)

 ## Asignación y operar sobre una variable en la misma línea.
x = 5
x += 8
x -= 7
x *= 5
x /= 10
print(x)

## Asignación diferentes tipos de valores a las variables.
entero = 10
flotante = 3.14
cadena = "Python"
booleano = True
lista = [1, 2, 3]
tupla = (4, 5, 6)
diccionario = {"nombre": "Juan", "edad": 21}
conjunto = {7, 8, 9}

print(diccionario)

## Tipado Explicito (opcional en Python)
celular: str = "Galaxy 20" ## String
pi: float = 3.141559 ## Flotante 
numero_celular: int = 66655165 ## Entero
es_mayor: bool = True ## Booleano
