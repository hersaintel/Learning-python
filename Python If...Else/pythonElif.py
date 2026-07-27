#The elif keyword is Pythons way of saying "if the previous conditions were not true, then try this condition":
a = 18
b  = 18
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

#You can have as many elif conditions as you need:
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")

#Categorizing age groups:
age = 25

if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 60:
    print("You are an adult")
elif age >= 65:
    print("You are a senior")

day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Sartuday")
elif day == 7:
    print("Sunday")