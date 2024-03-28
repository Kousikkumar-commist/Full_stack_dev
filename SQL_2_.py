#insert
#delete
#update
#select
import mysql.connector
a=mysql.connector.connect(host="localhost",user="root",password="",database="first_project")
b=a.cursor()
print("Press '1' to insert")
print("Press '2' to delete")
print("Press '3' to update")
print("Press '4' to select data from table")
#ame=input("Enter your name: ")
#age=int(input("Enter your age: "))
choice=int(input("Enter the choice: "))
if choice==1:
    t="INSERT INTO data (name,age) VALUES (%s,%s)"
    u=[('kousik',16)]
    b.executemany(t,u)
    a.commit()
elif choice==2:
    t="DELETE FROM data WHERE  name=%s"
    n=input("Enter the name of person you want to delete: ")
    b.execute(t,n)
    a.commit()