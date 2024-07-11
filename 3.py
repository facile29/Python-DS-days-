''' STRING FUNCTIONS'''

'''string functions 1'''

a= "This is a sample string for practicing string functions in python"

print(len(a))

print(a.count("is"))

print(a.upper())

print(a.lower())

print(a.index("sample"))

print (a.capitalize())

print(a.casefold())

print(a.find("string"))

print(a.find("p",20,40))

b= "This string says :{}"
print(b.format(a))


name="monika"
print(name.center(20))
print(name.center(20, '*'))


'''string functions 2'''

a = "abc123"
b = "abc"
c= "123"
d = "456"
e = "789"
f = "lowercase"
g = "UPPERCASE"
h = "     "
i = "Title Case String"

# format function

print(f"Is '{a}' alphanumeric? {a.isalnum()}")

print(b.isalpha())    
#  true if in string all characters are alphabet 

print(c.isdecimal())

print(d.isdigit())

print(e.isnumeric())

print(f.islower())

print(g.isupper())

print(h.isspace())

print(h.istitle())


'''string functions 3'''

ab = "Hello, welcome to the world of Python."

print(ab.endswith("Python."))

print(ab.startswith("Hello"))

print(ab.swapcase())

x= "      Hello, python!    "
print(x.strip())

print(ab .split())


y= "My name is "
z= y.ljust(20, ".")
print(z, "monika")

print(y. replace("My", "Her"))

print(ab.rindex("of"))

print(ab.rfind("to"))