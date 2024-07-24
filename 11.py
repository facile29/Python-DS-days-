'''Functions'''

def Hello():
    print("hello world!")
    
Hello()

def add():
    x=20
    y=10
    print(x+y)
    
add()

def rectangle(length, width):
    print("area of rectangle:", length*width)
    
rectangle(12,7)

def Hello(*name):                   # Arbitrary  argument
    print("my name is", name[2])
    
Hello("monika", "jiya", "gautam")


def mul(a,b):           #return statement 
    return(a*b)
print(mul(50, 7))


'''factorial of a number '''

def fact(n):
    if n==1:
        return 1
    else:
        return(n*fact(n-1))

number=int(input("enter the number for factorial: "))
print(fact(number))


'''compute nth fibonacci number '''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

number = 8
print(f"The",number,"th Fibonacci number is", fibonacci(number))


'''list of fibonacci numbers'''

def fib(n):
    fib_seq=[0, 1]
    
    for i in range(2, n + 1):
        fib_seq.append(fib_seq[i-1]+fib_seq[i-2])
    return fib_seq

num=int(input("enter the number:"))
print("fibonacci sequence upto", num,"th number", fib(num))


'''Lambda function'''

a= lambda b:b+10                  # single argument
print(a(4))

x= lambda a, b:a*b                # multiple args 
print(x(3,4))

num= [1,2,3,4,5]                      # with map 
square= list(map(lambda x:x**2, num))
print(square)


n=[2, 23, 40, 50, 67, 74, 31]           # with filter
even= list(filter(lambda x:x%2==0, n))
print(even)

tuple=[(1, "one"), (2,"two"), (3, "three")]         #with sorted 
sort= sorted(tuple, key=lambda x:x[1])
print(sort)

'''Local variables'''

num= 24
def hello():
    x=25 
    return x    
print(hello())

print(num)

'''Global variables'''

num= 24
def hello():
    global x
    x=25 
    return x    
print(hello())
print(x)
