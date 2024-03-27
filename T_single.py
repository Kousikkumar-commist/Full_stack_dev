# single inheritance 
class detail:
    def __init__(self):
        self.name=str(input("Enter the account holder name: "))
        self.acno=int(input("Enter the account number: "))
        print("Your current balance: ",balance)
        print("-> Press '1' for Deposite")
        print("-> Press '2' for Withdraw")
        self.choice=int(input("Enter the choice: "))
class work(detail):
    def hello(self,balance):
        if(self.choice==1):
            depo=int(input("Enter the amount: "))
            depo+=balance
            print("Your current balance is: ",depo)
        elif(self.choice==2):
            withdr=int(input("Enter the amount: "))
            withdr=balance-withdr
            print("Your current balance is: ",withdr)
        else:
            print("Enter the valid pin")
balance=100000
h=work()
h.hello(balance)