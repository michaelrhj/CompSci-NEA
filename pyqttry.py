import sys
from tkinter import *

def mainMenu():
	window = Tk()
	window.title("Main Menu")
	window.minsize(800,500)

	registerButton = Button(window,text="Register",bg='green').place(x=200,y=70,height=120,width=400)
	loginButton = Button(window,text="Login",bg='#0367fc').place(x=200,y=310,height=120,width=400)





	window.mainloop()

mainMenu()