# Ejercicio 2: Intersección de Listas
# Escribir una función que reciba dos listas y devuelva una nueva lista con los elementos comunes entre ambas (sin repetir).

# def listas_comunes(lista1,lista2):
#     lista_conver1=set(lista1)
#     lista_conver2=set(lista2)
#     elementos_comunes=lista_conver1.intersection(lista_conver2)
#     return elementos_comunes

# print(listas_comunes(["gato","perro"],["gallina", "perro","delfin"]))




clave=1234
intentosF=0

for intentos in range(1,4):
    pin = int(input("ingrese clave: "))
    if pin == clave:
        print("ingreso exitoso")
        break
    else:
        print("clave erronea")
        intentosF+=1
        print("intento fallido",intentosF)