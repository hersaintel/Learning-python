#Make a copy of a dictionary using the copy() method:
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
mydict = thisdict.copy()
print(mydict)

#Copy a dictionary to another dictionary by using the dict() function:
thisdict = { 
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
newdict = dict(thisdict)
print(newdict)