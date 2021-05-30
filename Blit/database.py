#!/usr/bin/python3
import pymysql
from tkinter import *
from tkinter import messagebox



win = Tk()
win.geometry("500x400")
win.configure(bg = '#d45500')


def helloCallBack():
 msg=messagebox.showinfo( "Hello Python", "Hello World")



L1 = Label(win, text="Username")
L1.place(x=150, y=100)
L1.configure(bg='#d45500')

E1 = Entry(win, bd=1)
E1.place(x=230, y=100)

L2 = Label(win, text="Password")
L2.place(x=150, y=160)
L2.configure(bg='#d45500')

E2 = Entry(win, bd=1)
E2.place(x=230, y=160)



B = Button(win, text ="Login", command = helloCallBack, bd =1)
B.place(x=230,y=200)
win.mainloop()


firstname = input("First name: ")
lastname = input("Last name: ")


# Open database connection
db = pymysql.connect("localhost","root","","TESTDB" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query to DELETE required records
sql = "SELECT * FROM EMPLOYEE2 WHERE FIRST_NAME =  '%s'" % (firstname)

try:
     # Execute the SQL command
     cursor.execute(sql)

     # Fetch all the rows in a list of lists.
     results = cursor.fetchall()
     for row in results:
         lname = row[1]

         if lastname == lname:
             print("Logged in successfully")
         else:
             print("Error!")
except:
     # Rollback in case there is any error
     db.rollback()
     print("sql error!")

# disconnect from server
db.close()
