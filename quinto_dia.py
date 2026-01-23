# Arrays -- Listas
# Posicion:     0  1  2  3   4   5   6
# Dato:         2  5  6 100 "h"  3   i

lista = ["Hola", 1 , 2, 3j]
print(lista)

# Metodos de una lista 
lista2 = [1,2,3,4,5,6,7,8,9,0]
#Funcion append
print(f"Antes {lista2}")
lista2.append("x")    # Nos permite agregar un elemento a la lista - al final de la lista

#Funcion pop
print(f"Antes {lista2}")
var = lista2.pop()
print(var)
print(f"Despues {lista2}")

#Funcion index
print(lista2.index(7))

#Funcion remove
lista2.remove(8)
print(f"Lista eliminada: {lista2}")

#Ejercicio
#1   2   3   4   5    6
#   .                 7 
#  .                  8
# .                   9
#17                  10
#16  15  14  13  12  11
print(lista2[2])
#El tamaño de la lista 
print(len(lista2))
