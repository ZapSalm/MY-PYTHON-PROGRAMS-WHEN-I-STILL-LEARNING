#PROGRRAMA VALIDACION DE INICIO DE SESION
correct_user = "A123"
correct_password = "A123"
counter = 0

while counter < 3:
    user = input("Introduzca un nombre de usuario: ")
    password = input("Introduzca su contraseña: ") 
    
    
    if user == correct_user and password == correct_user:
        print("Inicio de sesion exitoso!")
        break
    else:
        counter +=1
        print("Usuario o contraseña incorrectos. Intentos restantes: ", 3 - counter)
    
if counter == 3:
    print("Usuario bloqueado, puede volver a intentar dentro de 10 minutos.")
    
