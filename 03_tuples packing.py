# TUPLES, a difference of tuple to the list, is inmutable

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (20, 1.81, "Angel", "Salmeron")
my_other_tuple = (20,30,50,35)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) INDEX ERROR
#print(my_tuple[-6]) INDEX ERROR

print(my_tuple.count("Salmeron")) #Found the quantity of "Salmeron" in the tuple, in this case 1
print(my_tuple.index("Angel")) #Found in what position are "Angel" in the tuple, in this case 2
print(my_tuple.index("Salmeron"))

#my_tuple[1] = 1.85 "tuple" object doies not support item assignment
my_sums_tuple=my_tuple + my_other_tuple
print(my_sums_tuple)

print(my_sums_tuple[3:6])

my_tuple=list(my_tuple)
print(type(my_tuple))

my_tuple[2] = "RaspyTech"
my_tuple.insert(1, "Blue")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple[2] TypeError: "tuple" object doesn´t support item deletion

del my_tuple

#print(my_tuple) NameError: name "my_tuple" is not defined