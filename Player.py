import pygame, sys
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/img/Woodcutter.png')
        self.rect = self.image.get_rect()
        # self.rect.center = (WIDTH / 2, HEIGHT)
        self.rect.x = 0
        self.rect.y = HEIGHT - self.rect.height
        pygame.draw.rect(self.image, red, self.rect, 0)

    def move_right(self):
        self.rect.x += 5
        pygame.draw.rect(self.image, red, self.rect, 0)

    def move_left(self):
        self.rect.x -= 5
        pygame.draw.rect(self.image, red, self.rect, 0)

    def update(self):
        if self.rect.left > WIDTH:
            self.rect.right = 0
