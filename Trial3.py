n=int(input("Enter the number of required fibo terms:"))
a=-1
b=1
c=0
for it in range(n):
   c=a+b
   print(c)
   a=b
   b=c
