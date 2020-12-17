#importing libraries that are used
import sys
from tkinter import *

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
	registerUsernameLabel = Label(window,bg="#0394fc",text="Username: ").place(x=500, y=120)
	registerUsernameEntry = Entry(window).place(x=570, y=120)
	registerPasswordLabel = Label(window,bg="#0394fc",text="Password: ").place(x=500, y=160)
	registerPasswordEntry = Entry(window).place(x=570, y=160)	

	#register button
	registerButton = Button(window,text="Register",width="8").place(x=500, y=200)

	window.mainloop()

home()