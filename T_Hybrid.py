class details:
    def __init__(self) -> None:
        self.name=str(input("Enter the account holder name: "))
        self.acno=int(input("Enter the Account number: "))
        self.balance=int(input("Enter your current balance: "))
        print("-> Press '1' for Deposite")
        print("-> Press '2' for Withdraw")
        self.choice=int(input("Enter your choice: "))
        if self.choice==1:
            self.depo_amount=int(input("Enter the amount to deposite: "))
        elif self.choice==2:
            self.with_amount=int(input("Enter the amount to withdraw: "))
class transaction(details):
    def __init__(self) -> None:
        super().__init__()
        if self.choice==1:
            self.balance+=self.depo_amount
        elif self.choice==2:
            self.balance-=self.with_amount
class deposite(details):
    def __init__(self) -> None:
        super().__init__()
        if self.with_amount or self.depo_amount >= 1000:
            print("\nYou won the cashback of rupees 10\n")
            self.balance+=10
class show_details(transaction,deposite):
    def __init__(self) -> None:
        super().__init__()
        print("Transaction made successfully")
        print("Your current balance is: ",self.balance)
obj=show_details()