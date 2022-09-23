#set   ------ not order abd not indexed
mySetOne = {"Ahmad", "Daka", 100}
print (mySetOne)
#print (mySetOne[1])

myTuple =(1,2,3,4,5,6)
print(myTuple[0:3])

#slicing cant be done --TypeError: 'set' object is not subscriptable
mySetTwo ={1,2,3,4,5,6}
#print(mySetTwo[0:3])

#set hasimmutable data type 

#mySetThree={"osama","Ahmad",188,31.23,True,[1,2,3,4]}#unhashable type: 'list'
mySetThree={"osama","Ahmad",188,31.23,True,(1,2,3,4)}
print(mySetThree)

#items is unique

mySetFour={1,2,7,"osama",}
print(mySetFour)


#clear()
a={1,2,3}
print(a)

#union()

b={"one","two","three"}
c={"1","2","3"}
x={"zero","cool"}

print (b | c)
print(b.union(c,x))


#add()

d={1,2,3,4,5}
d.add(7)
d.add(9)
print(d)
#copy

e={1,2,3,4,5}
f=e.copy()
print (e)
print(f)

e.add(6)
print(e)
print(f)

#remove()

g={1,2,3,4}
g.remove(1)
#g.remove(8)
print(g)

#discard()

h={1,2,3,4}
h.discard(1)
h.discard(8)
print(h)

#pop
i={"A","M",1,3,4,5,True}
print(i.pop())

#update()
j={1,2,3}
k={1,"A","B",2}
j.update(['html',"php"])
j.update(k)
print(j)
print("+"*50)

#difference()
a={1,2,3,4}
b={1,2,3,"Osma","Ahmad"}

print(a)
print(a.difference(b)) #a-b
print(a-b)
print(a)
print("/" * 40) #separator


#difference_update()

c={1,2,3,4}
d={1,2,"Osma","Ahmad"}

print(c)
(c.difference_update(d)) #c-d
print(c)
print("-" * 40)

#intersection
e={1,2,3,4,"X"}
f={"Rana","X",2}
print(e)
print(e.intersection(f))# e & f
print("=" * 40)

#intersection_update()

j={1,2,3,4,"X","Rana"}
k={"Rana","X",2}
print(j)
j.intersection_update(k)# j & k
print(j)
print("%" * 40)

#symmetric_difference()
i={1,2,3,4,5,"X"}
m={"Ahmas","Rana",1,2,4,"X"}
print(i)
print(i.symmetric_difference(m))#i^m
print(i)
print("=" * 40)


#symmetric_difference_update()
s={1,2,3,4,5,"X"}
w={"Ahmas","Rana",1,2,4,"X"}
print(s)
s.symmetric_difference_update(w)#i^m
print(s)
print("=" * 40)



#issuperset()

a={1,2,3,4}
b={1,2,3}
c={1,2,3,4,5}
print(a.issuperset(b))  #True
print(a.issuperset(c)) #false

print("=" * 40)

#issubset()
d={1,2,3,4}
f={1,2,3}
e={1,2,3,4,5}
print(d.issubset(f))#false
print(d.issubset(e))#true
print("=" * 40)

#isdisjont()
g={1,2,3,4}
k={1,2,3}
l={23,43,6}
print(g.isdisjoint(k))#false
print(g.isdisjoint(l))#true
