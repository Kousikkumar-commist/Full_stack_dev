# Multiple inheritance
class Account:
    def __init__(self):
        self.name = input("Enter the account holder name: ")
class Transaction:
    def hello(self):
        self.acno = int(input("Enter the account number: "))
class Withdraw(Account,Transaction):
    def __init__(self):
        super().__init__()
        self.hello()
        balance = 1000
        print("What would you like to do?")
        print("1. Deposit")
        print("2. Withdraw")
        self.choice = int(input("Enter your choice: ")) 
        if self.choice == 2:
            self.withdraw_amount = int(input("Enter the amount to withdraw: "))
            balance-=self.withdraw_amount
            print("Transaction made successfully")
            print("Your current balance is:", balance)
        elif self.choice == 1:
            self.deposit_amount = int(input("Enter the amount to deposit: "))
            balance+=self.deposit_amount
            print("Transaction made successfully")
            print("Your current balance is:", balance)
        else:
            print("Invalid choice. Please enter 1 or 2.")  
w=Withdraw()