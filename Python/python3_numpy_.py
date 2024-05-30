'''
import numpy as np
dt=np.dtype([('age',np.int8)])
val=np.array([(10),(20),(30)],dtype=dt)
print(val)
print(type(val))
print (val['age'])

detail=np.dtype([('name','S20'),('age','i2')])
print(detail['name'])
'''
import numpy as np

a=np.arange(10)
x=np.zeros(2)
y=np.empty(2)
z=np.ones(2)
f=np.array(2)
h=np.dtype('i2')
g=np.asarray(2)

#print(a.reshape(2,4,3))  '2' matrix in 4×3 
print(a.slice(2,7,2)) # here in slice starting value 2 ending value 6(7) and set value 2 so 2 4 6 is output
print(x,y)