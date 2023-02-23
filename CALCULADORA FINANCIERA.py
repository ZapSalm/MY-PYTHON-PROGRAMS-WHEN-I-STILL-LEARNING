c=int(input("Cuanto es la cantidad a invertir? (en dolares) : "))
t=float(input("Cuanto es la tasa de interés? (en decimales) : "))
n=int(input("Por cuanto tiempo? (en años) : "))
print("La cantidad de",c, "dolares, a una tasa de",t,"anual, por",n,"años, da un capital final de:", c*(1+t)**n,"dolares")
