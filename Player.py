import pygame, sys
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, vel):
        super().__init__()
        self.frame = 0
        self.health = 100
        self.max_health = 500
        self.is_jumping = False
        self.is_falling = True
        self.image = pygame.image.load('assets/img/Woodcutter.png')
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.direction = "right"
        self.animation_count = 0
        self.mask = None

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

    def move(self,dx,dy):
        self.rect.x += dx
        self.rect.y += dy
        
    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)

    def draw(self, screen):
        pygame.draw.rect(screen, red, self.rect, 0)

    def update(self):
        if self.rect.left > WIDTH:
            self.rect.right = 0



