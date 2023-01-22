import random

import pygame
from random import choice


def load_image(name):
    fullname = f"{'sprits'}/{name}"
    image = pygame.image.load(fullname)
    return image


class Bomb(pygame.sprite.Sprite):
    bomb = load_image('bomb.png')

    def __init__(self):
        super().__init__(bomb_sprites, all_sprites)
        self.image = Bomb.bomb
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = display_width * 0.15
        self.rect.y = display_height * 0.40

    def update(self):
        self.rect = self.rect.move(0, 2)


class Bomber(pygame.sprite.Sprite):
    image = load_image('bomber.png')

    def __init__(self):
        super().__init__(bomb_sprites, all_sprites)
        self.image = Bomber.image
        self.rect = self.image.get_rect()
        self.rect.x = display_width * 0.1
        self.rect.y = display_height * 0.33


class House(pygame.sprite.Sprite):

    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(land_sprites, all_sprites)
        self.image = tile_images[tile_type]
        self.house_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = tile_width * pos_x
        self.rect.y = 0
        self.rect.bottom = display_height

    def update(self):
        #if not pygame.sprite.collide_mask(self, bimba):
        self.rect = self.rect.move(-3, 0)




class Pvo(pygame.sprite.Sprite):

    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(land_sprites, all_sprites)
        self.image = tile_images[tile_type]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = tile_width * pos_x
        self.rect.y = 0
        self.rect.bottom = display_height

    def update(self):
        self.rect = self.rect.move(-3, 0)


def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))

    return list(map(lambda x: list(x.ljust(max_width, '.')), level_map))


def generate_level(level):
    wall = ['wall1', 'wall2', 'wall3']
    print(random.choices(wall)[0])
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '!':
                Pvo('empty', x, y)
            elif level[y][x] == '_':
                House(random.choices(wall)[0], x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


pygame.init()

display_width = 1366
display_height = 768

image = load_image('fon.jpg')
screen = pygame.display.set_mode((display_width, display_height))
# screen.blit(image, ((display_width * 0.001), (display_height * 0.001)))
# screen.fill('black')
tile_images = {
    'wall1': load_image('house1_ru.png'),
    'wall2': load_image('house2_ru.png'),
    'wall3': load_image('house3_ru.png'),
    'empty': load_image('pvo_ua.png')
}

tile_width = 400



# sprits

land_sprites = pygame.sprite.Group()
bomb_sprites = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

#land1 = pygame.sprite.Sprite()
#land2 = pygame.sprite.Sprite()
#land3 = pygame.sprite.Sprite()
#land4 = pygame.sprite.Sprite()
#land5 = pygame.sprite.Sprite()

#land1.image = load_image("house1_ru.png")
#land2.image = load_image("house2_ru.png")
#land3.image = load_image("house3_ru.png")
#land4.image = load_image("pvo_ua.png")
# land5.image = load_image("wight_hose_ua.png")
# bomb1.image = load_image("bomb.png")


#land_sprites.add(land1, land4)
#bimba = Bomb()


clock = pygame.time.Clock()
running = True
Bomber()
level_map = load_level("level_1.txt")
hero, max_x, max_y = generate_level(level_map)
while running:
    bomb_sprites.update()
    land_sprites.update()
    # Bomber()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Bomb()
    screen.blit(image, ((display_width * 0.001), (display_height * 0.001)))
    bomb_sprites.draw(screen)
    land_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
