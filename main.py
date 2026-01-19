import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game Loop
    while True:
        log_state()

        # Close Button Functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black") # Makes the game background black
        player.update(dt) # Updates the position of the player if keys are pressed
        player.draw(screen) # Renders the player onto the screen
        pygame.display.flip() # Displays stuff onto the game screen
        
        dt = clock.tick(60) / 1000
   
main()