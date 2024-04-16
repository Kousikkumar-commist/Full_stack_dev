a=[1,2,3,4,5]
c=b=1
for i in a:
    i=c #i=24 c=24
    if b!=5:
        c=i*a[b] #120=24*5 / c=120
        b+=1 # b=5
if (b==5): #5=5
    print("The product all values in list 'a' is: ",c)