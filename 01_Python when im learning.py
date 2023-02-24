# Nota para mi: Para hacer comentario varias lineas de codigo sin tener que ir 1 x 1, primero seleccionamos todo lo que se quiere hacer comentario y luego combinacion de teclas:
# CTRL+K Y despues CTRL+C, para quitarlo todo, se repite, se seleciona todo y se hace CTRL + k Y despues CTRL+U

###OPERADORES ARITMETICOS###

# suma
print (3+4)
#El resultado es 7, suma total
# resta
print (3-4)
# El resultado es -1, resta normal
# multiplicacion
print (3*4)
# El resultado es 12, multiplicacion normal
# Division
print (3/4)
#El resultado es 0.75, division normal
#Residuo de la division
print (10%3)
#El resultado es 1, operador de modulo, o mejor dicho el residuo de la division
#Division con resultado entero
print (10//3)
#El resultado es 3, el // realiza una division con resultado entero, na mas
#Exponente
print(2**3) 
#El resultado es 8, es 2 elevado a 3, ** significa exponente y el resultado es 8
#Todos los simbolos se pueden combinar sin importar los numeros, pero no se pueden usar en str
print(2+4**3//10%2+6-2)
#El resultado es 6, se pueden combinar en la misma cadena sin problema siempre y cuando sean numeros y no str.

#En str se pueden usar + y * para hacer un poco mas facil la codificacion: 
print("Hola soy Angel " + "Mucho gusto")
#Son 2 str, pero que pasa si lo combinamos con enteros? o numeros en general?
# print("Hola soy Angel " + 1)
#Da error, porque estamos combinando str con int.
#Ahora bien, si combinamos el * con str? que pasara?
print("Hola soy Angel " * 10)
#Se repite, en este caso, las 10 veces que le pusimos, es una manera de ahorrar codigo en mi punto de vista!
#Pero algo mas curioso, se puede usar los float para multiplicarlos? si, pero requiere un proceso:
# print("Hola soy Angel " * 2.5)
#De normal esto daria error, ya que es un float y no puede multiplicarse 2.5 veces, pero podemos hacer esto?
#print("Hola soy Angel " * ((2.5*2))
#No se puede, porque sigue siendo float, ciertamente 2.5 * 2 es 5, pero como estamos trabajando con float enrealidad es 5.0, la manera correcta seria:
my_float=  (2.5*2)
print("Hola soy Angel " * int(my_float))
#Porque funciona? porque transformamos 5.0 siendo float, a entero, entonces seria 5, y ahora si podria ejecutar las 5 veces "Hola soy Angel" !

###OPERADORES COMPARATIVOS###
#Mayor que
print(3>4) 
#Menor que
print(3<4)
#Mayor o igual
print(3>=4)
#Menor o igual
print(3<=4)
#Si hay igualdad
print(3==4)
#Distinto a
print(3!=4)

#CON STRS (Compara en un orden alfabetico por ASCII) (No cuenta caracteres)

#Mayor que
print("Hola">"Python") 
#Menor que
print("Hola"<"Python")
#Mayor o igual
print("Hola">="Python")
#Menor o igual
print("Hola"<="Python")
#Si hay igualdad
print("Hola"=="Python")
#Distinto a
print("Hola"!="Python")

#Porque para contar caracteres se le tiene que poner len al inicio para que cuente los caracteres, ejemplo:
print(len("Hola")>=len("Python"))
#Hola no es mayor a Python, porque Hola, tiene 4 caracteres y python tiene 6, por lo tanto es False.

### OPERADORES LOGICOS (REPASARLO, BASTANTE COMPLEJO, Y TAMBIEN REPASAR LAS TABLAS DE VERDAD!!!!)### 

print(3>4 and "Hola">"Python") 
print(3>4 or "Hola">"Python") 
#Or compara la logica booleana entre 2 operadores (en este caso), con que uno de los 2 sea true, sera true.
print(not(3>4))
#Not sive para negar toda la condicion