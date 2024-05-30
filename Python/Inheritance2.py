import Inheritance1 
import platform
import datetime
x=datetime.datetime.now()
v=datetime.datetime(2007,10,31,3,10,59,60)
print(dir(Inheritance1))
print(dir(platform))
print(v,x)
print(x.year)
print(x.strftime("%a"))
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%C"))
print(x.strftime("%D"))