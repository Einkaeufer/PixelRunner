import pygame
import sys
from player import Player
from obstacle import Obstacle
from coin import Coin

# Initialize Pygame
pygame.init()

pygame.mixer.init()  # Initialize the mixer module
pygame.mixer.music.load('drawings/music.ogg')  # Load the music file
pygame.mixer.music.play(-1)  # Start playing the music. -1 means loop indefinitely
pygame.mixer.music.set_volume(0.3)  # Set volume to half

coin_sound = pygame.mixer.Sound('drawings/coin_collect.ogg')  # Load the coin collection sound
coin_sound.set_volume(1.0)  # Set volume to full for coin collection sound

oof_sound = pygame.mixer.Sound('drawings/oof.ogg')  # Load the collision sound
oof_sound.set_volume(1.2)  # Set volume to full for collision sound

jump_sound = pygame.mixer.Sound('drawings/jump.ogg')  # Load the collision sound
jump_sound.set_volume(0.7)  # Set volume to full for collision sound

hit_sound = pygame.mixer.Sound('drawings/hit.ogg')  # Load the collision sound
hit_sound.set_volume(0.7)  # Set volume to full for collision sound
# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60
FONT = pygame.font.Font(None, 36)  # Create a font object once and render() to create the image.

# Set up the display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def game_over(score):  # Add score parameter
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main()

        WIN.fill((0,0,0))
        draw_text('GAME OVER', FONT, (255, 0, 0), WIN, 20, 20)
        draw_text('Score: ' + str(score), FONT, (255, 255, 255), WIN, 20, 60)  # Display the score
        draw_text('Press Enter to play again', FONT, (255, 255, 255), WIN, 20, 100)
        pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True

    score = 0  # Initialize score

    # Create player, obstacle, and coin
    player_height = 60
    player_y_position = HEIGHT - 50 - player_height
    player = Player(int(WIDTH * 0.10), player_y_position)  # Player is now 10% away from the left side

    bg = pygame.image.load('drawings/wallpaper.jpg')
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))  # This line is to scale your image to fit the window

    obstacle = Obstacle(WIDTH, player_y_position, 5, WIDTH, HEIGHT)
    coin = Coin(WIDTH, player_y_position, 5, WIDTH, player_y_position)  # Create coin object

    score = 0  # Initialize score

    # Rest of your code...

    while run:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.is_jump = True
                    jump_sound.play()

        # Update game state
        player.jump()
        obstacle.move()
        coin.move()  # Move coin

        if player.collide_with_obstacle(obstacle):
            hit_sound.play()
            oof_sound.play()  # Play the collision sound
            game_over(score)  # Call game_over function when collision happens, passing score

        # Check coin collection
        if player.collide_with_coin(coin):
            score += 1  # Increase score
            coin.restart()  # Restart coin
            coin_sound.play()  # Play the coin collection sound

        # Draw everything
        WIN.blit(bg, (0, 0))  # This line sets the background
        player.draw(WIN)
        obstacle.draw(WIN)
        coin.draw(WIN)  # Draw coin

        pygame.display.update()

    pygame.quit()
    sys.exit()
