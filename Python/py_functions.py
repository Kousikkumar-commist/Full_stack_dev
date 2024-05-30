
'''
x=5
a=('Hello')
print(id(a,x))'''

# Slice() function give only the number of values entered in slice(2) of an tuple
'''
a=('1','2','3','4','5','6','7','8','9','10')
x=slice(3) 
print(a[x])'''

# F-String
'''
name="kousik"
print(f"Hello,{name}!")
print("Hello,",name,"!")
print("Hello,"+ name +"!")
message = f"{{This is a literal brace}}"
print(message)'''

# dir() funtion
'''
class person:
    name="kopi"
    age=20
print(dir(person))'''

# type(), enumerate(), zip() 
''''''
a=('apple','banana','orange')
k=('apple','banana','orange')
b="Hello world!"
c=33
x=type(a)
h=enumerate(a)
y=type(b)
z=type(c)
print(h,x,y,z)
print(zip(a))