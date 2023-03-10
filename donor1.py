import pygame
import sys


def load_image(name):
    image = pygame.image.load(f"{'sprits'}/{name}")
    return image


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect()
        self.rect.x = tile_width * pos_x
        self.rect.y = 0
        self.rect.bottom = height

    def update(self):
        self.rect = self.rect.move(2, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.pos = (pos_x, pos_y)

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(
            tile_width * self.pos[0] + 15, tile_height * self.pos[1] + 5)


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = []

    fon = pygame.transform.scale(load_image('fon.jpg'), (wight, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: list(x.ljust(max_width, '.')), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '!':
                Tile('empty', x, y)
            elif level[y][x] == '_':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
                level[y][x] = '_'
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


def mover(hero, movement):
    x, y = hero.pos
    if movement == "up":
        if y > 0 and level_map[y - 1][x] == "_":
            hero.move(x, y - 1)
    elif movement == "down":
        if y < max_y - 1 and level_map[y + 1][x] == "_":
            hero.move(x, y + 1)
    elif movement == "left":
        if x > 0 and level_map[y][x - 1] == "_":
            hero.move(x - 1, y)
    elif movement == "right":
        if x < max_x - 1 and level_map[y][x + 1] == "_":
            hero.move(x + 1, y)


pygame.init()
size = wight, height = 2000, 500
screen = pygame.display.set_mode(size)
FPS = 50

player = None
running = True
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

tile_images = {
    'wall': load_image('house1_ru.png'),
    'empty': load_image('pvo_ua.png')
}
player_image = load_image('bomb.png')

tile_width = 300
tile_height = 50


start_screen()
#level_map = load_level("level_1.txt")
#hero, max_x, max_y = generate_level(level_map)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                mover(hero, "up")
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                mover(hero, "down")
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                mover(hero, "left")
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                mover(hero, "right")
    level_map = load_level("level_1.txt")
    hero, max_x, max_y = generate_level(level_map)
    screen.fill('black')
    all_sprites.draw(screen)
    player_group.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()


pygame.quit()