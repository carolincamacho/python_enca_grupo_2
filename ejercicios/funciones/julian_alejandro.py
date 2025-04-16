# Ejercicio 3: Filtrar productos con stock
# Escribe una función que reciba un diccionario de productos con su cantidad disponible.
# La función debe retornar un nuevo diccionario que solo contenga los productos con cantidad mayor
#a cero.

# archivo se llama julian_alejandro.py

def filtrar(diccionario):
    nuevo_diccionario={} 
    for  clave,valor in diccionario.items():
        if valor>= 0:
            nuevo_diccionario.update({clave: valor})

    return nuevo_diccionario        
          #  print(clave, ":", valor)
          #  resultado = print(diccionario)
         #   return resultado

productos = {"iphone": 7,
                "laptop": 10, 
                "mouse": -2,
                "teclado": -1, 
                "diadema": 18}

articulos = {"microfono": 30,
                "control": -10, 
                "padmouse": -40,
                "monitor": -11, 
                "pantalla": 8}

print(filtrar(productos))
print(filtrar(articulos))