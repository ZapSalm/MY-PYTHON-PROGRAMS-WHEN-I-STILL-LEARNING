name, lastname, adress, age, country = "Angel","Salmeron","San Miguel",19,"El Salvador"
#OPTIMAL ONE
print(f"My name is {name} {lastname}, i live in {adress}, in {country}, and my age is {age}")
#OTHER WAYS TO MAKE IT
print("Hi, my name is %s %s, i live in %s, in %s, and my age is %d"%(name,lastname,adress,country,age))
print("Hi, my name is {} {}, i live in {}, in {}, and my age is {}".format(name,lastname,adress,country,age))
age=19
txt="My name is Angel and i am {} years old"
print(txt.format(age))

#PRACTICE LISTS

My_First_List = [20,19,20,20,21,18]
My_Second_list = [4,5,6]
#OR

#My_First_List = list(20,19,20,20,21,18)

print(len(My_First_List))
print(type(My_First_List))
print(My_First_List.count(20))
My_First_List.append("Derkaa")
print(My_First_List)

My_First_List.remove("Derkaa")
print(My_First_List)

My_First_List.extend(My_Second_list)

print(My_First_List)

My_First_List.append("Zaptyz")
print(My_First_List)

print(My_First_List.count(20))

#My_First_List.sort() ONLY FOR STR, THIS FUNCTION SORT THE LIST ALPHABETICALLY

#My_First_List.clear()
#print(My_First_List)

My_First_List.insert(0,"Hi")
print(My_First_List)

print(My_First_List.index("Zaptyz"))

Removed_element=My_First_List.pop(0)
print(Removed_element)
print(My_First_List)
