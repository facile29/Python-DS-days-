'''   BASIC PROBLEMS  '''

'''fibonacci series''' 

a= 0
b=1
num= int(input("fibonacci series upto: "))
if num==1:
    print(1)
else: 
    for i in range(2, num):
        c=a+b
        a=b
        b=c
        print(c)


'''find if the number is prime or not''' 

n= int(input("enter the number to check if it's prime:"))
if n>1:
    print(n, "is not prime number")
else: 
    for i in range(2, n):
        if n % i==0:
            print(n, "is not prime number")
            
        else:
            print(n, "is prime ")
    

'''check for palindrome number '''

x= int(input ("enter number to check palindrome:"))
temp=x
rev=0
while(x>0):
    digit= x%10
    rev= rev* 10+digit
    x= x//10
if rev== temp:
    print(temp, "is palindrome")
else: 
    print("not palindrome ")    


''' area calculator '''

print("AREA CALCULATOR")
print("-"*40)

while True: 
    choice = int(input("enter number between 1 to 4:\n1. Square\n2. Rectangle\n3. Circle\n4. Triangle\n"))

    if choice == 1:
        while True:
            side = int(input("enter side of square: "))
            square = side ** 2
            print("area of the square:", square)
            repeat=input("want to try square again (y/n)? ")
            if repeat=='n' or repeat=='no':
                break
            
    elif choice == 2:
        while True:
            length = int(input("enter length of rectangle: "))
            width = int(input("enter width of rectangle: "))
            rectangle = length * width
            print("area of rectangle:", rectangle)
            repeat=input("want to try rectangle again (y/n)? ")
            if repeat=='n' or repeat=='no':
                break

    elif choice == 3:
        while True: 
            radius = int(input("enter radius of circle: "))
            circle = 3.14 * (radius ** 2)
            print("area of circle:", circle)
            repeat=input("want to try circle again (y/n)? ")
            if repeat=='n' or repeat=='no':
                break

    elif choice == 4:
        while True:
            base = int(input("enter base of triangle: "))
            height = int(input("enter height of triangle: "))
            triangle = 0.5 * base * height
            print("area of  triangle:", triangle)
            repeat=input("want to try triangle again (y/n)? ")
            if repeat=='n' or repeat=='no':
                break
    else: 
        print("invalid input")
    repeat1= input("want to repeat menu(y/n)?")
    if repeat1=='n' or repeat1=='no':
        break

