#type conversion

#str
a=10.00
print(type(a))
print(type(str(a)))

print("#"*50)

#tuple
c="Rana"  #string
d=[1,2,3,4,5]#list
e={"A","B","C"}# set
F={"A":1,"B":2 }# Dictionary

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(F))

print("&"*50)

#list
c="Rana"  #string
d=(1,2,3,4,5)#tuple
e={"A","B","C"}# set
F={"A":1,"B":2 }# Dictionary

print(list(c))
print(list(d))
print(list(e))
print(list(F))

print("&"*50)
#set()

c="Rana"  #string
d=(1,2,3,4,5)#tuple
e=["A","B","C"]# list
F={"A":1,"B":2 }# Dictionary

print(set(c))
print(set(d))
print(set(e))
print(set(F))


print("&"*50)
#c="Rana"  #string
d=(("a", 1),("b",2),("c",3)) #tuple
e=[["one",1],["B",2],["C",3]]# list
#F={{"A","B" }# set


print(dict(d))
print(dict(e))
