'''Lists - an ordered collection of elements and mutable '''

'''list slicing'''

a=["monika", "amit", "jahanvi", "jiya", "gautam"]

print(a[2])
print(a[-4])
print(a[1:3])
print(a[:3])
print(a[::2])
print(a[-1:-4:-1])

'''list iteration'''

b =["apple", "mango", "grapes", "watermelon", "kiwi", "banana"]  

for i in b:           #using for loop 
    print(i)
    
    
for i in range (len(b)):           # using for loop with length function
    print(b[i])
    

i=0                              # using while loop 
while i<(len(b)):
    print(b[i])
    i+=1


[print (i) for i in b]              # short hand loop 


'''LIST FUNCTIONS'''

c=["black", "blue", "orange", "green", "violet"]

print(len(c))

print(c.count("blue"))

c.append("pink")
print(c)

c.insert(2,"purple")
print(c)

c.remove("violet")
print(c)

c.pop(3)
print(c)

d= c.copy()
print(d)

print(c.index("blue"))

x= ["white", "red"]
c.extend(x)
print(c)

c.reverse()
print(c)

c.sort()
print(c)

c.clear()
print(c)

'''List comprehension'''

l1=[10,20,30,40]
l2=[]
for i in l1:
    l2.append(i)
print(l2)

l3=[i for i in l1]
print(l3)


''' PROBLEM SOLVING '''

'''swap first and fourth element'''

d=["jay", "hay", "joey", "rose"]
d[0], d[3]= d[3], d[0]
print(d)

'''insert element in second position'''

d.insert(1, "lily")
print(d)

'''delete 3rd element'''

d.pop(2)
print(d)

'''multiply all no.s in list'''

e=[12, 20, 3, 40, 5, 9]
mul=1
for i in e:
    mul*=i
print(mul)    

'''largest no. and smallest number from list'''

e.sort()
print(e)
print("the largest no. in list is: ", e[-1])
print("the smallest no. in list is: ", e[0])



