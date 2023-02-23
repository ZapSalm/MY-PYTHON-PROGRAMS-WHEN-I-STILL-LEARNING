print("Bienvenido a mi pequeño juego")
number = int(input("Elige un número entre 1-3:"))
if number == 1:
    print("Te encanta considerarte un líder, ¿verdad?")
elif number == 2:
    print("Odias estar solo, ¿verdad?")
elif number == 3:
    print("Cuanto más, mejor, ¿no?")
number2 = float(input("Introducir un número con una cifra decimal entre 1 y 2: "))
if number2 == 2.00:
    print("¡Está bien! ¡Quise decir un poco menos que eso!")
elif number2 <= 1.50:
    print("¡Oh, vamos! ¡Puedes ir más alto!")
elif number2 == 3.00:
    print("Te gusta romper las reglas, ¿no?")
    print("Sabes qué, olvídalo!")
else:
    print("¿En serio? No puedes seguir instrucciones simples, ¿verdad?")