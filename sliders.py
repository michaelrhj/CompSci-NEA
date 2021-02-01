from tkinter import *
import game, math, scipy
from scipy.constants import g
gravity = scipy.constants.g
print(gravity)

def home():
    #window setup
    window = Tk()
    window.title("Sliders")
    window.minsize(800,500)
    window.configure(bg="#0394fc")
    
    #label and slider for velocity entry
    velocityLabel = Label(window,text="Velocity 0 to 30 (m/s): ",bg="#0394fc")
    velocityLabel.place(x=0,y=20)
    velocitySlider = Scale(window, from_=0.0, to=30.0, orient=HORIZONTAL,length=300,resolution=0.1,bg="#0394fc")
    velocitySlider.place(x=0,y=40)

    #label and slider for angle entry
    angleLabel = Label(window,text="Angle 0 to 90 (degrees): ",bg="#0394fc")
    angleLabel.place(x=400,y=20)
    angleSlider = Scale(window, from_=0.0, to=90.0, orient=HORIZONTAL,length=350,resolution=0.1,bg="#0394fc")
    angleSlider.place(x=400,y=40)

    #button used to submit values to the game
    submitButton = Button(window,text="Submit",width="8",command=lambda: getval(velocitySlider.get(),angleSlider.get()))
    submitButton.place(x=320,y=100)

    window.mainloop()

#gets the values from the sliders
def getval(x,y):
    updateProjectile(x,0,0,y) #sends the values to the updateProjectile function

def updateProjectile(initVelocity,xProjectile,yProjectile,angle): #takes in required values as parameters
    #time_now = pygame.time.get_ticks() #uses pygame to find current time
    #validates that initial velocity is greater than 0
    if initVelocity>0:
        #time_change = time_now - start_time #calculates change in time between start of the game and now 
        time_change=2
        #horizontal and vertical displacement calculated
        xDisplacement = initVelocity*math.cos(math.radians(angle))*time_change 
        yDisplacement = (initVelocity*math.sin(math.radians(angle))*time_change) - (0.5*gravity*time_change*time_change)
 
        #displacement is added onto the intial position
        xProjectile = xProjectile + xDisplacement
        yProjectile = yProjectile + yDisplacement #change for pygame
    else:
        window = Toplevel()
        label = Label(window,text="Projectile motion cannot be calculated. Velocity must be greater than 0").grid(row=1)

    print(xProjectile,yProjectile)

home()