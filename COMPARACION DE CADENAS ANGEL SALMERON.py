txt_1 = str(input("Introduzca su primera cadena : "))
txt_2 = str(input("Introduzca su segunda cadena : "))

txt_len_1 = len(txt_1)
txt_len_2 = len(txt_2)

if txt_len_1 > txt_len_2:
    print("La primera cadena ingresada es mas larga porque tiene : ", txt_len_1, "caracteres")
elif txt_len_1 < txt_len_2:
    print("La segunda cadena ingresada es mas larga porque tiene : ", txt_len_2, "caracteres") 
else:
    print("Las dos cadenas tienen la misma cantidad de caracteres : ", txt_len_1)