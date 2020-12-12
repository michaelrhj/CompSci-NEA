import pygame, sys, pymunk,math

def create_projectile(space):
	body = pymunk.Body(1,100,body_type=pymunk.Body.DYNAMIC)
	body.position = (50,450)
	shape = pymunk.Circle(body,100)
	space.add(body,shape)
	return shape

def draw_projectile(projectile):
	position_x = int(projectile.body.position.x)
	position_y = int(projectile.body.position.y)
	projectile_rect = projectile_surface.get_rect(center = (position_x,position_y))
	screen.blit(projectile_surface,projectile_rect)

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

pygame.init()
screen = pygame.display.set_mode((1200,650))
clock = pygame.time.Clock()
 
space = pymunk.Space()

grav_x = 10
grav_y = -10

projectile_surface = pygame.image.load('projectile1.png')

projectile1 = create_projectile(space)
target1 = create_target(space)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			sys.exit()

	screen.fill((52,110,235))
	draw_projectile(projectile1)
	draw_target(target1)
	if projectile1.position_y>=650:
		grav_y = -1*grav_y
	space.gravity = (grav_x,grav_y)
	space.step(1/50)
	pygame.display.update()
	clock.tick(100)