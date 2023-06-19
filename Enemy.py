import pygame, sys
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/img/GraveRobber.png')
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - self.rect.width
        self.rect.y = HEIGHT - self.rect.height
        flipped = pygame.transform.flip(self.image, True, False)
        pygame.draw.rect(flipped, red, self.rect, 0)

    def update(self):
        self.rect.x -= 5
        pygame.draw.rect(self.image, red, self.rect, 0)

    def move_right(self):
        self.rect.x += 5
        pygame.draw.rect(self.image, red, self.rect, 0)

    def move_left(self):
        self.rect.x -= 5
        pygame.draw.rect(self.image, red, self.rect, 0)
