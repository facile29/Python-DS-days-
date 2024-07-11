'''string slicing'''

a= "This is a sample string"

print(a[0:4])

print(a[4:12])

print(a[:4])    # positive indexing

print(a[-6:])   # negative indexing

b= "123456789"

print(b[::2])   # with gaps 
print(b[::3])  

print(b[:7:2])  # take by default 0 index if not given 

print(b[::-1])   # reverse string 
print(b[6::-1])

