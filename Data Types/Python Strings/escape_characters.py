"""
To insert characters that are illegal in a string, use an escape character.
"""
#An escape character is a backslash \ followed by the character you want to insert.

#The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#\' Single quote
txt = 'It\'s alright.'
print(txt) 

#\\ Backlash
txt = "This will insert one \\ (backslash)."
print(txt) 

#\n new line
txt = "Hello\nWorld!"
print(txt) 

#\r carriage return
txt = "Hello\rWorld!"
print(txt) 

#\t tab
txt = "Hello\tWorld!"
print(txt) 

#\b backspace
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

#\f form feed

#\ooo octal value
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#\xhh hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 