#You can access the items of a dictionary by referring them to its key name inside square brackets:
thisdist = {
    "brand": "Ford",
    "model" : "Mustang",
    "year": 1964
}
x = thisdist["model"]
print(x)

#There is also a method called get() that will give you the same result:
y = thisdist.get("model")
print(y)
#Get Keys
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1964
}
x = thisdict.keys()
print(x)

#The list of the keys is aview of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
print(x)

car["color"] = "red"
print(x)

#The values method will return a list of all the items in the dictionary.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.values()
print(x)

#The list of the values is a view of the dictionary, meaning that any changes done will be reflected in the values list.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)

car["year"] = 2020
print(x)

#Add a new item to the original dictionary and see that the values list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
car["color"] = 'red'
print(x)

#The items() method will return each item in a dictionary as tuples in a list.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.items()
print(x)

#The returned list is a view of the items of the dictionary meaning that any changes done to the dictionary will be reflected in the items list.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)
car["year"] = 2020
print(x)

#Add anew item to the original dictionary, and see that the items list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)
car["color"] = "Red"

print(x)

#To determine ifa specified key is present in a dictionary use the in keyword:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in car:
    print("yes, 'model' is one of the keys in the car dictionary")