#importing libraries that are used
import sys, sqlite3, pygame, math, pymunk, os
import winsound
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

	#settings button
	settingsPhoto = PhotoImage(file='C:\\Users\\M\\Desktop\\Files\\CompSci-NEA\\settings.png') #references settings image
	settingsButton = Button(window,text="Settings",image=settingsPhoto,compound=LEFT,command=settingsMenu).place(x=50,y=430)

	#instructions button
	instructionsButton = Button(window,text="Instructions",height=2,command=openInstructions).place(x=350,y=430)

	window.mainloop()

def openInstructions():
	os.startfile('C:\\Users\\M\\Desktop\\Files\\CompSci-NEA\\README.txt') #opens the README file
def settingsMenu():	
	musicIsOn = False #sets value
	def switch(musicIsOn):
		if musicIsOn: 
			musicIsOn = False
			winsound.PlaySound(None, winsound.SND_PURGE) #stops music
		else:
			winsound.PlaySound(r'C:\Users\M\Desktop\Files\CompSci-NEA\music.wav',winsound.SND_ASYNC) #plays music
			return (musicIsOn == True)
		
	#menu setup
	
	window = Toplevel()
	window.title("Settings")
	window.minsize(400,250)
	window.configure(bg="#0394fc")
	#label and button
	musicLabel = Label(window,text="Music is Off",bg="#0394fc").place(x=50,y=50)
	#musicPhoto = PhotoImage(file='C:\\Users\\M\\Desktop\\Files\\CompSci-NEA\\music-note.png') #references music image
	musicButton = Button(window,text="Toggle Music",height=2,command=lambda: switch(musicIsOn)).place(x=130,y=50)


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
			launch(enteredUsername)
		else:
			window = Toplevel()
			label = Label(window,text="Login unsuccessful").grid(row=1)
	else:
		window = Toplevel()
		label = Label(window,text="Login unsuccessful").grid(row=1)

def launch(enteredUsername):
	conn = sqlite3.connect('ProjectileMotionGame.db') #connects to database
	c = conn.cursor() #cursor class allows you to invoke methods that execute sqlite statements
	validate = c.execute("SELECT level FROM levels WHERE username=?", (enteredUsername,)).fetchone() #checks database for entries with the corresponding username
	'''	#if validate == '1':
		import level1 #loads correct level
	#elif validate == '2':
		import level2
		'''
	import level1



#procedure to create table in my database
'''
def createTable():
	conn = sqlite3.connect('ProjectileMotionGame.db') #connects to database
	conn.execute("PRAGMA foreign_keys = 1")
	c = conn.cursor() #cursor class allows you to invoke methods that execute sqlite statements
	#table is created with username and password fields
	c.execute("""CREATE TABLE users(
		username text PRIMARY KEY,
		password text
		)""")
	conn.commit() #changes are saved
	conn.close() #connection closed
'''
def delete():
	conn = sqlite3.connect('ProjectileMotionGame.db')
	c = conn.cursor()
	c.execute("DROP TABLE users")
	c.execute("DROP TABLE levels")
	print("Table dropped...")
	conn.commit()
	conn.close()

def createTable():
	conn = sqlite3.connect('ProjectileMotionGame.db') #connects to database
	conn.execute("PRAGMA foreign_keys = ON")
	c = conn.cursor() #cursor class allows you to invoke methods that execute sqlite statements
	#table is created with username and password fields
	#table is created with username and password fields
	c.execute("""CREATE TABLE users(
		username text PRIMARY KEY,
		password text
		)""")
	#conn.commit() #changes are saved
	#conn.close() #connection closed

	c.execute("""CREATE TABLE levels(
		username text,
		level int DEFAULT 1,
		FOREIGN KEY (username) REFERENCES users(username))""") #foreign key is defined
	conn.commit() #changes are saved
	conn.close() #connection closed

home()