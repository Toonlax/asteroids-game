import pygame
from player import Player
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group() # Creates an empty group (All updatable objects)
    drawable = pygame.sprite.Group() # Creates an empty group (All drawable objects)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    # Game Loop
    while True:
        log_state()

        # Close Button Functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black") # Makes the game background black
        updatable.update(dt) # Updates the position of any entity in the updatable group if keys are pressed
        for d in drawable:
            d.draw(screen) # Renders each element in the drawable group onto the screen
        pygame.display.flip() # Displays stuff onto the game screen
        
        dt = clock.tick(60) / 1000
   
main()