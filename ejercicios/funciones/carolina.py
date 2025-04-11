# Ejercicio 2: Intersección de Listas
# Escribir una función que reciba dos listas y devuelva una nueva lista con los elementos comunes entre ambas (sin repetir).

def listas_comunes(lista1,lista2):
    numero_1=int (input ("favor digitar la cantidad de elementos de la primera lista: "))
    lista_conver1=set(lista1[numero_1])
    numero_2=int (input ("favor digitar la cantidad de elementos de la segunda lista: "))
    lista_conver2=set(lista2[numero_2])
    elementos_comunes=lista_conver1.intersection(lista_conver2)
    return elementos_comunes

#print(listas_comunes(["gato","perro"],["gallina", "perro","delfin"]))
