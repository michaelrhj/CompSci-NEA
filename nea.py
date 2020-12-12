import pygame,sys
from tkinter import *
#from tkinter.ttk import *

def register():
	register_Window = Tk()
	register_Window.title("Register")

	username = Label(register_Window,text="Username: ").grid(row=1)
	username_Entry = Entry(register_Window).grid(row=1,column=1)

	password = Label(register_Window,text="Password: ").grid(row=2)
	password_Entry = Entry(register_Window,show='*').grid(row=2,column=1)

	button = Button(register_Window,text="Register").grid(row=3)

	register_Window.mainloop()

def login():
	login_Window = Tk()

	username = Label(login_Window,text="Username: ").grid(row=1)
	username_Entry = Entry(login_Window).grid(row=1,column=1)

	password = Label(login_Window,text="Password: ").grid(row=2)
	password_Entry = Entry(login_Window,show='*').grid(row=2,column=1)

	button = Button(login_Window,text="Login").grid(row=3)

	login_Window.mainloop()

def home():
	
	window = Tk()
	window.title("Home")
	window.minsize(600,200)

	register_Button = Button(window,text="Register",width=50,height=15,bg='lightblue',command=register)
	register_Button.grid(row=1)

	login_Button = Button(window,text="Login",width=50,height=15,bg='grey',command=login)
	login_Button.grid(row=1,column=1)

	window.mainloop()

'''

def first_stage(vel_init_hor,vel_init_ver):

	pygame.init()

	screen = pygame.display.set_mode((1200,650))

	projectile_img = pygame.image.load('projectile1.png')

	acc = -9.8
	time = 1

	#0.5 px ==== 30 metres 
	x =0
	y =0

	x_change = vel_init_hor * time

	#y_change = vel_init_ver * time + (0.5*acc*time*time)
	y_change = vel_init_ver*time

	running = True
	while running:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
				sys.exit()
		screen.fill((52,110,235))
		x = (x +(x_change/60))
		y = (y+(y_change/60))
		#time = time + 1
		print(x,y)
		screen.blit(projectile_img,(x,y))
		pygame.display.update()
'''

'''

		brown = (160,82,45)

		screen.blit(background_image,[0,0])

		projectile_img = pygame.image.load('projectile1.png')

		screen.blit(projectile_img,(x,y))

		pygame.draw.rect(screen,brown,(800,400,60,50))


		x= x+1




#General Setup


	

first_stage(20,20)
'''
home()