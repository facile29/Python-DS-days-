# '''numpy library'''

import numpy as np 
a= np.array([10, 20, 30, 40, 50])
print(a)
print(type(a))

'''slicing'''

print(a[0:3])
print(a[3:])

b= np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print(b)
print(b[0:2, 0:2])
print(b [0, 1:3])           
print(b[1, 2:4])

'''Functions'''

print(len(b))                                       # number of nested values

print("shape of array:", np.shape(b))               # rows, columns

print("size of array:", np.size(b))                 # number of elements

print("number of dimensions:", np.ndim(b))          # total values in array

print(b.dtype)                                      # type of array

print(b.astype(float))                              # conversion of datatype


'''mathematical operations''' 

print("for addition: ")

arr1= np.array([[10, 20], [30, 40]])
arr2= np.array([[10, 20], [30, 40]])
print(arr1+arr2)
print(np.add(arr1, arr2))

print("for subtract: ")

arr1= np.array([[40, 30], [10, 20]])
arr2= np.array([[40, 30], [10, 20]])
print(arr1-arr2)
print(np.subtract(arr1, arr2))

print("for multiplication:")

arr1= np.array([[10, 20], [30, 40]])
arr2= np.array([[10, 20], [30, 40]])
print(arr1*arr2)
print(np.multiply(arr1, arr2))

print("for dividing: ")

arr1= np.array([[10, 20], [30, 40]])
arr2= np.array([[10, 20], [30, 40]])
print(arr1/arr2)
print(np.divide(arr1, arr2))


x= np.array([10, 20])
y= np.array([2])

print(np.power(x,y))

a1= np.array([16, 9, 81, 100])
print(np.sqrt(a1))

'''combining and splitting array'''

#concatenation of arrays

n1= np.array([10, 20])                 
n2= np.array([30, 40])
print(np.hstack([n1, n2]))
print(np.vstack([n1, n2]))
print(np.concatenate([n1, n2]))

# splitting array
n3=np.array([[10, 20], [30, 40]])
n4= np.array_split(n3, 2)
print(n4)

n5=np.array_split(n3, 3)
print(n5)