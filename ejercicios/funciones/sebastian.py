# Datos correctos
usuario_correcto = "juan"
contrasena_correcta = "1234"

# Contadores
intentos = 0
errores_contrasena = 0
intentos_maximos = 3

# Ciclo con límite de intentos
while intentos < intentos_maximos:
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        print("¡Inicio de sesión exitoso!")
        intentos = intentos_maximos  
    else:
        if contrasena != contrasena_correcta:
            errores_contrasena += 1
        intentos += 1
        print(f"Credenciales incorrectas. Intento {intentos} de {intentos_maximos}.")

# Mensaje final si no se logró iniciar sesión
if usuario != usuario_correcto or contrasena != contrasena_correcta:
    print("Demasiados intentos fallidos. Acceso bloqueado.")

print(f"Número de veces que se ingresó una contraseña incorrecta: {errores_contrasena}")