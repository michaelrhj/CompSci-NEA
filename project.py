#importing libraries that are used
import sys
from tkinter import *
import sqlite3

#main menu screen
def home():
	#window setup
	window = Tk()
	window.title("Home")
	window.minsize(800,500)
	window.configure(bg="#0394fc")

	#top of the screen labels

	loginLabel = Label(window,bg="#0394fc",text="Login",font=("",30)).place(x=20,y=20)
	registerLabel = Label(window,bg="#0394fc",text="Register",font=("",30)).place(x=500,y=20)

	#login labels and entries
	loginUsernameLabel = Label(window,bg="#0394fc",text="Username: ").place(x=10, y=120)
	loginUsernameEntry = Entry(window).place(x=80, y=120)
	loginPasswordLabel = Label(window,bg="#0394fc",text="Password: ").place(x=10, y=160)
	loginPasswordEntry = Entry(window).place(x=80, y=160)

	#login button
	loginButton = Button(window,text="Login",width="8").place(x=10, y=200)

	#register labels and entries
	global registerUsernameEntry
	global registerPasswordEntry
	registerUsernameLabel = Label(window,bg="#0394fc",text="Username: ").place(x=500, y=120)
	registerUsernameEntry = Entry(window).place(x=570, y=120)
	registerPasswordLabel = Label(window,bg="#0394fc",text="Password: ").place(x=500, y=160)
	registerPasswordEntry = Entry(window).place(x=570, y=160)	

	#register button
	registerButton = Button(window,text="Register",width="8",command=registerUser).place(x=500, y=200)

	window.mainloop()

def registerUser():
	username = registerUsernameEntry.get()
	password = registerPasswordEntry.get()
	print(username,password)

def addUser():
	username = "master"
	password = "master"

	conn = sqlite3.connect('ProjectileMotionGame.db')
	c = conn.cursor()	
	c.execute("INSERT INTO users VALUES (?,?)",(username,password))
	conn.commit()
	conn.close()


#procedure to create table in my database
def createTable():
	conn = sqlite3.connect('ProjectileMotionGame.db') #connects to database
	c = conn.cursor() #cursor class allows you to invoke methods that execute sqlite statements
	#table is created with username and password fields
	c.execute("""CREATE TABLE users(
		username text,
		password text
		)""")
	conn.commit()
	conn.close()


#to create the database
def createDatabase():
	conn = sqlite3.connect(r"C:\Users\lola_\Desktop\Computer Science NEA\ProjectileMotionGame.db")
	c = conn.cursor()


home()

