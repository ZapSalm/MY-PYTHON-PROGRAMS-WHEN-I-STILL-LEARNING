# DICTIONARIES

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"name":"Angel", "Lastname":"Salmeron", "Age":20, 1:"Python"}

my_dict = {
    "name" : "Angel",
    "Lastname":"Salmeron",
    "Age": 20,
    "Languages" : {"Python", "Swift", "Kotlin"},
    1:1.77,
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))
# my_other_dict = 4
# and my_dict = 5
# why? because is the mount of elements in the dictionary

print(my_dict["name"])

my_dict["name"] = "Zaptyz"
print(my_dict["name"])

print(my_dict[1])

my_dict["Adress"] = "Adress Salmeron"

print(my_dict["Adress"])

print(my_dict)

del my_dict["Adress"]
print(my_dict)

print("Angel" in my_dict)
print("name" in my_dict)
print(my_dict["name"])
#print("Angelic" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_other_dict.fromkeys(("name", 1)))

my_new_dict = dict.fromkeys(("name", 1, "House"))
print(my_new_dict)
my_new_dict = dict.fromkeys((my_dict))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict,("Angel", "Salmeron"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict,"RaspyTech")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(list(dict.fromkeys(list(my_new_dict.values()))))
print(tuple(my_new_dict.values()))
print(set(my_new_dict))


capitals = {"USA" : "Washington D.C.",
            "India" : "New Dehli",
            "Russia" : "Moscow"}

#print(dir(capitals))
#print(help(capitals))

#print(capitals.get("USA"))
#print(capitals.get("India"))
#print(capitals.get("Russia"))
#print(capitals.get("Japan"))

#if capitals.get("Japan"):
#    print("That capital exist")
#else:
#    print("That capital doesn´t exist")

#capitals.update({"Germany" : "Berlin"})
#capitals.update({"China" : "Detroit"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()
#keys=capitals.keys()
#print(keys)

#for key in capitals.keys():
#    print(key)
    
#values = capitals.values()
#print(values)

#for value in capitals.values():
#    print(values)
    
#items = capitals.items()
#print(items)

items = capitals.items()

for key, value in capitals.items():
    print(f"{key}: {value}")