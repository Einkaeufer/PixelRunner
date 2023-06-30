import pygame
import sys
from player import Player
from obstacle import Obstacle
from coin import Coin  # Import the Coin class

# Initialize Pygame
pygame.init()

pygame.mixer.init()  # Initialize the mixer module
pygame.mixer.music.load('drawings/music.ogg')  # Load the music file
pygame.mixer.music.play(-1)  # Start playing the music. -1 means loop indefinitely
pygame.mixer.music.set_volume(0.5)  # Set volume to half

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

    # Create player, obstacle, and coin
    player_height = 60
    player_y_position = HEIGHT - 50 - player_height
    player = Player(int(WIDTH * 0.10), player_y_position)  # Player is now 10% away from the left side

    bg = pygame.image.load('drawings/wallpaper.jpg')
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))  # This line is to scale your image to fit the window

    obstacle = Obstacle(WIDTH, player_y_position, 5, WIDTH, HEIGHT)
    coin = Coin(WIDTH, player_y_position, 5, WIDTH, player_y_position)

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

        # Update game state
        player.jump()
        obstacle.move()
        coin.move()  # Move coin

        # Check collision
        collide_result = player.collide(obstacle, coin)  # Pass coin as argument
        if collide_result == 'obstacle':
            game_over(score)  # Pass score to game_over function
        elif collide_result == 'coin':
            coin.restart()  # Restart coin if it has been collected
            score += 1  # Increase score

        # Draw everything
        WIN.blit(bg, (0, 0))  # This line sets the background
        player.draw(WIN)
        obstacle.draw(WIN)
        coin.draw(WIN)  # Draw coin

        pygame.display.update()

    pygame.quit()
    sys.exit()
