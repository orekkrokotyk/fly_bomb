import pygame


def load_image(name):
    fullname = f"{'sprits'}/{name}"
    image = pygame.image.load(fullname)
    return image







pygame.init()

display_width = 1366
display_height = 768

image = load_image('fon.jpg')
screen = pygame.display.set_mode((display_width, display_height))
screen.blit(image, ((display_width * 0.001), (display_height * 0.001)))

#sprits

land_sprites = pygame.sprite.Group()

land1 = pygame.sprite.Sprite()
land2 = pygame.sprite.Sprite()
land3 = pygame.sprite.Sprite()
land4 = pygame.sprite.Sprite()
land5 = pygame.sprite.Sprite()

land1.image = load_image("house1_ru.png")
land2.image = load_image("house2_ru.png")
land3.image = load_image("house3_ru.png")
land4.image = load_image("pvo_ua.png")
land5.image = load_image("wight_hose_ua.png")

land_sprites.add(land1, land2, land3, land4, land5)
print(land_sprites)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #screen.fill('black')
    pygame.display.flip()

pygame.quit()
