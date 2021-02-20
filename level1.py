from tkinter import *
import math, scipy, sys, pymunk, pygame
from scipy.constants import g
gravity = scipy.constants.g
FPS = 60

def home():
    #window setup
    window = Tk()
    window.title("Level 1 Sliders")
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

    #skins options
    skinOptions = ['Dot','Fukiya','Rocket'] #the options available
    skinVariable = StringVar(window) #variable that holds the value
    skinVariable.set(skinOptions[0])
    skinLabel = Label(window,text="Choose projectile skin: ",bg="#0394fc")
    skinLabel.place(x=0,y=180)
    chooseSkin = OptionMenu(window,skinVariable,*skinOptions) #dropdown menu
    chooseSkin.place(x=0,y=200)

    #button used to submit values to the game
    submitButton = Button(window,text="Fire Projectile",width="15",command=lambda: pygame(velocitySlider.get(),angleSlider.get(),skinVariable.get()))
    submitButton.place(x=320,y=450)


    window.mainloop()




#pygame mainloop
def pygame(x,y,z):
    import pygame
    xProjectile = 0
    yProjectile = 0
     #initialises target
    def createTarget(space):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position= (400,450) #specifies position
        shape = pymunk.Circle(body,50) #shape type
        space.add(body,shape)
        return shape
    #draws target on pygame screen
    def drawTarget(target):
        xPosition = int(target.body.position.x)
        yPosition = int(target.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(xPosition,yPosition),50)
    
    def updateProjectile(initVelocity,xProjectile,yProjectile,angle): #takes in required values as parameters
        def collisionCheck(xProjectile,yProjectile): #takes in current projectile values
            def collidePopup():
                window = Toplevel()
                label = Label(window,text="Collision. You have completed the level").grid(row=1) #displays pop up screen telling user there has been a collision

            distance = math.sqrt(math.pow(400-xProjectile,2) + math.pow(450-yProjectile,2)) #calculates distance using pythagoras theorem
            if distance<70: #gives leeway as object sizes mean that the distance may never actually be zero
                pygame.quit()
                collidePopup() #calls collision function
        timeNow = pygame.time.get_ticks() #uses pygame to find current time
        #validates that initial velocity is greater than 0
        if initVelocity>0:
            timeChange = timeNow - startTime #calculates change in time between start of the game and now
            timeChange = timeChange/2000
            #horizontal and vertical displacement calculated
            xDisplacement = initVelocity*math.cos(math.radians(angle))*timeChange 
            yDisplacement = ((initVelocity*math.sin(math.radians(angle))*timeChange) - (0.5*(gravity)*timeChange*timeChange))
            yAnimate = 10*yDisplacement
            xAnimate = 10*xDisplacement
            #displacement is added onto the intial position
            xProjectile = xProjectile + xAnimate
            yProjectileReal = yProjectile + yDisplacement
            yProjectile = 600 - (yProjectile + yAnimate) #change for pygame
        else:
            window = Toplevel()
            label = Label(window,text="Projectile motion cannot be calculated. Velocity must be greater than 0").grid(row=1)
        #boundary conditions
        if xProjectile>600:
            running = False
            pygame.quit()
        if yProjectileReal>600 or yProjectileReal<0:
            running = False
            pygame.quit()

        screen.blit(projectileImg,(xProjectile,yProjectile))
        collisionCheck(xProjectile,yProjectile)

    pygame.init() #initialises pygame
    screen = pygame.display.set_mode((600,600)) #sets screen
    pygame.display.set_caption("Level 1")
    space = pymunk.Space()
    target1 = createTarget(space)
    startTime = pygame.time.get_ticks()
    if z == 'Fukiya':
        projectileImg = pygame.image.load('C:/Users/M/Desktop/Files/CompSci-NEA/fukiya.png')
    elif z== 'Rocket':
        projectileImg = pygame.image.load('C:/Users/M/Desktop/Files/CompSci-NEA/rocket.png')
    else:
        projectileImg = pygame.image.load('C:/Users/M/Desktop/Files/CompSci-NEA/projectile1.png')
    clock = pygame.time.Clock() #sets clock
    running = True
    while running: #pygame loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
      

        screen.fill((52,110,235)) #screen background
        #gets the values from the sliders
        drawTarget(target1)
        updateProjectile(x,xProjectile,yProjectile,y) #sends the values to the updateProjectile function
        pygame.display.flip() #updates display
        clock.tick_busy_loop(FPS)

home()

