import pygame
import time
import random

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout!")

BG = pygame.transform.scale(pygame.image.load("sources/bg.jpeg"), (WIDTH, HEIGHT))

def draw():
    WIN.blit(BG, (0,0))
    # refresh the display
    pygame.display.update()



def main():
    run = True

    while run:
        # first, we check if the user has pressed on the exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw()
    
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
