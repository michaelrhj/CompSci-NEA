import pygame

def updateProjectile(initVelocity,xProjectile,yProjectile,angle): #takes in required values as parameters
    timeNow = pygame.time.get_ticks() #uses pygame to find current time
    #validates that initial velocity is greater than 0
    if initVelocity>0:
        timeChange = timeNow - startTime #calculates change in time between start of the game and now 
        #horizontal and vertical displacement calculated
        xDisplacement = initVelocity*math.cos(math.radians(angle))*timeChange 
        yDisplacement = (initVelocity*math.sin(math.radians(angle))*timeChange) - (0.5*gravity*timeChange*timeChange)
 
        #displacement is added onto the intial position
        xProjectile = xProjectile + xDisplacement
        yProjectile = yProjectile - yDisplacement #change for pygame
    else:
        window = Toplevel()
        label = Label(window,text="Projectile motion cannot be calculated. Velocity must be greater than 0").grid(row=1)

    print(xProjectile,yProjectile)

#initialises target
def createTarget(space):
	body = pymunk.Body(body_type=pymunk.Body.STATIC)
	body.position= (900,450) #specifies position
	shape = pymunk.Circle(body,50) #shape type
	space.add(body,shape)
	return shape
#draws target on pygame screen
def drawTarget(target):
	xPosition = int(target.body.position.x)
	yPosition = int(target.body.position.y)
	pygame.draw.circle(screen,(0,0,0),(xPosition,yPosition),50)


pygame.init() #initialises pygame
screen = pygame.display.set_mode((1000,600)) #sets screen
clock = pygame.time.Clock() #sets clock
space = pymunk.Space()
target1 = createTarget(space)
startTime = pygame.time.get_ticks()
projectileImg = pygame.image.load('C:/Users/M/Desktop/Files/CompSci-NEA/projectile1.png')
running = True
while running: #pygame loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    screen.fill((52,110,235)) #screen background
    #gets the values from the sliders
 
    drawTarget(target1)
    pygame.display.flip() #updates display
    clock.tick_busy_loop(FPS)