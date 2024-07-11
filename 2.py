
'''loops and conditional statements '''
a= 44
if a%2==0:
    print("a is even")
else:
    print("a is odd")


'''area of shapes'''
choice= int(input("enter number between 1 to 4:"))

if choice ==1:
    side= int(input("enter the side of square:"))
    square= side**2
    print("area of square:", square)            #same   
elif choice ==3:
    radius= int(input("enter the radius of circle:"))
    circle = 3.14*(radius**2)
    print("area of circle:" , circle)
    
else:
    print("invalid input")


'''find vowel '''

alpha= input("enter a letter :")
if alpha in "aeiou":
    print(alpha , "is a vowel")
else:
    print("consonant")
    

'''table ''' 
n= 21
for i in range(1, 11):
    print(n , "x", i, "=", n*i)
    
    
n= int(input("enter number:"))
for i in range(1, 11):
    print(n , "x", i, "=", n*i)


'''while loop '''                                   
n= 0
while n<= 5:
    print(n)
    n+=1


''' for loop to print no.s'''
for i in range(1, 2):
    for j in range(1, 9):
        print(j, end=" ")
    print()


''' increasing tri'''
for i in range (1, 6):
    for j in range(1, i+1):
        print("*", end= "")
    print()


''' decreasing tri '''
for i in range (5, 0, -1):
    for j in range(1, i+1):
        print("*", end= "")
    print()


''' another increasing tri'''
n= 5
for i in range (n):
    for j in range(0, i+1):
        print("*", end= "")
    print()


''' right: increasing space, decreasing star'''
n= int (input("enter no. of rows:"))
for i in range (n):
    for k in range (i, n-1):
        print(' ', end=" ")
    for j in range (i+1):
        print("*", end= " ")
    print()


''' right: increasing space , decreasing star'''
n= 5
for i in range (n):
    for j in range (i+1):
        print(' ', end=" ")
    for j in range (i,n):
        print("*", end=" ")
    print()


''' left tri '''
n = 5
for i in range(n):
    for j in range(n - i):
        print(i, end="")
    print()


''' for loop with conditional statements '''
for i in range (1, 11):
    if i==3:
        print("add to fav")
    else: 
        print(i)


'''for loop with condition of common multiple 9-'''
n =int(input("enter number:"))
for i in range (1, n+1):
    if i% 8==0 and i%12==0:
        print(i)
        
        
''' while loop with condition''' 
n= 1
while n<= 10:
    if n==3:
        print("add to fav")
    else:
        print(n)
        
    n+=1


''' sum of even no.s'''
sum = 0
for i in range(1, 101):
    if i%2 == 0 :
        sum+=i
print(sum)


''' square of no.s '''
for i in range(1, 21):
    if i %2== 0:
        print(i, i**2)
    
    
''' sum of odd no.'''
sum =0
n=0
while n<=20:
    if n%2 != 0:
        sum+=n
    n+=1
print (sum)


'''billing system at super mart '''
while True:
    name= input("enter customer name:")
    total =0
    
    print("-"*40)
    
    while True:
        quantity= int(input("enter the no. of quantity of items: "))
        amount= int(input("enter the amount of items: "))
        total += amount*quantity
        
        repeat= input("want to add more items(y/n)? ")
        if repeat== 'n' or repeat=='no':
            break
    

    print("****************Happy Shopping************")
    print("Name of customer:", name)
    print("total amount bill: ", total)
    repeat1= input("want to go to next customer(y/n)? ")
    if repeat1=='n' or repeat1=='no':
            break

