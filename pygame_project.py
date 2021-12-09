import pygame
import random

# This project is about a spaceship that is avoiding into colliding with enemies
# User can navigate using LEFT, RIGHT, UP and DOWN arrow keys
# Images taken from https://www.flaticon.com

# Initialise pygame modules
pygame.init()

# Screen dimensions
screen_width = 600
screen_height = 600

# Create game screen
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Impact")

# Create game objects
player = pygame.image.load("player.png")
enemy1 = pygame.image.load("enemy_1.png")
enemy2 = pygame.image.load("enemy_2.png")
enemy3 = pygame.image.load("enemy_3.png")


# Resize game objects
player = pygame.transform.scale(player, (70, 70))
enemy1 = pygame.transform.scale(enemy1, (60, 60))
enemy2 = pygame.transform.scale(enemy2, (60, 60))
enemy3 = pygame.transform.scale(enemy3, (60, 60))

# Position game objects on the screen
# Player position
player_x = 500
player_y = screen_height - (player.get_height() + 70)


# Enemy1 position/coordinates
enemy1_x = random.randint(0, screen_width - enemy1.get_width())
enemy1_y = 0 - enemy1.get_height()

# Enemy2 position/coordinates
enemy2_x = random.randint(0, screen_width - enemy2.get_width())
enemy2_y = 0 - enemy2.get_height()

# Enemy2 position/coordinates
enemy3_x = random.randint(0, screen_width - enemy3.get_width())
enemy3_y = 0 - enemy3.get_height()

# This variable holds the value number of pixel the player should move
player_x_change = 0
player_y_change = 0

# The score variable will store game score
score = 0

# The level variable stores difficulty level of the game
level = 1

# Game loop for running the game until user exit the game
while 1:
    # Clear the screen
    game_screen.fill(0)

    # Display game objects on the screen
    game_screen.blit(player, (player_x, player_y))
    game_screen.blit(enemy1, (enemy1_x, enemy1_y))
    game_screen.blit(enemy2, (enemy2_x, enemy2_y))
    game_screen.blit(enemy3, (enemy3_x, enemy3_y))

    # Update the game screen
    pygame.display.flip()

    # Loop through the game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # Keys events are active when user presses a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_UP:
                player_y_change = -5
            if event.key == pygame.K_DOWN:
                player_y_change = 5

        # Keys events not active when keys user is not pressing a key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0

    # Increase y and x coordinates of the player they press one of the arrow key
    player_x += player_x_change
    player_y += player_y_change

    # Prevent player from moving outside the screen
    if player_x >= (screen_width - 70):
        player_x = (screen_width - 70)
    elif player_x <= 0:
        player_x = 0

    if player_y >= (screen_height - 70):
        player_y = (screen_height - 70)
    elif player_y <= 0:
        player_y = 0

    # Detect collision
    # Store image bounding box
    player_box = pygame.Rect(player.get_rect())
    enemy1_box = pygame.Rect(enemy1.get_rect())
    enemy2_box = pygame.Rect(enemy2.get_rect())
    enemy3_box = pygame.Rect(enemy3.get_rect())

    # Update object boxes according to their positions
    # Player box
    player_box.top = player_y
    player_box.left = player_x

    # Enemy 1 box
    enemy1_box.top = enemy1_y
    enemy1_box.left = enemy1_x

    # Enemy 2 box
    enemy2_box.top = enemy2_y
    enemy2_box.left = enemy2_x

    # Enemy 1 box
    enemy3_box.top = enemy3_y
    enemy3_box.left = enemy3_x

    if player_box.colliderect(enemy1_box) or player_box.colliderect(enemy2_box) or player_box.colliderect(enemy3_box):
        # Display information
        print("GAME OVER")
        print(f"Your score: {score}")
        print(f"LEVEL: {level-1}")

        # Exit the game
        pygame.quit()
        exit(0)

    # Make enemy approach the player by increasing enemy y position with random number + level
    enemy1_y += (random.randint(1, 3) + level)
    enemy2_y += (random.randint(1, 3) + level)
    enemy3_y += (random.randint(1, 3) + level)

    # Restart the enemy x and y position after they go beyond screen at the bottom
    if enemy1_y > screen_height and enemy2_y > screen_height and enemy3_y > screen_height:
        score += 1

        # After adding 5 on the score increase level by 1
        if score % 5 == 0:
            level += 1

        enemy1_y = 0 - enemy1.get_height()
        enemy1_x = random.randint(0, screen_width - enemy1.get_width())

        enemy2_y = 0 - enemy2.get_height()
        enemy2_x = random.randint(0, screen_width - enemy2.get_width())

        enemy3_y = 0 - enemy3.get_height()
        enemy3_x = random.randint(0, screen_width - enemy3.get_width())
