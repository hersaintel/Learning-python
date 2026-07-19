#The pop() method removes the items with the specified key name:
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang", 
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
    "brand": "Ford",
    "model" : "Mustang", 
    "year": 1964
}
thisdict.popitem()
print(thisdict)

#The del() keyword removes the item with the specified key name:
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

del thisdict["model"]
print(thisdict)

#The clear() method empties the dictionary:
thisdict = { 
    "brand": "Ford",
    "model": "Mustang", 
    "year": 1964
}
thisdict.clear()
print(thisdict)

#You can also delete a list of items by using the del() keyword:
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
del thisdict
print(thisdict)