password=input("Crea una nueva contraseña: ")
print("Bienvenido al portal!")
password_check=input("Introduzca su contraseña: ")
if password_check == password:
    print("Ha realizado con exito el inicio de sesion!")
else:
    print("Contraseña incorrecta, vuelve a intentarlo")