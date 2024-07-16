'''sets functions 2'''

# a={1, 2, 3, 4, 5, 6}
# b={10, 11, 12, 13}
# c={5, 6}

# print(a.isdisjoint(b))
# print(a.isdisjoint(c))

# print(a.issubset(c))
# print(c.issubset(a))

# print(a.issuperset(b))
# print(a.issuperset(c))

# a.update(b)
# print(a)

# a.update(c)
# print(a)

# a.clear()
# print(a)

'''set functions 3'''

# x={10, 20, 30, 40}
# y={30, 40, 50, 60}

# print(x.union(y))
# print(x.difference(y))

# x.difference_update(y)
# print(x)

# print(x.intersection(y))

# print(x.symmetric_difference(y))

'''PROBLEM SOLVING'''

'''find min and max from set '''
# s1={1000, 300, 500, 2000, 650, 50}

# maximum= max(s1)
# minimum= min(s1)

# print(maximum, "is the maximum element in set")
# print(minimum, "is the minimum element in set ")

'''common elements in 3 list using sets'''

# a=[1,2,3,4,5,6]
# b=[5, 7, 8, 6, 9]
# c=[10, 20, 6, 30, 5]

# x=set(a)& set(b)& set(c)

# print("the common element from in 3 list is", x)

'''remove item from set'''

# set= {1000, 300, 500, 2000, 650, 50}
# set.discard(50)
# print(set)
