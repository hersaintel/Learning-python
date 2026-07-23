#A dictionary can contain dictionaries, this is called nested dictionaries:
myfamily = {
    "child1" : {
        "name":"Emil",
        "year": 2004
    },
    "child2":{
        "name":"Tobias", 
        "year": 2007
    },
    "child3":{
        "name":"Linus",
        "year": 2010 
    }
}
print(myfamily)
print(myfamily["child2"]["name"]) #Access items in nested dictionary
#You can loop through a dictionary by using the items() method:
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])