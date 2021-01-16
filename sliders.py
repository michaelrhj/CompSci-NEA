from tkinter import *
import game

def home():
    #window setup
    window = Tk()
    window.title("Sliders")
    window.minsize(800,500)
    window.configure(bg="#0394fc")
    
    #label and slider for velocity entry
    velocityLabel = Label(window,text="Velocity 0 to 30 (m/s): ")
    velocityLabel.grid(row=1)
    velocitySlider = Scale(window, from_=0.0, to=30.0, orient=HORIZONTAL,length=600,resolution=0.1)
    velocitySlider.grid(row=2)

    #label and slider for angle entry
    angleLabel = Label(window,text="Angle 0 to 90 (degrees): ")
    angleLabel.grid(row=3)
    angleSlider = Scale(window, from_=0.0, to=90.0, orient=HORIZONTAL,length=600,resolution=0.1)
    angleSlider.grid(row=4)

    #button used to submit values to the game
    submitButton = Button(window,text="Submit",width="8",command=lambda: getval(velocitySlider.get(),angleSlider.get()))
    submitButton.grid(row=5)

    window.mainloop()

def getval(x,y):
    updateProjectile(x,0,0,y)

def updateProjectile(initVelocity,xProjectile,yProjectile,angle): #takes in required values as parameters
    time_now = pygame.time.get_ticks() #uses pygame to find current time
    #validates that initial velocity is greater than 0
    time_now=5
    start_time=0
    if initVelocity>0:
        time_change = time_now - start_time #calculates change in time between start of the game and now 
        #horizontal and vertical displacement calculated
        xDisplacement = initVelocity*math.cos(angle)*time_change 
        yDisplacement = initVelocity*math.sin(angle)*time_change + (0.5*gravity*time_change*time_change)
        #displacement is added onto the intial position
        xProjectile = xProjectile + xDisplacement
        yProjectile = yProjectile - yDisplacement
    else:
        window = Toplevel()
        label = Label(window,text="Projectile motion cannot be calculated. Velocity must be greater than 0").grid(row=1)

    print(xProjectile,yProjectile)

home()