import random
import pygame

class Coin:
    def __init__(self, x, y, vel, screen_width, player_y_position):
        self.x = x
        self.y = y
        self.vel = vel
        self.screen_width = screen_width
        self.image = pygame.image.load('drawings/coin.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.max_jump_height = player_y_position - 100  # Maximum height the player can jump

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)

    def move(self):
        self.x -= self.vel
        self.y += random.randint(-3, 3)  # Change in y direction
        if self.y < self.max_jump_height:  # Check if coin is too high
            self.y = self.max_jump_height
        if self.x + self.width < 0:
            self.restart()

    def restart(self):
        self.x = self.screen_width + random.randint(50, 150)
        self.y = random.randint(self.max_jump_height, self.max_jump_height + 100)  # Random y position within player's jump reach
