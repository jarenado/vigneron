import pygame, sys
from settings import *

bg_image = pygame.image.load('assets/img/clouds.png')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/img/Woodcutter.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        pygame.draw.rect(self.image, red, self.rect, 3)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

player = Player()

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('My Game')
        self.clock = pygame.time.Clock()
        self.screen.blit(bg_image, (0, 0))
        self.screen.blit(player.image, player.rect)


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                dt = self.clock.tick(FPS)
                pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
