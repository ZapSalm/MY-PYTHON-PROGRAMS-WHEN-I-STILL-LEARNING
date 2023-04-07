# SETS

#PRINCIPAL DIFERENCE IS, A SET IS NOT THE SAME WITH A LIST, BECAUSE A SET IS NOT A SORT STRUCTURE, AND ADD DISORDERLY AND KEEPS DISORDERLY
#A SET CANNOT ADD REPEATING ELEMENTS
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #initialment is a DICT

my_other_set = {"Angel", "Salmeron", "20"}

print(type(my_other_set)) #In this point is a set

print(len(my_other_set))

my_other_set.add("Zaptyz")
print(my_other_set)

my_other_set.add("Zaptyz")
print(my_other_set)

print("Angel" in my_other_set)
print("Angelic" in my_other_set)

my_other_set.remove("Angel")
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

del my_other_set 
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Angel","Raspy", "Minecraft"}
my_list = list(my_set)
print(my_list[0])

my_other_set = {"Python", "CSS", "HTML", "JavaScript"}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union(my_set).union("C#")) #SE PUEDEN AÑADIR ELEMENTOS SOLO SI NO SON PROPIOS DE LOS SETS, QUE SEAN NUEVOS COMO POR EJEMPLO "C#", LOS ELEMENTOS REPETIDOS NO VAN

print(my_new_set.difference(my_set)) #PORQUE NO APARECEN LOS NUEVOS AGREGADOS COMO POR EJEMPLO "C#"? PORQUE SOLO FUE PARA EL PRINT, NO TIENEN VARIABLE ASIGNADA

