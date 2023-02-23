print("Lets play a game! you want to play?")
print("Lets play then!, Guess a number 1 to 20, you have 3 tries, lets guess!")
first_try=print(input("First try: "))
first_try=first_try
while first_try <= 7:
    print("No, is not that number, try again!")
else:
    print(input(" ** Second try ** "))
   # print(first_try,f"You guess the number!!! Congratulations!!!") 
   
   # No compila porque supuestamente el numero no aparece y aparece como None, fix it
   # Leer pagina 69 del libro python para todos libro 2 en 1 o algo asi, esta este reto con 3 condiciones:
    #El juego tiene un número secreto que el usuario final no puede ver. Supongamos que el número está fijado en 19. 
    #Permitiremos que el usuario tenga tres intentos para adivinar el número correctamente. El juego se completa de varias maneras posibles:
    #El usuario adivina el número correctamente antes de que se le acaben las vidas.
    #El usuario se queda sin las tres oportunidades y no puede adivinar el número.
    #El usuario adivina el número en el último intento.