
My_variable = "My string variable"

print(len(My_variable))

# len sirve para contar los caracteres de una cadena de texto, contando los espacios :D

# Variables en una sola linea. ¡No abusar de ello!

name, surname, alias, age = "Angel", "Salmeron", "Zaptyz", 19
print("Me llamo:", name, surname, ". Mi edad es:", age, ". y mi alias es:", alias)

# Inputs

name = input("Cual es tu nombre?")
age = input("Cuantos años tienes?")

print(name, age)

#Forzar tipo?

address: str = "Mi direccion"
address = 32
print(type(address))
