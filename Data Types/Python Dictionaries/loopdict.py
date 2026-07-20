#You can loop through adictionary using a for loop:
#Print all the key names in the dictionary one by one:
thisdict = {
    "brand" : "Ford",
    "model": "Mustang",
    "year" : 1964
}
for x in thisdict:
    print(x)

#You can also use the values() method to return a list of all the values in the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict.values():
    print(x)
#Print both keys and values, by using the items() method:
thisdict = { 
    "brand": "Ford",
    "model": "Mustang", 
    "year": 1964
}
for x, y in thisdict.items():
    print(x,y)

#You can also loop through the keys of a dictionary by using the keys() method:
thisdict = {
    "brand": "Ford",
    "model": "Mustang", 
    "year": 1964
}
for x in thisdict.keys():
    print(x)
