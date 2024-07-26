'''PROBLEM SOLVING'''

'''Write a function to find maximum 0f three numbers'''

def max(a,b,c):
    if a>b and a>c:
        print("a is greatest.")
    elif b>a and b>c:
        print("b is greatest.")
    else:
        print("c is greatest.")

max(15, 60, 12)

'''create function and print a list where values are squares of numbers between 1 to 30'''

def list():
    l=[]
    for i in range (1,31):
        l.append (i**2)
    return l
print(list())


'''function to check given parameter is prime or not'''

def prime(n):
    if n==1:
        return ("not prime")
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print("not prime")
                break
        else:
            print(n, "is prime")

prime(7)


'''sum all the numbers in a list'''

def add(n):
    total=0
    for i in n:
        total+= i
        
    return total
    
print(add([5, 10, 10, 10]))


'''using recursion'''

def add(num):
    if len(num)==1:
        return num[0]
    else:
        return (num[0]+ add(num[1:]))

print(add([10, 20, 30, 40]))


'''fibonacci sequence using recursion'''

def fib(num):
    if num== 1:
        return 0
    elif num==2:
        return 1
    else:
        return (fib(num-1)+fib(num-2))
    
print(fib(7))


'''fibonacci sequence upto nth term'''

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

n = 10
print(fibonacci(n))
