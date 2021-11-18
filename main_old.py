import pygame
from modes.seka.seka import *

pygame.init()

VIDEO_INFO = pygame.display.Info()
WIDTH = VIDEO_INFO.current_w
HEIGHT = VIDEO_INFO.current_h
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
bg = pygame.image.load("locations//bg.bmp")
left_norm = pygame.image.load("skins//stepan//left_norm.png")
left_run = pygame.image.load("skins//stepan//left_run.png")
right_norm = pygame.image.load("skins//stepan//right_norm.png")
right_run = pygame.image.load("skins//stepan//right_run.png")
up_1 = pygame.image.load("skins//stepan//up_1.png")
up_2 = pygame.image.load("skins//stepan//up_2.png")
down_1 = pygame.image.load("skins//stepan//down_1.png")
down_2 = pygame.image.load("skins//stepan//down_2.png")
bg_x = 0
bg_y = 0
mode = 'standart'
seka_mode_bg = False


class Player(pygame.sprite.Sprite):
    SPEED = 10
    X = WIDTH / 2
    Y = HEIGHT / 2
    x = X
    y = Y

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = left_norm
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update_horizontal(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 25:
            self.x -= self.SPEED
            self.rect.center = (self.x, self.y)
        elif keys[pygame.K_RIGHT] and self.x < WIDTH - 25:
            self.x += self.SPEED
            self.rect.center = (self.x, self.y)

    def update_vertical(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > 35:
            self.y -= self.SPEED
            self.rect.center = (self.x, self.y)
        elif keys[pygame.K_DOWN] and self.y < HEIGHT - 35:
            self.y += self.SPEED
            self.rect.center = (self.x, self.y)

    def update_anim(self, anim_coefficient):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if anim_coefficient == 20:
                self.image = left_run
                self.rect = self.image.get_rect(center=(self.x, self.y))
            elif anim_coefficient == 10:
                self.image = left_norm
                self.rect = self.image.get_rect(center=(self.x, self.y))
        elif keys[pygame.K_RIGHT]:
            if anim_coefficient == 20:
                self.image = right_run
                self.rect = self.image.get_rect(center=(self.x, self.y))
            elif anim_coefficient == 10:
                self.image = right_norm
                self.rect = self.image.get_rect(center=(self.x, self.y))
        if keys[pygame.K_UP]:
            if anim_coefficient == 20:
                self.image = up_1
                self.rect = self.image.get_rect(center=(self.x, self.y))
            elif anim_coefficient == 10:
                self.image = up_2
                self.rect = self.image.get_rect(center=(self.x, self.y))
        if keys[pygame.K_DOWN]:
            if anim_coefficient == 20:
                self.image = down_1
                self.rect = self.image.get_rect(center=(self.x, self.y))
            elif anim_coefficient == 10:
                self.image = down_2
                self.rect = self.image.get_rect(center=(self.x, self.y))


def default_mode():
    global mode, running, anim_coefficient
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    player.update_anim(anim_coefficient)
    if anim_coefficient == 20:
        anim_coefficient = 0
    else:
        anim_coefficient += 1

    screen.blit(bg, bg_update())
    all_sprites.draw(screen)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_F4]:
        mode = 'seka'


def seka_mode():
    global mode
    bg = pygame.image.load('seka//images//bg_seka.png')
    if seka_mode_bg:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_F3]:
            game = Game()
            game.create_player(1)
            game.distribution()
            game.checks()
            card1 = pygame.image.load(
                'seka//images//' + game.players[0]['cards'][0] + '.png'
            )
            card2 = pygame.image.load(
                'seka//images//' + game.players[0]['cards'][1] + '.png'
            )
            card3 = pygame.image.load(
                'seka//images//' + game.players[0]['cards'][3] + '.png'
            )
            screen.blit(card1, (HEIGHT - 200, 125 + 300))
    else:
        screen.blit(bg, (0, 0))


def bg_update():
    global bg_x, bg_y
    keys = pygame.key.get_pressed()
    if (
        keys[pygame.K_LEFT]) and (
        bg_x < 0) and (
        player.x == player.X
    ):

        bg_x += player.SPEED
    elif (
        keys[pygame.K_RIGHT]) and (
        bg_x > -5120 + WIDTH + 25) and (
        player.x == player.X
    ):
        bg_x -= player.SPEED
    else:
        player.update_horizontal()
    if (
        keys[pygame.K_UP]) and (
        bg_y < 0) and (
        player.y == player.Y
    ):
        bg_y += player.SPEED
    elif (
        keys[pygame.K_DOWN]) and (
        bg_y > -2880 + HEIGHT + 25) and (
        player.y == player.Y
    ):
        bg_y -= player.SPEED
    else:
        player.update_vertical()
    return (bg_x, bg_y)


screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("TEST")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

anim_coefficient = 0
running = True
while running:
    clock.tick(FPS)
    if mode in 'standart':
        seka_mode_bg = False
        default_mode()
    elif mode in 'seka':
        seka_mode_bg = True
        seka_mode()

    pygame.display.flip()

pygame.quit()
