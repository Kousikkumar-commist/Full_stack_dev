import mysql.connector

x=mysql.connector.connect(host='localhost',user='root',password='',database='nst')
s=x.cursor()
#s.execute("CREATE DATABASE nst")

#s.execute("CREATE TABLE bio(Name VARCHAR(255),Age INT)")
'''t="INSERT INTO bio (Name,Age) VALUES(%s,%s)"
u=[('anu',12),('Arun',43),('Durai',34)]
s.executemany(t,u)'''
#s.execute("DELETE FROM bio WHERE Age=12")
#s.execute("UPDATE bio SET Name='AJAY'WHERE Age=43")
s.execute("SELECT * FROM bio")
t=s.fetchall()
for i in t:
    print(i)
x.commit()