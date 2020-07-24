# Podemos generar números aleatorios basados ​​en probabilidades 
# definidas utilizando el choice()método del randommódulo.
# El choice()método nos permite especificar la probabilidad de cada valor.
# La probabilidad se establece mediante un número entre 0 y 1, donde 0 significa
# que el valor nunca ocurrirá y 1 significa que el valor siempre ocurrirá.
# Genere una matriz 1-D que contenga 100 valores, donde cada valor debe ser 3, 5, 7 o 9.

#a probabilidad de que el valor sea 3 se establece en 0.1
#La probabilidad de que el valor sea 5 se establece en 0.3
#La probabilidad de que el valor sea 7 se establece en 0.6
#La probabilidad de que el valor sea 9 se establece en 0

from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))

print(x)