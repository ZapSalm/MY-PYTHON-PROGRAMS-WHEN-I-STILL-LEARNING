#Lists

my_list = list()
my_other_list = []

print(len(my_list))
print(len(my_other_list))

my_list = [19,20,39,52,30,15,20]

print(my_list)
print(len(my_list))

my_other_list = [20, 1.81, "Angel", "Salmeron"]

print(type(my_other_list))

#Why 0? is the first position in a list, and i want to access to the first object, its "20" in this case, my age

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(20)) #.count is used to count the same elements in a list.
#print(my_other_list[4])  ERROR BECAUSE IS OUT OF RANGE IN THE LIST 
#print(my_other_list[-5])

age, height, name, lastname = my_other_list
print(name)

print(my_list + my_other_list)


my_other_list.append("Raspytech")
print(my_other_list)

my_other_list.insert(1, "Blue")
print(my_other_list)

my_other_list[1] = "Red"
print(my_other_list)

my_other_list.remove("Red")
print(my_other_list)

my_list.remove(20)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2])
print(my_new_list[1:3])

my_list = "Hola python"
print(my_list)
print(type(my_list))

