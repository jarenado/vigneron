import pygame, sys
from os import listdir
from os.path import isfile, join
from settings import *


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height, direction='False'):
    path = join('assets/img/', dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image))

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32) 
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(surface)

        if direction:
            all_sprites[image.replace(".png","") + '_right'] = flip(sprites)
            all_sprites[image.replace('.png','') + '_left'] = sprites
        else:
            all_sprites[image.replace('.png','')] = sprites

    return all_sprites

class Player(pygame.sprite.Sprite):
    SPRITES = load_sprite_sheets("MainCharacters", "MaskDude", 34, 44)
    ANIMATION_DELAY = 5

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
        self.fall_count = 0

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
        print('left')
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        print('right')
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        # self.y_vel += min(1, (self.fall_count / FPS) * GRAVITY)
        self.move(self.x_vel, self.y_vel)

        self.fall_count += 1
        self.update_sprite()

    def update_sprite(self):
        sprite_sheet = "idle-bunny"
        if self.x_vel != 0:
            sprite_sheet = "idle-bunny"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1

    def draw(self, screen):
        screen.blit(self.sprite, (self.rect.x, self.rect.y))



