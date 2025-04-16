# Ejercicio 2: 
# Invertir diccionario
# Escribe una función que reciba un diccionario y retorne un nuevo diccionario donde las claves sean los valores
# y los valores las claves del original.

Products = {'Martillo': 15000, 'Cierra': 20000, 'Tornillo': 500, 'Destornillador': 8000 }

def invertir_diccionario():
    new_dic = {}
    for key, value in Products.items():
        new_dic[value]= key
    return new_dic

print(invertir_diccionario())