a=int(input("Enter the value of 'A': "))
b=int(input("Enter the value of 'B': "))
def add():
    print(a+b,"👌")
def sub():
    print(a-b,"👌")
def mul():
    print(a*b,"👌")
def div():
    print(a/b,"👌")
choice=(input("Enter your choice: "))
if (choice=='+'):
    add()
elif (choice=='-'):
    sub()
elif (choice=='*'):
    mul()
elif (choice=='/'):
    div()