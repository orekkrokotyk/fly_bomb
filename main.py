import pygame
from random import choice


def load_image(name):
    fullname = f"{'sprits'}/{name}"
    image = pygame.image.load(fullname)
    return image



class Mountain(pygame.sprite.Sprite):
    imag = load_image("house2_ru.png")

    def __init__(self):
        super().__init__(land_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        #self.rect.bottom = height


class Bomb(pygame.sprite.Sprite):
    bomb = load_image('bomb.png')

    def __init__(self):
        super().__init__(bomb_sprites)
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
        super().__init__(bomb_sprites)
        self.image = Bomber.image
        self.rect = self.image.get_rect()
        self.rect.x = display_width * 0.1
        self.rect.y = display_height * 0.33






pygame.init()

display_width = 1366
display_height = 768

image = load_image('fon.jpg')
screen = pygame.display.set_mode((display_width, display_height))
screen.blit(image, ((display_width * 0.001), (display_height * 0.001)))
#screen.fill('black')

#sprits

land_sprites = pygame.sprite.Group()
bomb_sprites = pygame.sprite.Group()

land1 = pygame.sprite.Sprite()
land2 = pygame.sprite.Sprite()
land3 = pygame.sprite.Sprite()
land4 = pygame.sprite.Sprite()
land5 = pygame.sprite.Sprite()

land1.image = load_image("house1_ru.png")
land2.image = load_image("house2_ru.png")
land3.image = load_image("house3_ru.png")
land4.image = load_image("pvo_ua.png")
#land5.image = load_image("wight_hose_ua.png")
#bomb1.image = load_image("bomb.png")


land_sprites.add(land1, land2, land3, land4)
print(land_sprites)


pos = [display_width * 0.1, display_height * 0.33]


clock = pygame.time.Clock()
running = True
#Bomber()
while running:
    bomb_sprites.update()
    #Bomber()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Bomb()

    screen.blit(image, ((display_width * 0.001), (display_height * 0.001)))
    bomb_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
