#The union() method returns a new set from all items of sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#You can use the | operator
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

#Join multiple methods using the union() method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Doe"}
set4 = {"apples", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#Use | operator to join more sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Doe"}
set4 = {"apples", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)

#Join a set with another data type
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

#Using the update() method
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#The intersection() method will return a new set, that only contains the items that are present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"linux", "android", "apple"}
set3 = set1.intersection(set2)
print(set3)

#You can use the & operator instead of intersection()
set1 = {"apple", "banana", "cherry"}
set2 = {"linux", "android", "apple"}

set3 = set2 & set1
print(set3)

#The intersection_update() method will also keep only the duplicates, but will change the original set instead of returning a new set
set1 = {"apple", "banana", "cherry"}
set2 = {"linux", "android", "apple"}

set1.intersection_update(set2)
print(set1)

#The values True and 1 are considered the same value. The goes for False and 0
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {1, "linux", False, "android", True, "apple", 2}
set3 = set1.intersection(set2)
print(set3)

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set
set1 = {"apple", "banana", "cherry"}
set2 = {"linux", "android", "apple"}
set3 = set1.difference(set2)
print(set3)

#You can use the - operator to get the same result
set1 = {"apple", "banana", "cherry"}
set2 = {"linux", "android", "apple"}
set3 = set1 - set2
print(set3)

#Use the difference_update method to keep only the items from the first set that are not present in the other set
set1 = {"apple", "banana", "cherry"}
set2 = {"linux", "android", "apple"}
set1.difference_update(set2)
print(set1)

#The symmetric_difference() method will keep only the elements that are not present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"linux", "android", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

#You can use the ^ operator instead of symmetric_difference() to get the same result
set1 = {"apple", "banana", "cherry"}
set2 = {"linux", "android", "apple"}
set3 = set1 ^ set2
print(set3)

#Use the symmetric_difference_update() method to keep the items that are not present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"linux", "android", "apple"}
set1.symmetric_difference_update(set2)
print(set1)