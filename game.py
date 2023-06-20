import pygame, sys
from settings import *
from Player import *
from Enemy import *



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('My Game')
        self.clock = pygame.time.Clock()
        self.screen.blit(bg_image, (0, 0))
        self.screen.blit(player.image, player.rect)
        self.screen.blit(enemy.image, enemy.rect)

    def draw(self):
        self.screen.blit(bg_image, (0, 0))
        self.screen.blit(player.image, player.rect)
        self.screen.blit(enemy.image, enemy.rect)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print('space')
                    if event.key == pygame.K_d:
                        player.rect.x += 15
                        self.draw()

                    if event.key == pygame.K_a:
                        player.rect.x -= 15
                        self.draw()


                dt = self.clock.tick(FPS)
                pygame.display.update()


if __name__ == '__main__':
    bg_image = pygame.transform.scale(pygame.image.load('assets/img/level1.png'), (WIDTH, HEIGHT))
    player = Player()
    enemy = Enemy()
    enemies = pygame.sprite.Group()
    enemies.add(enemy)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(enemy)

    game = Game()
    game.run()
