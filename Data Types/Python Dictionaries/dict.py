#Dictionaries are used to tore data values in key:value pairs
#A dictionary is a collection which is ordered, changable and don not allow duplicates
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))

#The values in dictionary items can be any data type:
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(type(thisdict))

#Use the dict() method to make a dictionary
thisdict = dict(name="John", age=30, country="Norway")
print(thisdict)