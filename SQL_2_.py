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
elif choice==2:
    b.execute("DELETE FROM data WHERE age=16")
elif choice==3:
    b.execute("UPDATE data SET  age=80 WHERE age=16")
elif choice==4:
    b.execute("SELECT * FROM data")
    t=b.fetchall()
    for i in t:
        print(i)
a.commit()