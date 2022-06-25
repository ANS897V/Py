#Set
# a={1,3,4,5,1}
# print(a)
# print(type(a))

#This will create empty dictionary and not empty set
a={}
print(type(a))


#An empty set will be created by this syntax
b=set()
print(type(b))
b.add(4)
b.add(6)
b.add((3,5,6)) #tuples can be added in the set whereas list and dictionary can be added
b.add(6) # will not add repetitive values
print(b)

print(len(b)) #Returns length of the set

b.remove((3,5,6)) #remove (3,5,6) from set
print(b)