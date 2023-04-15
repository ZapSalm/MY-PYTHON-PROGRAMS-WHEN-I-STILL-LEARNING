# GUIA PRACTICA BY ANGEL SALMERON. TODOS LOS DERECHOS RESERVADOS 2023-2023

# Hola! gracias por ver mi proyecto!, es una guia asignada por INSAFORP, estará en github (Hola profe!), con mis codigos hechos 100% por mi, sobre mis conocimientos,
# Cualquier correccion o duda hazmelo saber por discord : Zaptyz_ #6173

#Recomiendo profundamente ejecutarlo como yo lo hice, usando el shell de windows, que es la manera en la que se trabajó el proyecto :)

# RESPUESTA A LA PREGUNTA #1:
# Proponga el tipo de dato que utilizaría en los siguientes casos:

""" # DUI:

DUI = int(input("INTRODUCE TU DUI: ")) 

# Número de teléfono:

telefono = int(input("INTRODUCE TU NUMERO DE TELEFONO: "))

# Total, a pagar en una tienda:

total = print(float(19.99))

# Edad de una persona:

edad = int(input("INTRODUCE TU EDAD: "))

# Estado (activo o inactivo) de un usuario:

estado = bool(input("Estado actual?: (true=activo false=inactivo): "))

# Fecha de nacimiento de un empleado: INT() OR STR()

date = str(input("FECHA DE NACIMIENTO:  YYYY-MM-DD  "))
date = int(input("FECHA DE NACIMIENTO:  YYYY-MM-DD  "))

# Correo electrónico: STR()

email = str(input("INTRODUCE TU CORREO ELECTRONICO: ")) """


# RESPUESTA A LA PREGUNTA #2:
# Proponga dos ejemplos de valores que almacenaría en los diferentes tipos de datos vistos en la sesión de clase.

""" tipo_cadena = ("Esto es una cadena de texto") # Puras cadenas de texto
tipo_entero = (2030) # Numeros enteros
tipo_flotante = (0.5) # . flotantes
tipo_complejo = (1+1j) # Complejos
print(tipo_cadena)
print(type(tipo_cadena))
print(tipo_entero)
print(type(tipo_entero))
print(tipo_flotante)
print(type(tipo_flotante))
print(tipo_complejo)
print(type(tipo_complejo)) """

# RESPUESTA LA PREGUNTA #3

# En la empresa “El empleado feliz” se tomará como medida implementar la marcación por
# huella. El marcador por huella asocia dicha marcación al nombre del empleado, la fecha y
# hora en que registra la marcación, el código del empleado (el cual contiene sus iniciales y
# un número correlativo).
# De la descripción anterior se pide que defina el nombre de las variables para guardar la
# información, defina el tipo de dato de dicha variable y que escriba un ejemplo del valor que
# podría almacenar dicha variable.

""" DUI = int("Introduzca su huella/DUI : ")
nombre_del_empleado = str("Introduzca su nombre completo : ")
hora_Fecha = str("Introduzca la hora de entrada : ")
codigo_empleado = int("Introduzca el codigo de empleado correspondiente : ") """


# RESPUESTA A LA PREGUNTA #4
# Escriba una aplicación que permita validar si el usuario y contraseña ingresados son correctos,
# después de tres ingresos fallidos la aplicación deberá mostrar el mensaje de error “usuario bloqueado",
# puede volver a intentar dentro de 10 minutos”.

# PROGRRAMA VALIDACION DE INICIO DE SESION

""" correct_user = "A123"
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
    print("Usuario bloqueado, puede volver a intentar dentro de 10 minutos.") """
    
# EXPLICACION: Me costó pensar sobre cómo hacerlo, empecé con la idea de usar condicionales para el inicio de sesión y para la cantidad de intento que tiene,
# un contador, en este caso counter, se pone en la terminal el nombre de usuario y contraseña, tiene que coincidir con el que preestablecimos previamente,
# que en este caso es A123, tanto para user como password, el código va a estar en bucle si las credenciales no coinciden y se le sumará +1 al contador hasta llegar a 3,
# el número de intentos mas el print que avisará cuantos intentos llevamos, que es 3 – el numero que llevamos en counter, al llegar a 3,
# sale el mensaje que se bloqueará por 10 minutos. Sin embargo, si el condicional es verdadero, se detendrá diciendo el inicio de sesión es exitoso!

# RESPUESTA A LA PREGUNTA #5
# Cree una aplicación que determine si un número es par o impar.

# Par o impar?

""" num = int(input("Ingresa un número: "))
if num % 2 == 0:
    print(f"El número {num} es par")
else:
    print(f"El número {num} es impar") """
    
# EXPLICACION: Es un programa sencillo, en el cual se le pone un input para recibir el número, se le pone como int() para no poder ingresar otro tipo de dato
# y se hace una simple formula que si el numero es divisible entre 2, es par, de lo contrario es impar.

# RESPUESTA A LA PREGUNTA #6
# Crear una aplicación que solicite la edad al usuario y valide a través de un mensaje si “es
# mayor de edad” o si “es menor de edad”. La mayoría de edad se alcanza al cumplir los 18 años.

#Mayoria de edad

""" edad = int(input("Ingresa tu edad: "))

if edad > 18:
    print("Eres mayor de edad!")
else:
    print("Eres menor de edad...") """

# EXPLICACION: El programa funciona con un input() en int() y un condicional que si es mayor de 18, sale el print() de eres mayor de edad y viceversa.

# RESPUESTA A LA PREGUNTA #7
# Crear un programa que ordene de mayor a menor tres números ingresados por el usuario.

# Numeros iguales

""" num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

numeros = [num1, num2, num3]
numeros.sort(reverse=True)

print("Los números ordenados de mayor a menor son:", numeros) """

# EXPLICACION : Pedimos 3 numeros con input, lo asignamos como float() por si acaso el usuario decide usar punto flotante, luego ponemos los datos en una lista,
# y se usa la funcion .sort, se utiliza reverse=true para que sea de mayor a menor y lo ultimo es un print de los numeros ya ordenados.

# RESPUESTA A LA PREGUNTA #8

# Solicitar al usuario dos textos, comparar e indicar cuál de los dos contiene más caracteres.

# Cual es mas larga? XD

""" txt_1 = str(input("Introduzca su primera cadena : "))
txt_2 = str(input("Introduzca su segunda cadena : "))

txt_len_1 = len(txt_1)
txt_len_2 = len(txt_2)

if txt_len_1 > txt_len_2:
    print("La primera cadena ingresada es mas larga porque tiene : ", txt_len_1, "caracteres")
elif txt_len_1 < txt_len_2:
    print("La segunda cadena ingresada es mas larga porque tiene : ", txt_len_2, "caracteres") 
elif txt_len_1 == txt_len_2:
    print("Las dos cadenas tienen la misma cantidad de caracteres : ", txt_len_1) """
    
# EXPLICACION: Usamos if para ponerle una condicion, en la que si la primera cadena es mas larga le imprima el mensaje correspondiente y viceversa, tambien en el else
# pensé (que es bastante probable), sean iguales, entonces en el ultimo elif, puse que imprimiera que las cadenas son iguales. (no puse el else a pesar que al revisarlo
# me pareció que estaba bien, pero realmente no las estaba comparando, entonces puse el elif :D)
    
# RESPUESTA A LA PREGUNTA #9

# Cree una aplicación que solicite la edad y el sexo de un usuario e indique si la persona puede
# jubilarse tomando en consideración las reglas siguientes:
# Un hombre se puede jubilar si tiene 60 años o más y una mujer si tiene 55 años o más.

# PENSIONADOS

""" msg_1 = "No tienes la edad suficiente!" 
msg_2 = "Tienes la edad suficiente!"

jubilados = int(input("Cuantos años tienes? : "))
jubilados_1 = str(input("De que sexo eres? : "))

if jubilados >= 60 and jubilados_1 == "Masculino":
    print(msg_2)
elif jubilados >= 55 and jubilados_1 == "Femenino":
    print(msg_2)
else:
    print(msg_1) """
    
# EXPLICACION : Creé 2 mensajes, 1 de exito y el otro de fallo, que es msg_1 y 2, despues comparé los numeros ingresados, en este caso la edad, y dependiendo
# de que edad tenga, imprime un mensaje o otro.
    
# RESPUESTA A LA PREGUNTA #10 y #11

# En una tienda deportiva se tiene una promoción para la venta de camisas de la selección
# de El Salvador de la siguiente manera:
# Si se compran entre 1 y 3 camisas se aplica un descuento de 10%
# Si compran entre 5 y 8 camisas se aplica un descuento de 15%
# Y si se compran más de 8 camisas se aplica un descuento de 20%

# y el #11 : Cree un programa que solicite la cantidad de camisas, el precio unitario de la camisa y
# muestre como salida la compra sin descuento, el descuento y el total a pagar.


""" print("Hola!, bienvenido a nuestra tienda de camisas de la seleccion de EL SALVADOR EL MAS GRANDE PAPA!")
compra = int(input("Cuantas camisas va a llevar amor? : "))

if compra >= 1 and compra <= 3:
    print("Te llevas un descuento del 10%!")
    descuento = 0.1
elif compra >= 5 and compra <= 8:
    print("Te llevas un descuento del 15%!!")
    descuento = 0.15
elif compra > 8:
    print("Te llevas un descuento de 20%!!!")
    descuento = 0.2
else:
    print("La cantidad ingresada es invalida.")
    exit()
    
precio_camisa = 5.0
precio_total = compra * precio_camisa
descuento_aplicado = precio_total * descuento
precio_final = precio_total - descuento_aplicado

print(f"El precio final sin descuento aplicado es : {precio_total} usd y con descuento aplicado es : {precio_final} usd") """

# EXPLICACION: Aplica el descuento correspondiente al numero de camisas que se lleve, y luego asignamos cuanto vale cada camisa, y hacemos las operaciones que
# escribí, cuanto es el precio final, con el descuento y el precio final, luego le doy formato y pongo los precios con usd al final, gg.