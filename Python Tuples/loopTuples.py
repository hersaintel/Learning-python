#You can loop the tuple items using a for loop:
#Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

#You can also loop through the tuple items by referring to their index number;
#Use the range() and len() functions to create a suitable iterable

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple)

#You can loop theougha tuple items using a while loop. Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes. Also remember to increase the index by 1

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i+1