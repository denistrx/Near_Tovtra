import pygame
import pickle
import os

from sys import platform

from modes.default import main as default

pygame.init()

VIDEO_INFO = pygame.display.Info()
WIDTH = VIDEO_INFO.current_w
HEIGHT = VIDEO_INFO.current_h
FPS = 60
MODE = 'menu'

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Orest History")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

menu_image = pygame.image.load('menu//images//bg.png')
menu_image = pygame.transform.scale(menu_image, (WIDTH, HEIGHT))
new_image = pygame.image.load('menu//images//new.png')
new_active_image = pygame.image.load('menu//images//new_active.png')
exit_image = pygame.image.load('menu//images//exit.png')
exit_active_image = pygame.image.load('menu//images//exit_active.png')
continue_image = pygame.image.load('menu//images//continue.png')
continue_active_image = pygame.image.load('menu//images//continue_active.png')
sound = pygame.mixer.Sound('menu//sounds/menu.ogg')

screen.blit(menu_image, (0, 0))
screen.blit(new_image, (WIDTH / 2 - 265 / 2, HEIGHT / 4))
screen.blit(continue_image, (WIDTH / 2 - 265 / 2, HEIGHT / 3))
screen.blit(exit_image, (WIDTH / 2 - 265 / 2, HEIGHT / 1.5))


def continue_button():
    global player, MODE
    if platform in 'win32':
        f = open(
            'C:\\users\\' + os.getlogin() + '\\player.nt', 'rb')
    elif platform in 'linux':
        f = open(
            '//home//' + os.getlogin() + '//.player.nt', 'rb')
    data = pickle.load(f)
    player = default.Player(
        data['NAME'],
        data['SPEED'],
        data['x'],
        data['y'],
        data['bg_x'],
        data['bg_y'],
        data['skin_name'],
        data['location_name'],
        data['anim_direction'],
        data['inventory_max_len'],
        data['inventory']
    )
    f.close()
    all_sprites.add(player)
    MODE = 'default'


def new_button():
    if platform in 'win32':
        f = open(
            'C:\\users\\' + os.getlogin() + '\\player.nt', 'wb')
    elif platform in 'linux':
        f = open(
            '//home//' + os.getlogin() + '//.player.nt', 'wb')
    pickle.dump(default.Player.new_save(), f)
    f.close()
    continue_button()


def save():
    if platform in 'win32':
        f = open(
            'C:\\users\\' + os.getlogin() + '\\player.nt', 'wb')
    elif platform in 'linux':
        f = open(
            '//home//' + os.getlogin() + '//.player.nt', 'wb')
    pickle.dump(player.save(), f)
    f.close()


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if MODE in 'menu':
        screen.blit(menu_image, (0, 0))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (
            WIDTH / 3 < mouse[0] < WIDTH / 3 + 265) and (
            HEIGHT / 4 < mouse[1] < HEIGHT / 4 + 76
        ):
            screen.blit(new_image, (WIDTH / 2 - 265 / 2, HEIGHT / 4))
            if click[0]:
                sound.play()
                new_button()
        else:
            screen.blit(new_active_image, (WIDTH / 2 - 265 / 2, HEIGHT / 4))
        if (platform in 'win32' and os.path.isfile(
            'C:\\users\\' + os.getlogin() + '\\player.nt')) or (
            platform in 'linux' and os.path.isfile(
                '//home//' + os.getlogin() + '//.player.nt')
        ):
            if (
                WIDTH / 3 < mouse[0] < WIDTH / 3 + 265) and (
                HEIGHT / 3 < mouse[1] < HEIGHT / 3 + 76
            ):
                screen.blit(
                    continue_image,
                    (WIDTH / 2 - 265 / 2, HEIGHT / 3)
                )
                if click[0]:
                    sound.play()
                    continue_button()
            else:
                screen.blit(
                    continue_active_image,
                    (WIDTH / 2 - 265 / 2, HEIGHT / 3)
                )
        if (
            WIDTH / 3 < mouse[0] < WIDTH / 3 + 265) and (
            HEIGHT / 1.5 < mouse[1] < HEIGHT / 1.5 + 170
        ):
            screen.blit(exit_image, (WIDTH / 2 - 265 / 2, HEIGHT / 1.5))
            if click[0]:
                sound.play()
                running = False
        else:
            screen.blit(exit_active_image, (WIDTH / 2 - 265 / 2, HEIGHT / 1.5))
    if MODE in 'default':
        if keys[pygame.K_ESCAPE]:
            sound.play()
            save()
            player.exit()
            MODE = 'menu'
        screen.blit(player.bg, (player.bg_x, player.bg_y))
        all_sprites.update()
        all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
