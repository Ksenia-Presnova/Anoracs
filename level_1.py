import os
import sys

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def draw(screen):
    global running
    im = pygame.transform.scale(pygame.image.load("victory_screen.png"), (1060, 800))
    screen.blit(im, (0, 0))


class Main_Hero(pygame.sprite.Sprite):
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    image = pygame.image.load("Hero_p1.png").convert_alpha()
    image1 = pygame.transform.scale(image, (202, 202))

    def __init__(self, *group):
        super().__init__(all_sprites)
        self.image_p2 = pygame.transform.scale(pygame.image.load("Hero_p2.png"), (202, 202))
        self.image_p1 = pygame.transform.scale(pygame.image.load("Hero_p1.png"), (202, 202))
        self.image_p2_2 = pygame.transform.scale(pygame.image.load("Hero_p2_2.png"), (202, 202))
        self.image_p1_2 = pygame.transform.scale(pygame.image.load("Hero_p1_2.png"), (202, 202))
        self.image = Main_Hero.image1
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 413
        self.y = self.rect.y
        self.size = [202, 202]
        self.step = 15

    def check_win(self):
        if self.rect.x >= 800 and self.rect.y == 413:
            return True
        return False

    def check(self):
        if (self.rect.x <= 180 and self.rect.y < 413) or (790 <= self.rect.x <= 1060 and self.rect.y < 413):
            self.rect.y = 413
        elif 175 < self.rect.x < 790 and self.rect.y < 500:
            self.rect.y = 500

    def update(self, *args, **kwargs):
        print(self.rect.x, self.rect.y)
        if args and args[1][1] and self.rect.x + self.step < width - 100:
            self.rect = self.rect.move(self.step, 0)
            if self.image == self.image_p2:
                self.image = self.image_p1
            else:
                self.image = self.image_p2
            self.check()
        elif args and args[1][0] and self.rect.x - self.step + 90 > 0:
            self.rect = self.rect.move(-self.step, 0)
            if self.image == self.image_p2_2:
                self.image = self.image_p1_2
            else:
                self.image = self.image_p2_2
            self.check()
        elif args and args[1][2]:
            self.rect = self.rect.move(0, -self.step * 8)
        if pygame.sprite.spritecollideany(self, mobs) and self.rect.y == 500:
            self.rect.x = 0
            self.rect.y = self.y
            Slime1.rect.x = 1500
        if self.check_win():
            screen.fill(pygame.Color('black'))
            draw(screen)


class Slime(pygame.sprite.Sprite):
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    image = pygame.image.load("Slime.png").convert_alpha()
    image1 = pygame.transform.scale(image, (100, 100))

    def __init__(self, *group):
        super().__init__(all_sprites)
        self.add(mobs)
        self.size = [100, 100]
        self.image = Slime1.image1
        self.rect = self.image.get_rect()
        self.start_x = 2000
        self.rect.x = self.start_x
        self.rect.y = 604
        self.border = 265
        self.step = 0

    def update(self, *args, **kwargs):
        if self.rect.x - 10 <= 0:
            self.rect.x = self.start_x
        else:
            self.rect = self.rect.move(-self.step, 0)


if __name__ == '__main__':
    pygame.init()

    size = width, height = 1060, 800
    screen = pygame.display.set_mode(size)
    mobs = pygame.sprite.Group()

    # Спрайт отвечающий за задний фон(небо)
    all_sprites = pygame.sprite.Group()
    sky = pygame.sprite.Sprite()
    sky.image = load_image("sky.png")
    sky.rect = sky.image.get_rect()
    sky.rect.x = 0
    sky.rect.y = 0
    all_sprites.add(sky)

    # Лес

    forest = pygame.sprite.Sprite()
    forest.image = pygame.transform.scale(pygame.image.load("forest.png"), (916, 687))
    forest.rect = sky.image.get_rect()
    forest.rect.x = 0
    forest.rect.y = 0
    all_sprites.add(forest)

    # Слайм

    Slime1 = Slime
    Slime1.rect = Slime.image.get_rect()
    Slime1.rect.x = 795
    Slime1.rect.y = 604
    Slime1(all_sprites)

    # Блок слева
    grass = pygame.sprite.Sprite()
    grass.image = load_image("grass.png")
    grass.rect = grass.image.get_rect()
    grass.rect.x = 0
    grass.rect.y = 600
    all_sprites.add(grass)

    # Блок справа

    grass = pygame.sprite.Sprite()
    grass.image = load_image("grass.png")
    grass.rect = grass.image.get_rect()
    grass.rect.x = 895
    grass.rect.y = 600
    all_sprites.add(grass)

    # Трава\Земля

    for i in range(4):
        grass = pygame.sprite.Sprite()
        grass.image = load_image("grass.png")
        grass.rect = grass.image.get_rect()
        grass.rect.x = i * 265
        grass.rect.y = 687
        all_sprites.add(grass)

    # Герой

    Hero = Main_Hero
    Hero.rect = Hero.image.get_rect()
    Hero.rect.x = 0
    Hero.rect.y = 500
    Hero(all_sprites)

    running = True
    N = 10
    to_left, to_right, to_up = False, False, False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_left = True
                if event.key == pygame.K_RIGHT:
                    to_right = True
                if event.key == pygame.K_UP:
                    to_up = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    to_left = False
                if event.key == pygame.K_RIGHT:
                    to_right = False
                if event.key == pygame.K_UP:
                    to_up = False
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            all_sprites.update(event, [to_left, to_right, to_up])
            # draw(screen)

        screen.fill(pygame.Color('white'))

        all_sprites.draw(screen)
        all_sprites.update()
        # draw(screen)
        pygame.display.flip()

    pygame.quit()
