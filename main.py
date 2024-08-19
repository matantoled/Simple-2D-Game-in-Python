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

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0,0))

    time_text = FONT.render(f'Time: {round(elapsed_time)}s', 1, "white")
    WIN.blit(time_text, (10,10))


    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    # refresh the display
    pygame.display.update()



def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, 
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    # the first star that we add will be added in 2000 milliseconds
    star_add_increment = 2000

    # tells us when we should add the next star
    star_count = 0

    # all the stars are currently on the screen
    stars = []

    hit = False


    while run:
        # framerate (the number of times the while loop will be running)
        star_count += clock.tick(60)

        # calculate the elapsed time since the start of the program or a specific event
        elapsed_time = time.time() - start_time


        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0



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
        

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1, "red")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)
    
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
