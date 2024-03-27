import Trial18
print("-> Press '1' for Deposite")
print("-> Press '2' for Withdraw")
choice=int(input(" "))
if(choice==1):
    depo=int(input("Enter the amount: "))
elif(choice==2):
    withdr=int(input("Enter the amount: "))
else:
    print("Enter the valid pin")
obj1=Trial18.transaction()