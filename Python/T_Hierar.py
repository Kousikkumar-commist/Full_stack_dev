# Hiererchical inheritance
balance=1000
class details:
    def __init__(self):
        self.name=str(input("Enter the account holder name: "))
        self.acno=int(input("Enter the account number: "))
        print("Your current balance: ",balance)
        print(" ")
class withdr(details):
    def __init__(self):
        super().__init__()
        self.witham=int(input("Enter the amount to withdraw: "))
        print("Your current balance is: ",balance-self.witham)

class deposi(details):
    def __init__(self):
        super().__init__()
        self.depoam=int(input("Enter the amount to withdraw: "))
        print("Your current balance is: ",balance+self.depoam)

print("-> Press '1' for Deposite")
print("-> Press '2' for Withdraw")
choice=int(input("Enter your choice: "))
if (choice==1):
    h=withdr()
elif(choice==2):
    w=deposi()
else:
    print("Enter the valid choice")