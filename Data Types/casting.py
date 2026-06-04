"""
Casting in python is done using constructor functions:

    int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
    float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
    str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

"""
#Integers
x = int(3) #x will be 3
y = int(4.8)#y will be 4
z = int("9") #z will be 9

#Float
x = float(3) #x will be 3.0
y = float(4.8)#y will be 4.8
z = float("9")#z will be 9.0

#String
x = str(3)#x will be "3"
y = str(4.8)#y will be "4.8"
z = str("m2")#z will be "m2"