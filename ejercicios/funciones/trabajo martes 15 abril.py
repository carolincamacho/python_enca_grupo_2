'''
Ejercicio 1: Contar vocales en valores
Escribe una función que reciba un diccionario cuyas claves son nombres y los valores son strings.
La función debe devolver un nuevo diccionario con la misma clave pero con la cantidad de vocales
en su valor.
'''  


estudiantes = {"angel":"osorio", "marta":"perez", "andres": "orozco"}

def contar_vocales_en_valores(diccionario):
    vocales = 'aeiouAEIOU'  
    diccionario_resultado = {}
    
    for clave, valor in diccionario.items():
        cantidad_vocales = sum(1 for letra in valor if letra in vocales)
        diccionario_resultado[clave] = cantidad_vocales
    
    return diccionario_resultado

print (contar_vocales_en_valores(estudiantes))
