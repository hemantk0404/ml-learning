import random
#list comp
a=[random.random() for n in range(20)]
print(a)
b=[x*x for x in range(20)]
print(b)
c=[n for n in range(50) if n<10]
print(c)
d=['!' if al in 'aeiou' else al for al in "technical"]
print(d)

#generate set
a={x**2 for x in range(10)}
print(a)


#generate dict
d1={1:"A",2:"B",3:"c"}
d2={k:v for (k,v) in d1.items()}
print(d2)