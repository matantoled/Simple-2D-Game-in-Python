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
BUTTON_FONT = pygame.font.SysFont("comicsans", 40)

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f'Time: {round(elapsed_time)}s', 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()

def draw_lost_screen(player, elapsed_time, stars):
    draw(player, elapsed_time, stars)  # Keep the screen visible
    lost_text = FONT.render("You Lost!", 1, "red")
    WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2 - 50))

    restart_button = pygame.Rect(WIDTH/2 - 100, HEIGHT/2 + 20, 200, 50)
    pygame.draw.rect(WIN, "green", restart_button)
    restart_text = BUTTON_FONT.render("Restart", 1, "white")
    WIN.blit(restart_text, (restart_button.x + (restart_button.width - restart_text.get_width())/2, 
                            restart_button.y + (restart_button.height - restart_text.get_height())/2))

    pygame.display.update()
    return restart_button

def main():
    run = True
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # Reset the cursor at the start of the game

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, 
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock = pygame.time.Clock()

    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000   # the first star that we add will be added in 2000 milliseconds

    star_count = 0  # tells us when we should add the next star

    
    stars = []      # all the stars are currently on the screen

    hit = False
    hit_star = None  # To keep track of the star that hits the player

    while run:
        star_count += clock.tick(60) # framerate (the number of times the while loop will be running)
        elapsed_time = time.time() - start_time # calculate the elapsed time since the start of the program or a specific event

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
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
            player.x += PLAYER_VELOCITY
        
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                hit = True
                hit_star = star  # Keep the star that hits the player
                break

        if hit:
            if hit_star:
                # Ensure the star that caused the hit remains visible
                stars.append(hit_star)
            restart_button = draw_lost_screen(player, elapsed_time, stars)
            countdown_start = time.time()
            countdown = 10  # 10 seconds countdown

            while True:
                # Calculate remaining time
                remaining_time = countdown - int(time.time() - countdown_start)
                if remaining_time <= 0:
                    pygame.quit()
                    return

                # Clear the previous countdown text before drawing the new one
                pygame.draw.rect(WIN, BG.get_at((0, 0)), 
                                 (WIDTH/2 - 100, HEIGHT/2 + 80, 200, 50))
                countdown_text = FONT.render(f"Closing in {remaining_time}s", 1, "red")
                WIN.blit(countdown_text, (WIDTH/2 - countdown_text.get_width()/2, HEIGHT/2 + 80))
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_button.collidepoint(event.pos):
                            main()
                            return
                    if event.type == pygame.MOUSEMOTION:
                        if restart_button.collidepoint(event.pos):
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                        else:
                            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

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
