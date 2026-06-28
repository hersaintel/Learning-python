#Using the + operator
list1 = ["a", "b", "c"]
list2 = [1,2,3,]

list3 = list1 + list2
print(list3)

#Another way is by appending the items from list 2 into list1
list1 = ["a", "b", "c"]
list2 = [1,2,3]
for x in list2:
    list1.append(x)

print(list1)

#You can also use the extend() method to add list2 to list1
list1 = ["a", "b", "c"]
list2 = [1,2,3]

list1.append(list2)
print(list1)