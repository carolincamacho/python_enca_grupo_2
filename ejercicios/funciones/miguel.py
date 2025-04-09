# Ejercicio 2: Intersección de Listas
# Escribir una función que reciba dos listas y devuelva una nueva lista con los elementos comunes entre ambas (sin repetir).


def listas():
    lista1=[1,5,7,8,9,4,3]
    lista2=[3,12,4,67,8,0]

    interseccion=lista1.intersection(lista2)

    return list(interseccion)

print(listas())


