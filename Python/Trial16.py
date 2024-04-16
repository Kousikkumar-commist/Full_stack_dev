def fuel():
    if(choice==1):
        print("Petrol per Liter is 100 Rs")
        print("---------------------------")
        print("Total amount: ",no*100,"Rs")
        print("---------------------------")
    elif(choice==2):
        print("Diesel per Liter is 98 Rs")
        print("---------------------------")
        print("Total amount: ",no*98,"Rs")
        print("---------------------------")
    elif(choice==3):
        print("Electricity per hour is 70 Rs")
        print("---------------------------")
        print("Total amount: ",no*70,"Rs")
        print("---------------------------")
print("Press '1' For Petrol:")
print("Press '2' For Diesel:")
print("Press '3' For Electricity:") 
choice=int(input("Enter your choice: "))
no=int(input("Enter the number of liters/hour:"))
fuel()