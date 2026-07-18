#Add items by using a new index key and assigning a value to it:
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang", 
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Add items by using the update() method:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year" : 1962
}

thisdict.update({"color":"red"})