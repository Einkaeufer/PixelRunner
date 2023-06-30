import random

import pygame


class Coin:
    def __init__(self, x, y, vel, screen_width):
        self.x = x
        self.y = y
        self.vel = vel
        self.screen_width = screen_width
        self.image = pygame.image.load('drawings/coin.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)

    def move(self):
        self.x -= self.vel
        if self.x + self.width < 0:
            self.restart()

    def restart(self):
        self.x = self.screen_width + random.randint(50, 150)
