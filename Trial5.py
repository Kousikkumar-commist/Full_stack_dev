print("Press 1 To find Average")
print("Press 2 To find Fibonacci series")
print("Press 3 To find Tables")
choice=int(input("Enter your choice: "))
if(choice==1):
    a=int(input("Enter your mark1: "))
    b=int(input("Enter your mark2: "))
    c=int(input("Enter your mark3: "))
    d=int(input("Enter your mark4: "))
    e=int(input("Enter your mark5: "))
    total=a+b+c+d+e
    if(a>35) and (b>35) and (c>35) and (d>35) and (e>35) :
        print("Your Average is: ",total/5)
    else:
        print("Sorry your are failed")
elif(choice==2):
    n=int(input("Enter the number of required fibo terms:"))
    a=-1
    b=1
    c=0
    for it in range(n):
        c=a+b
        print(c)
        a=b
        b=c
elif(choice==3):
    a=int(input("Enter the number to find table: "))
    for it in range(10):
        c=a*it
        if(c!=0):
            print(a,"×",it,"=",c)
else:
    print("Enter a correct choice")