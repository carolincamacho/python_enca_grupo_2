# Ejercicio 2: Intersección de Listas
# Escribir una función que reciba dos listas y devuelva una nueva lista con los elementos comunes entre ambas (sin repetir).

List_1 = [1,2,3,4,5,6,6]
List_2 = [5,6,7,8,9,10]

def inter_listas(a,b):
    return list(set(a) & set(b))

print(inter_listas(List_1, List_2))