import pygame, sys
from settings import *
from Player import *

bg_image = pygame.image.load('assets/img/clouds.png')


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
