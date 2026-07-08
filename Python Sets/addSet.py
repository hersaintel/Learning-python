#You can add set items using the add() method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#To add a set to another set use the update method
fruits = {1, 2, 3}
tropical = {"a", "b", "c"}
fruits.update(tropical)
print(fruits)
