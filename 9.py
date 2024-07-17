'''PROBLEM SOLVING'''

'''sort values'''

a={1:"orange", 2: "blue", 3:"green", 4:"pink", 5:"white"}
a= sorted(a.values())
print(a)

'''print dict where keys are 1 to 15 and values are there square'''

b={}
for i in range(1,16):
    b[i]= i**2
print(b)
    
'''multiply all items in dict'''

c={1:1, 2:4, 3:12, 4:5}
d=1
for i in c:
    d*=c[i]
print(d)

'''sort dictionary by key'''

e={5:"orange", 2: "blue", 4:"green", 1:"pink", 3:"white"}
e= sorted(e.keys())
print(e)


'''SETS'''

x= {"monika", "amit", "jahanvi", "priya", "jiya"}

for i in x:
    print(i)
    
'''sets functions'''

x.add("dolly")
print(x)

x.pop()
print(x)

x.remove("priya")
print(x)

x.discard("jiya")

y=x.copy()
print(y)

