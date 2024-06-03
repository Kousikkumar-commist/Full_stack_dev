# THIS CODE IS DONE BY ME

def recursion(n,m,f):  
    if f!=m: 
        m=m-f 
        n=n+m 
        c=f+1 
        m=m+f
        recursion(n,m,c) 
    else:
        print("The sum of the",m,"natural number is: ",n)
    
val=int(input("Enter the value: ")) 
t=val
recursion(val,t,1) 

# THIS CODE IS DONE BY CHATGPT

def recursion(n, current=1, total=0):
    if current > n:
        print("The sum of the first", n, "natural numbers is:", total)
    else:
        recursion(n, current + 1, total + current)

val = int(input("Enter the value: "))
recursion(val)