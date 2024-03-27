num=int(input("Enter the Number"))
sum=0
temp1=num
while(num>0):
    f=1
    last=num%10
    for i in (last,-1):
        f=f*i
        i-=1
    sum+=f
    num=num/10
if(sum==temp1):
    print("Yes it is a strong number")
else:
    print("No it is not a strong number")
i=1
for i in range(i,5):
    for j in range(i,5):
        print("*",end=" ")
    print()