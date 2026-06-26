#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["apple","mango", "banana", "cherry"]
thislist.sort()
print(thislist)

#Sort the list numerically
thislist = [23,85, 1, 17, 75, 48]
thislist.sort()
print(thislist)

#Sort List objects in descending order

thislist = ["apple","mango", "banana", "cherry"]
thislist.sort(reverse = True)
print(thislist)

#Sort the list in descending order
thislist = [23,85, 1, 17, 75, 48]
thislist.sort(reverse = True)
print(thislist)

#You can also customize your own funtion by using the keyword argument key = function
#The functioon will return a number that will be used to sort the list(the lowest number first)
#Example: Sort the list based on close the number is to 50:

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#By default the sort() is case senstive, resulting in all capital letters being sorted before lower case letters:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#If you want acase sensitive sort function, use str.lower as a key function
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#To reverse the order of a list regardless of the alphabet use the reverse() method
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#