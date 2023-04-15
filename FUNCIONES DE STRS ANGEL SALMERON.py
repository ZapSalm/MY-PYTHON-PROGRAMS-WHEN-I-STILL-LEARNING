#ALGUNAS FUNCIONES DE LOS STRS

ex_str = "EstoEsUnaCadena12"
my_list = ["Python", "CSS", "HTML", "CSS"]
print(ex_str.capitalize()) # Es para poner la primera letra en mayuscula y las que le siguen en minuscula

print(ex_str.center(100)) # Imprime la palabra de la variable con (en este caso) 100 caracteres en blanco con la palabra de la cadena en el medio

print(my_list.count("CSS")) # Regresa la cantidad de veces que un valor se repite dentro de una lista, en este caso "CSS" se repite 2 veces

print(my_list.index("Python")) # Imprime en que posicion esta la palabra, en este caso "HTML" en una lista.

print(ex_str.isalnum()) # Es para preguntar si es alphanumeric, o alfanumerico, cuenta de la a-z 0-9, los espacios no cuentan, por eso es False

print(ex_str.isalpha()) # Es para saber si son letras del alfabeto a-z, no cuenta espacios ni numeros

################################################################################################################################
tabla_de_traduccion = str.maketrans("ae", "xy")
nuevo = ex_str.translate(tabla_de_traduccion) # Se utiliza para remplazar caracteres en un string con otro conjunto de caracteres especificados
print(nuevo)
#   Y usando un dict():
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

#################################################################################################################################
txt = "50"
x = txt.zfill(100) # Llena la cadena con ceros hasta que llega a tener x caracteres de largo (incluyendo los caracteres que estan dentro de la variable str)
print(x)

#################################################################################################################################
#print(ex_str.rfind())    # Es un método de cadena que busca la posición de la última aparición de una subcadena en una cadena dada.
                         # La búsqueda se realiza de derecha a izquierda. Si la subcadena no se encuentra en la cadena dada, rfind() devuelve -1.
cadena = "Fola que tal, espero que hayas aprendido a capturar, pokemons"
posicion = cadena.rfind("pokemons")
print(posicion)