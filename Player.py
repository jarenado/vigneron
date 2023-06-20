import pygame, sys
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.frame = 0
        self.health = 100
        self.max_health = 500
        self.is_jumping = False
        self.is_falling = True
        self.image = pygame.image.load('assets/img/Woodcutter.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = HEIGHT - self.rect.height - 190
        pygame.draw.rect(self.image, red, self.rect, 0)

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount**2 * 0.1 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

    def move_right(self):
        self.rect.x += 5
        pygame.draw.rect(self.image, red, self.rect, 0)

    def move_left(self):
        self.rect.x -= 5
        pygame.draw.rect(self.image, red, self.rect, 0)

    def update(self):
        if self.rect.left > WIDTH:
            self.rect.right = 0
