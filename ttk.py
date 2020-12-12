from tkinter import *
from tkinter.ttk import *

def register():
	window = Tk()
	window.title("Home")
	window.geometry('600x200')

	style = Style()
	style.configure('TButton', font=('calibri', '10','bold'),background='green')


	registerButton = Button(window,text="Register",style='TButton')
	registerButton.place(x=0,y=0,width=300,height=200)

	loginButton = Button(window,text="Login",style='TButton')
	loginButton.place(x=300,y=0,width=300,height=200)	

	window.mainloop()


register()
