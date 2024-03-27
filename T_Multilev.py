# Multilevel inheritance
balance=1000
class details:
    def __init__(self):
        self.name=str(input("Enter the account holder name: "))
        self.acno=int(input("Enter the account number: "))
        print("Your current balance: ",balance)
class mode(details):
    def __init__(self):
        super().__init__()
        print("-> Press '1' for Withdraw")
        print("-> Press '2' for Deposite")
        self.choice=int(input("Enter your choice: "))
class tran(mode):
    def __init__(self):
        super().__init__()
        if (self.choice==1):
            witham=int(input("Enter the amount to withdraw: "))
            print("Your current balance is: ",balance-witham)
        elif(self.choice==2):
            depoam=int(input("Enter the amount to Deposite: "))
            print("Your current balance is: ",balance+depoam)
        else:
            print("Enter the valid choice")
obj=tran()
