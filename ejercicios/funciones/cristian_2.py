# Ejercicio 2: Intersección de Listas
# Escribir una función que reciba dos listas y devuelva una nueva lista con los elementos comunes entre ambas (sin repetir).


def mi_funcion(lista1,lista2):
    
    return lista_combinada
    
# def lista1 (1, 2, 3, 4, 5): 
# def lista2 (4, 5, 6, 7, 8):
# def interseccion(lista1, lista2):
 
#     set1 = set(lista1)
#     set2 = set(lista2)
    
#     interseccion = set1.intersection(set2)
    
#     return list(interseccion)
clave=1234
intentos_fallidos=0
aviso=0
for intentos_fallidos in range(1,4):
        pin = int(input("ingrese clave "))
        if pin == clave:
            print("clave correcta")
            break
        else:
            intentos_fallidos+=1
            aviso+=1
            print("clave incorrecta",aviso)