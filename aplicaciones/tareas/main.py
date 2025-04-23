import tareas

print("Aplicación de administración de tareas")

while True:
    print("1. agregar tarea")
    
    opcion=input("Eliga una opcion: ")
    if opcion=="1":
        nueva=input("Ingrese la nueva tarea")
        tareas.lista_tareas.append(nueva)
    if opcion=="2":
        print(tareas.lista_tareas)
    if opcion=="3":
        lista=tareas.lista_tareas.remove("programar")
        print(lista)