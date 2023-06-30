import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_jump = False  # Add this line
        self.jump_count = 12
        self.initial_height = self.y  # This line needs to be moved after self.y
        self.image = pygame.image.load('drawings/runner.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = (self.x + 10, self.y + 10, self.width - 20, self.height - 20)  # This creates a hitbox that is smaller than the image size


    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)  # Update the hitbox here


    def jump(self):
        if self.is_jump:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jump = False
                self.jump_count = 10
                self.y = self.initial_height  # Reset height after jump

    def collide(self, obs, coin):
        if self.hitbox[0] < obs.hitbox[0] + obs.hitbox[2] and self.hitbox[0] + self.hitbox[2] > obs.hitbox[0]:
            if self.hitbox[1] < obs.hitbox[1] + obs.hitbox[3] and self.hitbox[1] + self.hitbox[3] > obs.hitbox[1]:
                return 'obstacle'
        if self.hitbox[0] < coin.hitbox[0] + coin.hitbox[2] and self.hitbox[0] + self.hitbox[2] > coin.hitbox[0]:
            if self.hitbox[1] < coin.hitbox[1] + coin.hitbox[3] and self.hitbox[1] + self.hitbox[3] > coin.hitbox[1]:
                return 'coin'
        return False

    def collide_with_obstacle(self, obstacle):
        player_hitbox = pygame.Rect(self.hitbox)
        obstacle_hitbox = pygame.Rect(obstacle.hitbox)
        return player_hitbox.colliderect(obstacle_hitbox)

    def collide_with_coin(self, coin):
        player_hitbox = pygame.Rect(self.hitbox)
        coin_hitbox = pygame.Rect(coin.hitbox)
        return player_hitbox.colliderect(coin_hitbox)