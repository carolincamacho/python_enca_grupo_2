'''
El bucle for es una expresión para el control del flujo usada en programación donde
puedes definir el número de iteraciones en una parte del código.
objetos iterables

for <variable> in <objeto_iterable>:
    operaciones1
    operaciones2
'''

texto="Instituto"

for letra in texto:     #recorre la palabra que esta en la variable texto
    print(letra)

#-----------

mi_lista=[2,8,7,4]
elementos=0 #inicializamos una variable

for i in mi_lista:      #cuenta la cantidad de elementos de la lista
    elementos+=1 #contador que usa una variable inicializada por fuera

print(elementos)

mi_set={"a","b","caSa palMirA"}     

for dato in mi_set:
    dato1=dato.title() #Siempre la primera letra en mayúscula en cada palabra
    dato2=dato.capitalize() #La primera palabra con la primera letra en mayúscula
    print(dato1,dato2

)
 
mi_diccionario={
    "juana":26,
    "Diana":30
}

for clave in mi_diccionario:    #trae la primera parte del diccionario
    print (clave)
    
for clave,valor in mi_diccionario.items(): #El parentesis me trae el método o ejecuta
    print(clave, ":", valor)
    
for valores in mi_diccionario.values():     #trae la segunda parte del diccionario
    print(valores)
    
    
#---uso de ciclo while
'''
El ciclo while permite recorrer un objeto iterable
"mientras" se cumpla una condición
'''

j = 0
#pin='1234'

while j<=3: #condición
    
    j = j + 1
    print(j)
    

#Ejercicio: Verificar intentos de logueo

clave=1234
for intentos in range(1,4):
    if intentos <=3:
        pin = int(input("ingrese clave"))
        if pin == clave:
            print("ingreso exitoso")
        else:
            intentos_fallidos+=1
            print("clave erronea")