import pygame, sys
from settings import *
from Player import *
from Enemy import *



class Game:
    def __init__(self):
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

        my_font = pygame.font.SysFont('Comic Sans MS', 40)

        # Points
        points_display = my_font.render('Points: 40', False, (0, 0, 0))
        self.screen.blit(points_display, (WIDTH - 180,20))

        # Health
        health_display = my_font.render('Health: 100', False, (0, 0, 0))
        self.screen.blit(health_display, (WIDTH - 180,50))

        pygame.display.update()


    def run(self):
        pygame.mixer.music.load('assets/audio/music.mp3')
        pygame.mixer.music.play(-1)
        pygame.font.init() # you have to call this at the start, 
                           # if you want to use this module.

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            player.loop(FPS)
            handle_move(player)
    
            self.draw()
            dt = self.clock.tick(FPS)

def handle_move(player):
    keys = pygame.key.get_pressed()
    player.x_vel = 0

    if keys[pygame.K_SPACE]:
        # player.move_left(5)
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('assets/audio/gunloop.wav'))
        game.draw()
        print('shoot')

    if keys[pygame.K_a]:
        player.move_left(5)
        game.draw()
        print('a')

    if keys[pygame.K_d]:
        player.move_right(5)
        game.draw()
        print('d')

    if keys[pygame.K_w]:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/audio/jump.wav'))
        player.move_up(5)
        game.draw()
        print('w')

    if keys[pygame.K_s]:
        player.move_down(5)
        game.draw()
        print('s')


if __name__ == '__main__':

    pygame.init()
    # set main game window size
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    # get background image
    bg_image = pygame.transform.scale(pygame.image.load('assets/img/level1.png'), (WIDTH, HEIGHT)).convert_alpha()
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
