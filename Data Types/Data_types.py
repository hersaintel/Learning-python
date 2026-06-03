"""
Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	dict
Set Types: 	set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview
None Type: 	NoneType
"""
#You can get the data type of any oject using type() function.
x=5
print(type(x)) #int

x=2.5
print(type(x))#float

x=1j
print(type(x))#complex

x="Hello, World!"
print(type(x))#str

x=["Apples", "Oranges"]
print(type(x))#list

x=("Bananas", "Carrots")
print(type(x))#tuple

x={"Bacon", "Beef"}
print(type(x))#set

x=True
print(type(x))#bool

x=range(6)
print(type(x))#range

x={"name":"John","Age":"39"}
print(type(x))#dict

x=frozenset({"Laptops","Signals"})
print(type(x))#frozenset

x=b"Hello"
print(type(x))#bytes

x=bytearray(5)
print(type(x))#bytearray

x=memoryview(bytes(5))
print(type(x))#memoryview

x=None
print(type(x))#nonetype

#If you want to specify the data type, you can use the following constructor functions:
x = str("Hello World") 	#str 	
x = int(20) 	#int 	
x = float(20.5) 	#float 	
x = complex(1j) 	#complex 	
x = list(("apple", "banana", "cherry")) 	#list 	
x = tuple(("apple", "banana", "cherry")) 	#tuple 	
x = range(6) 	#range 	
x = dict(name="John", age=36) 	#dict 	
x = set(("apple", "banana", "cherry")) 	#set 	
x = frozenset(("apple", "banana", "cherry")) 	#frozenset 	
x = bool(5) 	#bool 	
x = bytes(5) 	#bytes 	
x = bytearray(5) 	#bytearray 	
x = memoryview(bytes(5)) 	#memoryview