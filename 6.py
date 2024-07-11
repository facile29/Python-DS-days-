'''' PROBLEMS '''

'''reverse string'''

a= input("enter a string:")
rev= a[::-1]
print(rev)

'''check if string contains only digits'''

a= "123456"
b= a.isdigit()
print(b)

'''if string is palindrome '''

temp= input("enter a string:")
a= temp[::-1]
if temp==a:
    print("string is palindrome. ")
else:
    print("not palindrome. ")

'''find no. of vowels in a string'''

a= "hello"
vowels=0
for i in a:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowels+=1 
        
print("number of vowels in string are:", vowels)

'''if string begins with capital letter '''

name=input("enter the name:")
t= name.istitle()
print(t)

'''sort strings alphabetically '''

m="sample string"
print(sorted(m))

'''number of occurrence of substring'''
x="some says the world will end in fire, some says in ice."
print(x.count("some"))
print(x.count("says"))
print(x.count("world"))

