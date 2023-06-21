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
        # self.screen.blit(player.image, player.rect)
        # player.draw(self.screen)
        # self.screen.blit(enemy.image, enemy.rect)

    def draw(self):
        self.screen.blit(bg_image, (0, 0))
        # self.screen.blit(player.image, player.rect)
        # self.screen.blit(enemy.image, enemy.rect)
        player.draw(self.screen)
        pygame.display.update()


    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            player.loop(FPS)
            handle_move(player)
    
                # if event.type == pygame.KEYDOWN:
                    # if event.key == pygame.K_SPACE:
                        # print('space')
                    # if event.key == pygame.K_d:
                        # player.rect.x += 15
                        # player.draw(self.screen)
                        # self.draw()

                    # if event.key == pygame.K_a:
                        # player.rect.x -= 15
                        # player.draw(self.screen)
                        # self.draw()


            self.draw()

            dt = self.clock.tick(FPS)
            pygame.display.update()

def handle_move(player):
    keys = pygame.key.get_pressed()
    player.x_vel = 0

    if keys[pygame.K_a]:
        player.move_left(5)
        game.draw()
        print('a')

    if keys[pygame.K_d]:
        player.move_right(5)
        game.draw()
        print('d')



if __name__ == '__main__':

    # set main game window size
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    # get background image
    bg_image = pygame.transform.scale(pygame.image.load('assets/img/level1.png'), (WIDTH, HEIGHT))
    # create player
    player = Player(0, 400, 100, 100, 5)

    # enemy = Enemy()
    # enemies = pygame.sprite.Group()
    # enemies.add(enemy)
    # all_sprites = pygame.sprite.Group()
    # all_sprites.add(player)
    # all_sprites.add(enemy)

    game = Game()
    game.run()
