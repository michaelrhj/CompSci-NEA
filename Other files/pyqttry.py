#importing libraries that are used
import sys
from tkinter import *

#main menu screen
def mainMenu():
	#window setup
	window = Tk()
	window.title("Main Menu")
	window.minsize(800,500)
	#buttons
	registerButton = Button(window,text="Register",bg='green',command=registerWindow).place(x=200,y=70,height=120,width=400)
	loginButton = Button(window,text="Login",bg='#0367fc',command=loginWindow).place(x=200,y=310,height=120,width=400)

	window.mainloop()

def registerWindow():
	#window setup
	window=Tk()
	window.title("Register")
	window.minsize(800,500)

	#labels and entries
	usernameLabel = Label(window,text="Username: ").place(x=0, y=20)
	usernameEntry = Entry(window).place(x=70, y=20)
	passwordLabel = Label(window,text="Password: ").place(x=0, y=60)
	passwordEntry = Entry(window).place(x=70, y=60)

	#register button
	registerButton = Button(window,text="Register").place(x=0, y=100)

def loginWindow():
	#window setup
	window=Tk()
	window.title("Login")
	window.minsize(800,500)

	#labels and entries
	usernameLabel = Label(window,text="Username: ").place(x=0, y=20)
	usernameEntry = Entry(window).place(x=70, y=20)
	passwordLabel = Label(window,text="Password: ").place(x=0, y=60)
	passwordEntry = Entry(window).place(x=70, y=60)	

	#login button
	registerButton = Button(window,text="Login").place(x=0, y=100)
	
mainMenu()