# # Ejercicio 2: Intersección de Listas
# # Escribir una función que reciba dos listas y devuelva una nueva lista con los elementos
# #  comunes entre ambas (sin repetir).

# def listas(lista_1,lista_2):
  
    
#     return lista_1,lista_2

# print(listas(["perro, foca, caballo"], ["ballena, foca, tiburon"]))


# # def listas(lista_1,lista_2):
# #     lista_1="perro, foca, caballo"
# #     lista_2="ballena, foca, tiburon"
# #     resultado=lista_1 + " " + lista_2
# #     return lista_1,lista_2

# # print(listas(["perro, foca, caballo"], ["ballena, foca, tiburon"]))




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
