import pygame
import random  # Add this line to import the random module

class Obstacle:
    def __init__(self, x, player_y_position, vel, screen_width, screen_height):
        self.x = x
        self.y = player_y_position
        self.vel = vel
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load('drawings/obstacle.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = (self.x + 10, self.y + 10, self.width - 20, self.height - 20)
        self.player_y_position = player_y_position

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x + 10, self.y + 10, self.width - 20, self.height - 20)

    def move(self):
        self.x -= self.vel
        if self.x + self.width < 0:
            self.restart()

    def restart(self):
        self.x = self.screen_width + random.choice([i for i in range(50, 150, 10)])
        self.y = self.player_y_position  # Obstacle now restarts at the player's height
