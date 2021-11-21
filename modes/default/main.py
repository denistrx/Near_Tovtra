import pygame

pygame.init()

VIDEO_INFO = pygame.display.Info()
WIDTH = VIDEO_INFO.current_w
HEIGHT = VIDEO_INFO.current_h

EXISTS = False


class Player(pygame.sprite.Sprite):
    NAME = None
    SPEED = 5
    X = WIDTH / 2
    Y = HEIGHT / 2
    x = X
    y = Y
    bg_x = 0
    bg_y = 0
    anim_coefficient = 0
    anim_direction = {
        'left': True,
        'right': True,
        'up': True,
        'down': True
    }
    skin_name = 'stepan'
    location_name = 'galya'
    bg = pygame.image.load(
        'modes//default//locations//' + location_name + '.bmp')
    skin = {
        'left_norm': pygame.image.load(
            'modes//default//skins//' + skin_name + '//left_norm.png'),
        'left_run': pygame.image.load(
            'modes//default//skins//' + skin_name + '//left_run.png'),
        'right_norm': pygame.image.load(
            'modes//default//skins//' + skin_name + '//right_norm.png'),
        'right_run': pygame.image.load(
            'modes//default//skins//' + skin_name + '//right_run.png'),
        'up_1': pygame.image.load(
            'modes//default//skins//' + skin_name + '//up_1.png'),
        'up_2': pygame.image.load(
            'modes//default//skins//' + skin_name + '//up_2.png'),
        'down_1': pygame.image.load(
            'modes//default//skins//' + skin_name + '//down_1.png'),
        'down_2': pygame.image.load(
            'modes//default//skins//' + skin_name + '//down_2.png')
    }
    inventory_max_len = 5
    inventory = []

    def __init__(
        self, NAME, SPEED, x, y, bg_x, bg_y,
        skin_name, location_name, anim_direction,
        inventory_max_len, inventory
    ):
        self.anim_coefficient = 0
        self.NAME = NAME
        self.SPEED = SPEED
        self.x = x
        self.y = y
        self.bg_x = bg_x
        self.bg_y = bg_y
        self.skin_name = skin_name
        self.location_name = location_name
        self.anim_direction = anim_direction
        self.inventory_max_len = inventory_max_len
        self.inventory = inventory
        pygame.sprite.Sprite.__init__(self)
        if self.anim_direction['left']:
            self.image = self.skin['left_norm']
        elif self.anim_direction['right']:
            self.image = self.skin['right_norm']
        elif self.anim_direction['up']:
            self.image = self.skin['up_1']
        elif self.anim_direction['down']:
            self.image = self.skin['down_1']
        else:
            self.image = self.skin['left_norm']
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

    def update_anim(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT]) or (
            keys[pygame.K_RIGHT]) or (
            keys[pygame.K_UP]) or (
            keys[pygame.K_DOWN]
        ):
            if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                self.anim_direction['down'] = False
                self.anim_direction['up'] = True
                self.anim_direction['left'] = False
                self.anim_direction['right'] = False
                if self.anim_coefficient == 20:
                    self.anim_coefficient = 0
                    self.image = self.skin['up_1']
                    self.rect = self.image.get_rect(center=(self.x, self.y))
                elif self.anim_coefficient == 10:
                    self.image = self.skin['up_2']
                    self.rect = self.image.get_rect(center=(self.x, self.y))
            elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
                self.anim_direction['down'] = True
                self.anim_direction['up'] = False
                self.anim_direction['left'] = False
                self.anim_direction['right'] = False
                if self.anim_coefficient == 20:
                    self.anim_coefficient = 0
                    self.image = self.skin['down_1']
                    self.rect = self.image.get_rect(center=(self.x, self.y))
                elif self.anim_coefficient == 10:
                    self.image = self.skin['down_2']
                    self.rect = self.image.get_rect(center=(self.x, self.y))
            elif (
                keys[pygame.K_LEFT]) and (
                not keys[pygame.K_RIGHT]) and (
                not keys[pygame.K_UP]) and (
                not keys[pygame.K_DOWN]
            ):
                self.anim_direction['left'] = True
                self.anim_direction['right'] = False
                if self.anim_coefficient == 20:
                    self.anim_coefficient = 0
                    self.image = self.skin['left_run']
                    self.rect = self.image.get_rect(center=(self.x, self.y))
                elif self.anim_coefficient == 10:
                    self.image = self.skin['left_norm']
                    self.rect = self.image.get_rect(center=(self.x, self.y))
            elif (
                keys[pygame.K_RIGHT]) and (
                not keys[pygame.K_LEFT]) and (
                not keys[pygame.K_UP]) and (
                not keys[pygame.K_DOWN]
            ):
                self.anim_direction['left'] = False
                self.anim_direction['right'] = True
                if self.anim_coefficient == 20:
                    self.anim_coefficient = 0
                    self.image = self.skin['right_run']
                    self.rect = self.image.get_rect(center=(self.x, self.y))
                elif self.anim_coefficient == 10:
                    self.image = self.skin['right_norm']
                    self.rect = self.image.get_rect(center=(self.x, self.y))
        else:
            self.anim_coefficient = 0
            if self.anim_direction['left']:
                self.image = self.skin['left_norm']
                self.rect = self.image.get_rect(center=(self.x, self.y))
            elif self.anim_direction['right']:
                self.image = self.skin['right_norm']
                self.rect = self.image.get_rect(center=(self.x, self.y))
            elif self.anim_direction['up']:
                self.image = self.skin['up_1']
                self.rect = self.image.get_rect(center=(self.x, self.y))
            elif self.anim_direction['down']:
                self.image = self.skin['down_1']
                self.rect = self.image.get_rect(center=(self.x, self.y))
        self.anim_coefficient += 1

    def update(self):
        keys = pygame.key.get_pressed()
        if (
            keys[pygame.K_LEFT]) and (
            self.bg_x < 0) and (
            self.x == self.X
        ):
            self.bg_x += self.SPEED
        elif (
            keys[pygame.K_RIGHT]) and (
            self.bg_x > -5120 + WIDTH + 25) and (
            self.x == self.X
        ):
            self.bg_x -= self.SPEED
        else:
            self.update_horizontal()
        if (
            keys[pygame.K_UP]) and (
            self.bg_y < 0) and (
            self.y == self.Y
        ):
            self.bg_y += self.SPEED
        elif (
            keys[pygame.K_DOWN]) and (
            self.bg_y > -2880 + HEIGHT + 25) and (
            self.y == self.Y
        ):
            self.bg_y -= self.SPEED

        else:
            self.update_vertical()
        self.update_anim()

    def new_save():
        data = {
            'NAME': None,
            'SPEED': 5,
            'x': WIDTH / 2,
            'y': HEIGHT / 2,
            'bg_x': 0,
            'bg_y': 0,
            'skin_name': 'stepan',
            'location_name': 'galya',
            'anim_direction': {
                'left': False,
                'right': False,
                'up': False,
                'down': False
            },
            'inventory_max_len': 5,
            'inventory': []
        }
        return data

    def save(self):
        data = {
            'NAME': self.NAME,
            'SPEED': self.SPEED,
            'x': self.x,
            'y': self.y,
            'bg_x': self.bg_x,
            'bg_y': self.bg_y,
            'skin_name': self.skin_name,
            'location_name': self.location_name,
            'anim_direction': self.anim_direction,
            'inventory_max_len': self.inventory_max_len,
            'inventory': self.inventory
        }
        return data

    def exit(self):
        self.kill()
        print(123)