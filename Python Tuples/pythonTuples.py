#Tuple items are unchangable
mytuples = ("apple", "banana", "cherry")
print(mytuples)

#Python tuples are ordered, unchangable and allow duplicates
mytuples = ("apple", "banana", "cherry", "cherry", "banana")
print(mytuples)

#Print the number of items in a tuple
mytuples = ("apple", "banana", "cherry", "cherry", "banana")
print(len(mytuples))

#To create a one item tuple remember the comma after the item:
mytuple = ("apple",)
print(mytuple)

#Atuple can have integers, strings and boolen values:
tuple1 = ("abc", 34, True, 40, "male") 
print(tuple1)

#What is the data type of tuples
tuple1 = ("abc", 34, True, 40, "male")
print(type(tuple1))

#Create a tuple using the tuple() constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)