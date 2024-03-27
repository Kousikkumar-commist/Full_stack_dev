def add():
    print("👉 Correct ans:",a+b,"👈")
    if(predic==a+b):
        print("👏Well done👏")
    else:
        print("👍Better luck next time👍")
def sub():
    print("👉 Correct ans:",a-b,"👈")
    if(predic==a-b):
        print("👏Well done👏")
    else:
        print("👍Better luck next time👍")
def mul():
    print("👉 Correct ans:",a*b,"👈")
    if(predic==a*b):
        print("👏Well done👏")
    else:
        print("👍Better luck next time👍")
def div():
    print("👉 Correct ans:",a/b,"👈")
    if(predic==a/b):
        print("👏Well done👏")
    else:
        print("👍Better luck next time👍")
print(" ")
print("\t\t-----------------------------")
print("\t\t|    🙏    WELCOME    🙏    |")
print("\t\t|    1    2   3   DEL AC    |")
print("\t\t|    4    5   6    +   -    |")
print("\t\t|    7    8   9    *   /    |")
print("\t\t|         0         ANS     |")
print("\t\t-----------------------------")
print(" ")
print("Press '1' For Addition:")
print("Press '2' For Subtraction:")
print("Press '3' For Mutiplication:")
print("Press '4' For Division:")
choice=int(input("Enter your choice: "))
a=int(input("Enter the value of 'A': "))
b=int(input("Enter the value of 'B': "))
predic=int(input("Enter you prediction: "))
if (choice==1):
    add()
elif (choice==2):
    sub()
elif (choice==3):
    mul()
elif (choice==4):
    div()