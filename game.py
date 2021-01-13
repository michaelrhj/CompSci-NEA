import pygame, math,sys,pymunk,os

FPS = 60

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


def update(velocity,projectile_x,projectile_y,angle):
	time_now = pygame.time.get_ticks()
	if velocity>0 and projectile_y<800:
		time_change = time_now - start_time
		if time_change>0:
			time_change = time_change/100
			displacement_x = velocity*math.cos(angle)*time_change
			displacement_y = velocity*math.sin(angle)*time_change + (0.5*gravity*time_change*time_change)
			projectile_x = projectile_x + displacement_x
			projectile_y = projectile_y - displacement_y

	screen.blit(projectile_img,(projectile_x,projectile_y))

pygame.init()
screen = pygame.display.set_mode((800,800))

gravity = -9.8

space = pymunk.Space()
target1 = create_target(space)

projectile_img = pygame.image.load('C:/Users/M/Desktop/Files/CompSci-NEA/projectile1.png')
projectile_x = 100
projectile_y = 300
velocity = 42
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


	update(velocity,projectile_x,projectile_y,angle)


	pygame.display.flip()

	clock.tick_busy_loop(FPS)
