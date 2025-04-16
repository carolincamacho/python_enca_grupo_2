# # Ejercicio 2: Intersección de Listas

# # Escribir una función que reciba dos listas y devuelva una nueva lista con los elementos comunes entre ambas (sin repetir).

 

# def listas_comunes(lista1,lista2):

#     numero_1=int (input ("favor digitar la cantidad de elementos de la primera lista: "))

#     lista_conver1=set(lista1[numero_1])

#     numero_2=int (input ("favor digitar la cantidad de elementos de la segunda lista: "))

#     lista_conver2=set(lista2[numero_2])

   

#     elementos_comunes=lista_conver1.intersection(lista_conver2)

#     return elementos_comunes

 

# #print(listas_comunes(["gato","perro"],["gallina", "perro","delfin"]))

 

#Carolina-Cristian

# Ejercicio 4: Clasificar edades

# Crea una función que reciba un diccionario con nombres y edades.

# La función debe devolver un nuevo diccionario con tres claves: "niños", "adultos" y "mayores",

# agrupando los nombres según su edad (<13, 13-59, 60+).

 

empleados={

    "carolina":74,

    "cristian":32,

    "julian":12,

    "Andres":6,

    "guille":50

}

 

#edades ={}

 

def clasificar (diccionario):

    clasificados={"niños":{},"adultos":{},"mayores":{}}

    for clave,valor in diccionario.items():

        if valor<13:

            #edades.update({"niños":{clave:valor}})

            #edades[clave]=valor

            clasificados["niños"][clave]=valor

        elif valor>60:

            #edades.update({"Mayores":{clave:valor}})

            #edades[clave]=valor

            clasificados["mayores"][clave]=valor

        else:

            #edades.update({"Adultos":{clave:valor}})

            #edades[clave]=valor

            clasificados["adultos"][clave]=valor

       

    return clasificados

print(clasificar(empleados))


