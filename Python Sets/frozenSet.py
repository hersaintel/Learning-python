#Frozen set is an immutable type of a set and items cannot be removed.
#Use the frozenset() constructor to create a frozenset from any iterable
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

#Return a copy of a frozenset
x = frozenset({1, 2, 3})
y = x.copy()
print(y)
print(x)

#Return the difference
a = frozenset({1,2,3,4})
b = frozenset({3,4,5})
print(a.difference(b))
print(a - b)

#Return a frozenset with intersection
a = frozenset({1,2,3,4})
b = frozenset({3,4,5})
print(a.intersection(b))
print(a & b)

#Return true if there is no intersection between frozensets
a = frozenset({1,2})
b = frozenset({3,4})
c = frozenset({4,5})
print(a.isdisjoint(b))
print(b.isdisjoint(c))

#Return True if a frozenset is a proper subset of another
a = ({1,2,3})
b = ({2,3})
print(b.issubset(a))
print(b < a)
print(b <= a)

#Return True if a frozenset is a proper superset of another
a = frozenset({1,2,3})
b = frozenset({1,2})
print(a.issuperset(b))
print(a > b)
print(a >= b)

#Return frozenset with the symmetric_differences
a = frozenset({1,2,3,4})
b = frozenset({3,4,5})
print(a.symmetric_difference(b))
print(a ^ b)

#Return a new frozenset with a union
a = frozenset({1,2,3})
b = frozenset({3,4,5})
print(a.union(b))
print(a | b)
