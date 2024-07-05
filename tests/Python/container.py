#lists iterable mutable like arrays
l0 =[1,2,3,4,5]
l1=[[1,2,3,4],[5,6,7,8]]
print(l1)
print(l0[0:2])
for i in l0:
    print(i)
i=0
while i<len(l0):
    print(i)
    i=i+1
l3=l0+l1
print(l3)
l4=list("Africa") #create list
print(l4)
l4=l3  #shallow copy
l5=l3+[] #deep copy 
l5=[*l3]
#search 
if 1 in l0:
    print("Found in list")

#Tuples immutable collection iterable
#usually store different data 
t1=("A",1,2)
print(t1[0])
#t1+t2 works 

#Sets unique values and non iterable stored with hash values 
s1=set()
s2={"S",1,2,3}
print(s2) #printed in hash code 
#loops allowed
for i in s2:
    print (i)
#add no concat 
if 1 in s2:
    print("Found in tuple")

#Dict mutable nonitratable 
d1={1:"A",2:"B",3:"c"}
print(d1)
print(d1[1])
if 1 in d1.keys():
    print("Found key in dict")