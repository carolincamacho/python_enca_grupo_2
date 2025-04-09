'''
Funciones:
En python como en cualquier otro lenguaje podemos personalizar las instrucciones 
necesarias para resolver un problema
esas instrucciones pueden quedar opcionalmente escritas en lo que denominamos funciones

input()
int()
float()

sintaxis de una función:


def <nombre>(opcionalmente argumentos):  # el def es solo para definir funciones.
    operaciones
    
    return <resultado>

'''
variable1=100

#Ejemplo 1:

def sumar(): #No tiene argumentos
    x=2
    y=5
    return x+y

print(sumar())
    
def sumar_2(x,y): #Hay dos argumentos que son requeridos para operar
    
    
    return x + y

x=40

print(sumar_2(x,7)) #llamar a la funcion es abrir y cerrar parentesis()


def operar(dato1,dato2):
    #esta función concatenará dos textos
    dato1=dato1.lower()
    dato2=dato2.lower()
    respuesta=dato1 + " " + dato2
    
    return respuesta

print(operar("instituto", "Enca24"))


#Funciones con argumentos opcionales
def ejemplo(y,z,w,x=5): #Una función puede tener argumentos opcionales
                        #y,z,w son obligatorio y la X es opcional porque esta definida
    return str(x) #Str lo devuelve como texto

print(type(ejemplo(9,2,6)))
    

    