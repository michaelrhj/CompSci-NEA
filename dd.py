import pygame
import random
import math

# Window size
WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 400
FPS           = 60

# background colours
INKY_GREY    = ( 128, 128, 128 )

INITIAL_VELOCITY_LOW  = 10  # pixels per millisecond (adjusted later)
INITIAL_VELOCITY_HIGH = 100
LAUNCH_ANGLE          = 80  # random start-angle range

class Projectile( pygame.sprite.Sprite ):
    GRAVITY          = -9.8  

    def __init__( self, bitmap, start_x, start_y, velocity=0, angle=0 ):
        pygame.sprite.Sprite.__init__( self )
        self.image       = bitmap
        self.rect        = bitmap.get_rect()
        self.start_x     = start_x
        self.start_y     = start_y
        self.rect.center = ( ( start_x, start_y ) )
        # Physics
        self.start_time = pygame.time.get_ticks()   # "now" in milliseconds
        self.velocity   = velocity
        self.angle      = math.radians( angle )     # Note: convert Degrees to Radians            

    def update( self ):
        time_now = pygame.time.get_ticks()
        if ( self.velocity > 0 and self.rect.y < WINDOW_HEIGHT - self.rect.height ):
            time_change = ( time_now - self.start_time ) 
            if ( time_change > 0 ):
                time_change /= 100.0  # fudge for metres/second to pixels/millisecond
                # re-calculate the displacement
                # x
                displacement_x  = self.velocity * time_change * math.sin( self.angle ) 
                # y
                half_gravity_time_squared = self.GRAVITY * time_change * time_change / 2.0
                displacement_y  = self.velocity * time_change * math.cos( self.angle ) + half_gravity_time_squared 

                # reposition sprite
                self.rect.center = ( ( self.start_x + int( displacement_x ), self.start_y - int( displacement_y ) ) )

                # Stop at the bottom of the window
                if ( self.rect.y >= WINDOW_HEIGHT - self.rect.height ):
                    self.rect.y = WINDOW_HEIGHT - self.rect.height
                    self.velocity = 0
                    self.kill()   # remove the sprite


### MAIN
pygame.init()
SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
window  = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ), SURFACE )
pygame.display.set_caption("Projectile Motion Example")

# Load resource image(s)
sprite_image = pygame.image.load( "ball.png" )#.convert_alpha()

# Make some sprites 
screen_centre_x = WINDOW_WIDTH  // 2
screen_bottom_y = WINDOW_HEIGHT - 10
SPRITES = pygame.sprite.Group()   
for i in range( 20 ):
    speed = random.randrange( INITIAL_VELOCITY_LOW, INITIAL_VELOCITY_HIGH )  # metres per second
    angle = random.randrange( -LAUNCH_ANGLE, LAUNCH_ANGLE ) 
    new_sprite = Projectile( sprite_image, screen_centre_x, screen_bottom_y, speed, angle )
    SPRITES.add( new_sprite )

# Main Loop
clock = pygame.time.Clock()
done  = False
while not done:
    # Handle user-input
    for event in pygame.event.get():
        if ( event.type == pygame.QUIT ):
            done = True

    # Repaint the screen
    window.fill( INKY_GREY )
    SPRITES.update()          # re-position the sprites
    SPRITES.draw( window )    # draw the sprites

    # Update the window, but not more than 60fps
    pygame.display.flip()
    clock.tick_busy_loop( FPS )

pygame.quit()
