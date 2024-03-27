a=[1,2,3,4,5]
b=1
c=1
for i in a:
    i=c
    c=i*a[b]
    b+=1
    if (len(a)==5):
        print(c) 
