mi_lista=[
          {"nombre": "estudiar", "completada":False}, 
          {"nombre": "programar", "completada":False},
          {"nombre": "dormir", "completada":False}
          ]

for i, tarea in enumerate(mi_lista):
    estado="ok" if tarea["completada"] else "no"
    print(f"{i+1}. {tarea['nombre']}[{estado}]")

def ejemplo():
    global x
    x=3
    return "función sin salida"

print(ejemplo())
print(x)