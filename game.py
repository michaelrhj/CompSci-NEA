import pygame, math,sys,pymunk,os
import sliders

FPS = 60

def yep():
	print(sliders.x,sliders.y)

def create_target(space):
	body = pymunk.Body(body_type=pymunk.Body.STATIC)
	body.position= (550,450)
	shape = pymunk.Circle(body,50)
	space.add(body,shape)
	return shape

def draw_target(target):
	position_x = int(target.body.position.x)
	position_y = int(target.body.position.y)
	pygame.draw.circle(screen,(0,0,0),(position_x,position_y),50)	

#function for updating the projectile position
def updateProjectile(initVelocity,xProjectile,yProjectile,angle): #takes in required values as parameters
	time_now = pygame.time.get_ticks() #uses pygame to find current time
	#validates that initial velocity is greater than 0
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
	
	return(xProjectile,yProjectile)
"""
def updateProjectile(initVelocity,xProjectile,yProjectile,angle): #takes in required values as parameters
	time_now = pygame.time.get_ticks() #uses pygame to find current time
	if initVelocity>0 and yProjectile<800:
		time_change = time_now - start_time
		if time_change>0:
			time_change = time_change/100
			xDisplacement = initVelocity*math.cos(angle)*time_change
			yDisplacement = initVelocity*math.sin(angle)*time_change + (0.5*gravity*time_change*time_change)
			xProjectile = xProjectile + xDisplacement
			yProjectile = yProjectile - yDisplacement

	screen.blit(projectile_img,(xProjectile,yProjectile))
	"""

pygame.init()
screen = pygame.display.set_mode((800,800))

gravity = -9.8

space = pymunk.Space()
target1 = create_target(space)

projectile_img = pygame.image.load('C:/Users/M/Desktop/Files/CompSci-NEA/projectile1.png')
xProjectile = 100
yProjectile = 300
initVelocity = 42
angle = math.radians(45)
start_time = pygame.time.get_ticks()


clock = pygame.time.Clock()
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()

	screen.fill((52,110,235))

	draw_target(target1)


	updateProjectile(initVelocity,xProjectile,yProjectile,angle)


	pygame.display.flip()

	clock.tick_busy_loop(FPS)

yep()