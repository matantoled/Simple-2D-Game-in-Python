import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout!")

BG = pygame.transform.scale(pygame.image.load("sources/bg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VELOCITY = 5

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time):
    WIN.blit(BG, (0,0))

    time_text = FONT.render(f'Time: {round(elapsed_time)}s', 1, "white")
    WIN.blit(time_text, (10,10))


    pygame.draw.rect(WIN, "red", player)

    # refresh the display
    pygame.display.update()



def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, 
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0


    while run:
        # framerate (the number of times the while loop will be running)
        clock.tick(60)

        # calculate the elapsed time since the start of the program or a specific event
        elapsed_time = time.time() - start_time

        # first, we check if the user has pressed on the exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        # ensure that the *entire player object* stays within the screen boundaries when moving to the right,
        # so we also have to consider the size of the width of the player object
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
            player.x += PLAYER_VELOCITY
        


        draw(player, elapsed_time)
    
    pygame.quit()


if __name__ == "__main__":
    main()
"""
This block (above) ensures that the main function is only 
executed when this script is run directly,
not when it is imported as a module in another script.

Explanation:
- The `if __name__ == "__main__":` statement checks whether the script is being run directly.
- If true, it calls the `main()` function, starting the game.
- If this script were imported into another script, the `main()` function would not run 
  automatically, preventing unintended execution of the game.
"""
