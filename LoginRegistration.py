#importing libraries that are used
import sys, sqlite3, pygame, math, pymunk, os 

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
	loginUsernameEntry = Entry(window)
	loginUsernameEntry.place(x=80, y=120)
	loginPasswordLabel = Label(window,bg="#0394fc",text="Password: ").place(x=10, y=160)
	loginPasswordEntry = Entry(window,show="*") #the password is blanked out
	loginPasswordEntry.place(x=80, y=160)

	#login button
	loginButton = Button(window,text="Login",width="8",command=lambda:loginUser(loginUsernameEntry.get(),loginPasswordEntry.get())).place(x=10, y=200)

	#register labels and entries
	registerUsernameLabel = Label(window,bg="#0394fc",text="Username: ").place(x=500, y=120)
	registerUsernameEntry = Entry(window)
	registerUsernameEntry.place(x=570, y=120)
	registerPasswordLabel = Label(window,bg="#0394fc",text="Password: ").place(x=500, y=160)
	registerPasswordEntry = Entry(window,show="*") #the password is blanked out
	registerPasswordEntry.place(x=570, y=160)	

	#register button
	registerButton = Button(window,text="Register",width="8",command=lambda: registerUser(registerUsernameEntry.get(),registerPasswordEntry.get())).place(x=500, y=200)

	window.mainloop()


#procedure to register the user

def registerUser(enteredUsername,enteredPassword): #takes entered values as parameters
	if len(enteredPassword)>=1 and len(enteredUsername)>=1:	#if username/ password field is not blank
		conn = sqlite3.connect('ProjectileMotionGame.db') #connects to database
		c = conn.cursor() #cursor class allows you to invoke methods that execute sqlite statements
		#checks to see if username is already in database
		for row in c.execute("SELECT * FROM users WHERE username=?",(enteredUsername,)):
			window = Toplevel()
			label = Label(window,text="Registration unsuccessful").grid(row=1)	
			
		#if the username is not already taken, carry on as normal
		else:
			c.execute("INSERT INTO users VALUES (?,?)",(enteredUsername,enteredPassword)) #inserts values into the database
			window = Toplevel()
			label = Label(window,text="Registration successful").grid(row=1)
		conn.commit() #changes are saved
		conn.close() #connection closed
	else: #if username/ password field is blank
		window = Toplevel()
		label = Label(window,text="Username/ Password cannot be blank").grid(row=1)

#procedure to login the user
def loginUser(enteredUsername,enteredPassword):  #takes entered values as parameters
	conn = sqlite3.connect('ProjectileMotionGame.db') #connects to database
	c = conn.cursor() #cursor class allows you to invoke methods that execute sqlite statements
	validate = c.execute("SELECT username, password FROM users WHERE username=?", (enteredUsername,)).fetchone() #checks database for entries with the corresponding username
	if validate: # if an entry is found
		username, password = validate
		if enteredPassword == validate[1]: #checks entered password against stored password
			window = Toplevel()
			label = Label(window,text="Login successful").grid(row=1)
			launch()
		else:
			window = Toplevel()
			label = Label(window,text="Login unsuccessful").grid(row=1)
	else:
		window = Toplevel()
		label = Label(window,text="Login unsuccessful").grid(row=1)

def launch():
	import sliders



#procedure to create table in my database
def createTable():
	conn = sqlite3.connect('ProjectileMotionGame.db') #connects to database
	c = conn.cursor() #cursor class allows you to invoke methods that execute sqlite statements
	#table is created with username and password fields
	c.execute("""CREATE TABLE users(
		username text,
		password text
		)""")
	conn.commit() #changes are saved
	conn.close() #connection closed


home()

