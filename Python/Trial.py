print("Press 1 To find Biggest number between any two number")
print("Press 2 To find Biggest number between any three number")
print("Press 3 To find odd or even number")
print("Press 4 To find positive or negative number")
choice=int(input("Enter your choice: "))
if(choice==1):
    a=int(input("Enter the value of A: "))
    b=int(input("Enter the value of B: "))
    if(a>b):
        print("A is the greatest number")
    else:
        print("B is the greatest number")
elif(choice==2):
    a=int(input("Enter the value of A: "))
    b=int(input("Enter the value of B: "))
    c=int(input("Enter the value of C: "))
    if(a>b) and (a>c):
        print("A is the greatest number")
    elif(b>a) and (b>c):
        print("B is the greatest number")
    elif(c>a) and (c>b):
        print("C is the greatest number")
elif(choice==3):
    val=int(input("Enter the value to find odd or even: "))
    if(val%2==0):
        print("The given number is even number")
    else:
        print("The given number is odd number")
elif(choice==4):
    a=int(input("Enter the value of A: "))
    if(a>=0):
        print("The given number is positive")
    else:
        print("The given number is negative")
else:
    print("Enter a correct choice")