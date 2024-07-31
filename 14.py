
'''add, remove elements in array'''

import numpy as np
a=np.array([10, 20 ])
print(np.append(a, [40, 50]))

b=(np.insert(a, 1, [60, 80]))                # array, index, value 
print(b) 

print(np.delete(b, [1]))

'''sort, filter, search array'''

# sort array
s=np.array([5, 17, 4, 9, 18, 12])
sa= np.sort(s)
print(sa)

# search array
x= np.where(s==9)
print(x)

y= np.searchsorted(sa, 18)                  #array must be sorted 
print(y)

# filter array
f= np.array([10, 20, 30, 40])
fa=[True, False, True, False]
new= f[fa]
print(new)

h= np.array([3, 10, 18, 27])
ha=h%2==0
n= h[ha]
print(n)

'''aggregate functions'''

arr= np.array([50, 100, 150, 200])

print(np.sum(arr))
print(np.min(arr))
print(np.max(arr))
print(np.size(arr))
print(np.mean(arr))
print(np.cumsum(arr))
print(np.cumprod(arr))

'''example'''

a= [100, 50, 150, 30, 40]
b= [2, 3, 4, 5, 9 ]
price= np.array(a)
quantity= np.array(b)

c= np.cumprod([price, quantity], axis=0)
print(c)

print("total bill:", c[1].sum())

'''statistical functions'''

import statistics as st

food= np.array([100, 200, 150, 300, 200])

# mean, median, mode, standard deviation, variance , correlation coefficient

print(np.mean(food))
print(np.median(food))

print(st.mode(food))
print(np.std(food))
print(np.var(food))

ar=np.array([400, 200, 500, 800, 1000])
br= np.array([10, 20, 30, 40, 50])

print(np.corrcoef([ar, br]))


