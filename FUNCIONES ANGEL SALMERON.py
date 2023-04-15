""" def hola(nombre ="Anonimo"):
    if nombre == "Anonimo":
        print("hola we")
    else:
        print(f"Hola {nombre} bienvenido al curso de Python de la Academia")

name=input("Cual es tu nombre?")
hola (name)
 """
""" def maximo(lista):
    max = 0
    for x in lista:
        if x > max:
            max = x
    return max

lista = [34,1,23,19,9,15,4,2,35,100]
maximo = maximo (lista)

print (maximo) """

""" def minimo(lista):
    min = 1000000000000000
    for x in lista:
        if x < min:
            min = x
    return min

lista = [34,1,23,19,9,15,4,2,35,100]
minimo = minimo (lista)

print (minimo) """

def area(ancho,largo):
    area = ancho * largo
    
    return area

ancho = float(input("Cual es el ancho de tu rectangulo? en centimentros "))
largo = float(input("Cual es el largo de tu rectangulo? en centimentros "))

print(f"El area de tu rectangulo es " + str(area(ancho,largo)) + " centimentros cuadrados")