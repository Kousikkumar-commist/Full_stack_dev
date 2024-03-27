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