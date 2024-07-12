''' TUPLES '''

a= "mango", "cheery", "kiwi", "apple"
print(type(a))

'''slicing in tuple'''

print(a[1:3])
print(a[:3])
print(a[2:])
print(a[::2])
print(a[1: : 2])
print(a[::-1])
print(a[2::-1])

'''iteration with for loop'''

for i in a:
    print(i)
    
'''iteration with length and range'''

for i in range(len(a)):
    print(a[i])

'''iteration using while loop'''

i=0
while i<len(a):
    print(a[i])
    i+=1

'''Conversion of tuples '''

b=list(a)
print(type(b))
b.append("kiwi")
a=tuple(b)
print(a)

''' Functions '''

print(a.count("kiwi"))
print(a.index("cheery"))

'''DICTIONARY'''

data={"name": "monika", "age": 19, "gender": "female"}
print(type(data))

print(data["age"])

'''Iteration''' 

for x in data:                      #print keys
    print(x)
    
for x in data :                     #print values
    print(data[x])
    
for x in data.values():             #using value function 
    print(x)

for x,y in data.items():            #using items functions
    print(x,"-", y)

'''Functions '''

print(data.get("name"))
print(data.items())
print(data.keys())
print(data.values())

c= data.copy()
print(c)

data.update({'city':'Noida'})
print(data)

data.pop('city')
print(data)

data.popitem()
print(data)

data.clear()
print(data)

'''nested dictionaries '''

employees={1: {"name":"monika", "age": 19,"gender": "female"}, 
2: {"name":"amit", "age": 22,"gender": "male"}, 
3:{"name":"jahanvi", "age": 21,"gender": "female"}} 

print(employees[2])
print(employees[2]["age"])
print(employees[1]["name"])