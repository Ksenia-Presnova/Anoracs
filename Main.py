import os
import sqlite3 as qt
import sys

from AnimatedSprite import AnimatedSprite
from Button import Button
from BackGroundLayer import BackgroundLayer
from TextLabel import TextLabel

import pygame

import Params


def draw(screen):
    im = pygame.transform.scale(pygame.image.load("victory_screen.png"), (1060, 800))
    screen.blit(im, (0, 0))


# Спрайты уровень 1
class Main_Hero(pygame.sprite.Sprite):
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    image = pygame.image.load("Hero_p1.png").convert_alpha()
    image1 = pygame.transform.scale(image, (202, 202))

    def __init__(self, *group):
        super().__init__(group)
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
        if self.rect.x >= 790 and self.rect.y == 413:
            return True
        return False

    def check(self):
        if (self.rect.x <= 180 and self.rect.y < 413) or (790 <= self.rect.x <= 1060 and self.rect.y < 413):
            self.rect.y = 413
        elif 175 < self.rect.x < 790 and self.rect.y < 500:
            self.rect.y = 500

    def update(self, *args, **kwargs):
        # print(args)
        # print(self.rect.x, self.rect.y)
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
        if pygame.sprite.spritecollideany(self, args[2]) and self.rect.y == 500:
            self.rect.x = 0
            self.rect.y = self.y
            args[3].rect.x = 1500
        if self.check_win():
            # GameClear()
            pygame.init()
            size = 1060, 800
            screen = pygame.display.set_mode(size)
            screen.fill(pygame.Color('black'))
            draw(screen)
            # Редактировано Ксенией
            # В функцию необходимо передать имя персонажа, затем время прохождения, выбранный скин (0 или 1), и номер уровня
            LevelResultWindow('Имя персонажа', 0, 0, 1)


class Slime(pygame.sprite.Sprite):
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    image = pygame.image.load("Slime.png").convert_alpha()
    image1 = pygame.transform.scale(image, (100, 100))

    def __init__(self, *group, mobs):
        super().__init__(mobs)
        self.size = [100, 100]
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.start_x = 3000
        self.rect.x = self.start_x
        self.rect.y = 604
        self.border = 265
        self.step = 5

    def update(self, *args, **kwargs):
        # print(self.rect.x)
        if self.rect.x - 10 <= 0:
            self.rect.x = self.start_x
        else:
            self.rect = self.rect.move(-self.step, 0)


# Спрайты уровень 2
class Main_Hero2(pygame.sprite.Sprite):
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    image = pygame.image.load("Hero_p1.png").convert_alpha()
    image1 = pygame.transform.scale(image, (202, 202))

    def __init__(self, *group):
        super().__init__(group[0])
        self.image_p2 = pygame.transform.scale(pygame.image.load("Hero_p2.png"), (202, 202))
        self.image_p1 = pygame.transform.scale(pygame.image.load("Hero_p1.png"), (202, 202))
        self.image_p2_2 = pygame.transform.scale(pygame.image.load("Hero_p2_2.png"), (202, 202))
        self.image_p1_2 = pygame.transform.scale(pygame.image.load("Hero_p1_2.png"), (202, 202))
        self.image = Main_Hero2.image1
        self.start_x = 0
        self.start_y = 490
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 490
        self.y = self.rect.y
        self.size = [202, 202]
        self.step = 15

    def check_win(self):
        if self.rect.x >= 780 and self.rect.y <= 130:
            return True
        return False

    def check(self):
        if self.rect.x <= 180 and self.rect.y < 485:
            self.rect.y = self.start_y
        elif self.rect.x <= 445 and self.rect.y < 360:
            self.rect.y = 360
        elif self.rect.x <= 710 and self.rect.y < 235:
            self.rect.y = 235

    def update(self, *args, **kwargs):
        # print(args)
        # print(self.rect.x, self.rect.y)
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
        if pygame.sprite.spritecollideany(self, args[2]):
            self.rect.x = 0
            self.rect.y = self.y
        if self.check_win():
            # GameClear()
            pygame.init()
            size = 1060, 800
            screen = pygame.display.set_mode(size)
            screen.fill(pygame.Color('black'))
            draw(screen)
            # Редактировано Ксенией
            # В функцию необходимо передать имя персонажа, затем время прохождения, выбранный скин (0 или 1), и номер уровня
            LevelResultWindow('Имя персонажа', 0, 0, 2)


class FireBall(pygame.sprite.Sprite):
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    image = pygame.image.load("FireBall.png").convert_alpha()
    image1 = pygame.transform.scale(image, (100, 100))

    def __init__(self, *group, mobs):
        super().__init__(mobs)
        self.size = [100, 100]
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.start_x = 0
        self.start_y = 0
        self.finish_x = 1060
        self.finish_y = 800
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.border = 0
        self.step = 3

    def update(self, *args, **kwargs):
        # print(self.rect.x)
        k = 1.325
        if self.rect.x + 10 >= self.finish_x or self.rect.y + 10 >= self.finish_y:
            self.rect.x = self.start_x
            self.rect.y = self.start_y
        else:
            self.rect = self.rect.move(self.step * k, self.step)


# Спрайты уровень 3
class Main_Hero3(pygame.sprite.Sprite):
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    image = pygame.image.load("Hero_p1.png").convert_alpha()
    image1 = pygame.transform.scale(image, (202, 202))

    def __init__(self, *group):
        super().__init__(group[0])
        self.staff = False
        self.image_p2 = pygame.transform.scale(pygame.image.load("Hero_p2.png"), (202, 202))
        self.image_p1 = pygame.transform.scale(pygame.image.load("Hero_p1.png"), (202, 202))
        self.image_p2_2 = pygame.transform.scale(pygame.image.load("Hero_p2_2.png"), (202, 202))
        self.image_p1_2 = pygame.transform.scale(pygame.image.load("Hero_p1_2.png"), (202, 202))
        self.image = Main_Hero3.image1
        self.start_x = 0
        self.start_y = 490
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 490
        self.y = self.rect.y
        self.size = [202, 202]
        self.step = 15

    def check(self):
        if pygame.sprite.spritecollideany(self, Staff_U3) or self.staff:
            return True
        return False

    def check_win(self):
        if self.staff and self.rect.x < 200:
            return True
        return False

    def update(self, *args, **kwargs):
        # print(args)
        # print(self.rect.x, self.rect.y)
        self.staff = self.check()
        if args and args[1][1] and self.rect.x + self.step < width - 100:
            self.rect = self.rect.move(self.step, 0)
            if self.image == self.image_p2:
                self.image = self.image_p1
            else:
                self.image = self.image_p2
        elif args and args[1][0] and self.rect.x - self.step + 90 > 0:
            self.rect = self.rect.move(-self.step, 0)
            if self.image == self.image_p2_2:
                self.image = self.image_p1_2
            else:
                self.image = self.image_p2_2
        elif args and args[1][2]:
            self.rect = self.rect.move(0, -self.step * 8)
        if pygame.sprite.spritecollideany(self, args[2]):
            self.rect.x = 0
            self.rect.y = self.y
        if self.check_win():
            # GameClear()
            pygame.init()
            size = 1060, 800
            screen = pygame.display.set_mode(size)
            screen.fill(pygame.Color('black'))
            draw(screen)
            # Редактировано Ксенией
            # В функцию необходимо передать имя персонажа, затем время прохождения, выбранный скин (0 или 1), и номер уровня
            LevelResultWindow('Имя персонажа', 0, 0, 2)


class FireBall2(pygame.sprite.Sprite):
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    image = pygame.image.load("FireBall2.png").convert_alpha()
    image1 = pygame.transform.scale(image, (100, 100 * 2.09))

    def __init__(self, *group, mobs, x):
        super().__init__(mobs)
        self.size = [100, 100]
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.start_x = x
        self.start_y = 0
        self.finish_x = x
        self.finish_y = 800
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.border = 0
        self.step = 0

    def update(self, *args, **kwargs):
        print(self.rect.y)
        if self.rect.y + 10 >= 800:
            self.rect.x = self.start_x
            self.rect.y = self.start_y
        else:
            self.rect = self.rect.move(0, self.step)


class Staff(pygame.sprite.Sprite):
    pygame.init()
    screen = pygame.display.set_mode((100, 100))
    image = pygame.image.load("staff.png").convert_alpha()
    image1 = pygame.transform.scale(image, (100 * 2.43, 100))

    def __init__(self, *group, staff):
        super().__init__(staff)
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.x = 830
        self.rect.y = 465


# Сделано Ксенией
# Данная функция позволяет загружать изображения, которые лежат рядом с проектом
def load_image(name, colorkey=None):
    fullname = os.path.join('', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# Сделано Ксенией
# Данная функция очищает все объекты
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# При добавлении новых типов объектов обязательно необходимо занести их очистку сюда!!! ЭТО ВАЖНО!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def GameClear():
    all_sprites.empty()
    # Спрайты уровень 1
    all_sprites1.empty()
    mobs1.empty()
    # Спрайты уровень 2
    all_sprites2.empty()
    mobs2.empty()
    # Спрайты уровень 3
    all_sprites3.empty()
    mobs3.empty()
    Staff_U3.empty()
    objects.clear()
    fons.clear()
    texts.clear()


# Сделано Ксенией
# Данная функция загружает все объекты окна с выбором уровня
def LevelChoiceWindow():
    GameClear()
    BackgroundLayer(load_image('Level_window_fon.png'), fons, screen)
    Button((width - Params.WIDTH_LEVEL_CHOICE_WINDOW) / 2 - 150, (height - Params.HEIGHT_LEVEL_CHOICE_WINDOW) / 2 - 75,
           Params.WIDTH_LEVEL_CHOICE_WINDOW, Params.HEIGHT_LEVEL_CHOICE_WINDOW, objects, screen, '1', lambda: CharacterChoiceWindow(1))
    Button((width - Params.WIDTH_LEVEL_CHOICE_WINDOW) / 2, (height - Params.HEIGHT_LEVEL_CHOICE_WINDOW) / 2 - 75,
           Params.WIDTH_LEVEL_CHOICE_WINDOW, Params.HEIGHT_LEVEL_CHOICE_WINDOW, objects, screen, '2', lambda: CharacterChoiceWindow(2))
    Button((width - Params.WIDTH_LEVEL_CHOICE_WINDOW) / 2 + 150, (height - Params.HEIGHT_LEVEL_CHOICE_WINDOW) / 2 - 75,
           Params.WIDTH_LEVEL_CHOICE_WINDOW, Params.HEIGHT_LEVEL_CHOICE_WINDOW, objects, screen, '3', lambda: CharacterChoiceWindow(3))
    Button((width - Params.WIDTH_LEVEL_CHOICE_WINDOW) / 2 - 150, (height - Params.HEIGHT_LEVEL_CHOICE_WINDOW) / 2 + 75,
           Params.WIDTH_LEVEL_CHOICE_WINDOW, Params.HEIGHT_LEVEL_CHOICE_WINDOW, objects, screen, '4', lambda: CharacterChoiceWindow(4))
    Button((width - Params.WIDTH_LEVEL_CHOICE_WINDOW) / 2, (height - Params.HEIGHT_LEVEL_CHOICE_WINDOW) / 2 + 75,
           Params.WIDTH_LEVEL_CHOICE_WINDOW, Params.HEIGHT_LEVEL_CHOICE_WINDOW, objects, screen, '5', lambda: CharacterChoiceWindow(5))
    Button((width - Params.WIDTH_LEVEL_CHOICE_WINDOW) / 2 + 150, (height - Params.HEIGHT_LEVEL_CHOICE_WINDOW) / 2 + 75,
           Params.WIDTH_LEVEL_CHOICE_WINDOW, Params.HEIGHT_LEVEL_CHOICE_WINDOW, objects, screen, '6', lambda: CharacterChoiceWindow(6))
    Button(10, 10, 100, 100, objects, screen, '<===', MainWindow)


# Сделано Ксенией
# Данная функция загружает все объекты окна с выбором персонажа
def CharacterChoiceWindow(x):
    GameClear()
    BackgroundLayer(load_image('Vibor_window_fon.png'), fons, screen)
    cord_x_1 = (width - Params.WIDTH_CHARACTER_CHOICE_WINDOW) / 2 - width / 4
    cord_y_1 = (height - Params.HEIGHT_CHARACTER_CHOICE_WINDOW) / 2 - height / 8
    cord_x_2 = (width - Params.WIDTH_CHARACTER_CHOICE_WINDOW) / 2 + width / 4
    cord_y_2 = (height - Params.HEIGHT_CHARACTER_CHOICE_WINDOW) / 2 + height / 8
    AnimatedSprite(pygame.transform.scale(load_image('Personazh.png'),
                                          (Params.WIDTH_CHARACTER_CHOICE_WINDOW * 4,
                                           Params.HEIGHT_CHARACTER_CHOICE_WINDOW)), 4, 1, cord_x_1, cord_y_1, all_sprites)
    AnimatedSprite(pygame.transform.scale(load_image('Personazh2.png'),
                                          (Params.WIDTH_CHARACTER_CHOICE_WINDOW * 4,
                                           Params.HEIGHT_CHARACTER_CHOICE_WINDOW)), 4, 1, cord_x_2,
                   cord_y_2, all_sprites)
    Button(10, 10, 100, 100, objects, screen, '<===', LevelChoiceWindow)

    TextLabel('Просто нажимайте на клавиатуру!!!', 10, height - 90, texts, screen, color=(200, 200, 255))
    stroka = TextLabel('Персонаж', 10, height - 50, texts, screen, redaction=True)

    if x == 1:
        Button(cord_x_1 + Params.WIDTH_CHARACTER_CHOICE_WINDOW / 3.5, cord_y_1 - 50, 150, 50, objects, screen, 'Выбрать', lambda: uroven_1(1, stroka.stroka))
        Button(cord_x_2 + Params.WIDTH_CHARACTER_CHOICE_WINDOW / 3.5, cord_y_2 - 50, 150, 50, objects, screen, 'Выбрать', lambda: uroven_1(2, stroka.stroka))
    elif x == 2:
        Button(cord_x_1 + Params.WIDTH_CHARACTER_CHOICE_WINDOW / 3.5, cord_y_1 - 50, 150, 50, objects, screen, 'Выбрать', lambda: uroven_2(1, stroka.stroka))
        Button(cord_x_2 + Params.WIDTH_CHARACTER_CHOICE_WINDOW / 3.5, cord_y_2 - 50, 150, 50, objects, screen, 'Выбрать', lambda: uroven_2(2, stroka.stroka))
    elif x == 3:
        Button(cord_x_1 + Params.WIDTH_CHARACTER_CHOICE_WINDOW / 3.5, cord_y_1 - 50, 150, 50, objects, screen, 'Выбрать', lambda: uroven_3(1, stroka.stroka))
        Button(cord_x_2 + Params.WIDTH_CHARACTER_CHOICE_WINDOW / 3.5, cord_y_2 - 50, 150, 50, objects, screen, 'Выбрать', lambda: uroven_3(2, stroka.stroka))
    elif x == 4:
        Button(cord_x_1 + Params.WIDTH_CHARACTER_CHOICE_WINDOW / 3.5, cord_y_1 - 50, 150, 50, objects, screen, 'Выбрать', lambda: uroven_4(1, stroka.stroka))
        Button(cord_x_2 + Params.WIDTH_CHARACTER_CHOICE_WINDOW / 3.5, cord_y_2 - 50, 150, 50, objects, screen, 'Выбрать', lambda: uroven_4(2, stroka.stroka))
    elif x == 5:
        Button(cord_x_1 + Params.WIDTH_CHARACTER_CHOICE_WINDOW / 3.5, cord_y_1 - 50, 150, 50, objects, screen, 'Выбрать', lambda: uroven_5(1, stroka.stroka))
        Button(cord_x_2 + Params.WIDTH_CHARACTER_CHOICE_WINDOW / 3.5, cord_y_2 - 50, 150, 50, objects, screen, 'Выбрать', lambda: uroven_5(2, stroka.stroka))
    elif x == 6:
        Button(cord_x_1 + Params.WIDTH_CHARACTER_CHOICE_WINDOW / 3.5, cord_y_1 - 50, 150, 50, objects, screen, 'Выбрать', lambda: uroven_6(1, stroka.stroka))
        Button(cord_x_2 + Params.WIDTH_CHARACTER_CHOICE_WINDOW / 3.5, cord_y_2 - 50, 150, 50, objects, screen, 'Выбрать', lambda: uroven_6(2, stroka.stroka))


# Сделано Ксенией
# Данная функция загружает первый уровень игры
def uroven_1(personazh, ima):
    # Сделано Кириллом
    GameClear()

    pygame.init()

    size = width, height = 1060, 800
    screen = pygame.display.set_mode(size)

    # Спрайт отвечающий за задний фон(небо)
    sky = pygame.sprite.Sprite()
    sky.image = load_image("sky.png")
    sky.rect = sky.image.get_rect()
    sky.rect.x = 0
    sky.rect.y = 0
    all_sprites1.add(sky)

    # Лес

    forest = pygame.sprite.Sprite()
    forest.image = pygame.transform.scale(pygame.image.load("forest.png"), (916, 687))
    forest.rect = sky.image.get_rect()
    forest.rect.x = 0
    forest.rect.y = 0
    all_sprites1.add(forest)

    # Слайм

    Slime1 = Slime
    Slime1.rect = Slime.image.get_rect()
    Slime1.rect.x = 795
    Slime1.rect.y = 604
    Slime1(mobs=mobs1)

    # Блок слева
    grass = pygame.sprite.Sprite()
    grass.image = load_image("grass.png")
    grass.rect = grass.image.get_rect()
    grass.rect.x = 0
    grass.rect.y = 600
    all_sprites1.add(grass)

    # Блок справа

    grass = pygame.sprite.Sprite()
    grass.image = load_image("grass.png")
    grass.rect = grass.image.get_rect()
    grass.rect.x = 895
    grass.rect.y = 600
    all_sprites1.add(grass)

    # Трава\Земля

    for i in range(4):
        grass = pygame.sprite.Sprite()
        grass.image = load_image("grass.png")
        grass.rect = grass.image.get_rect()
        grass.rect.x = i * 265
        grass.rect.y = 687
        all_sprites1.add(grass)

    # Герой

    Hero = Main_Hero
    Hero.rect = Hero.image.get_rect()
    Hero.rect.x = 0
    Hero.rect.y = 500
    Hero(all_sprites1)

    running1 = True
    N = 10
    to_left, to_right, to_up = False, False, False

    while running1:
        for event in pygame.event.get():
            if Hero.check_win(Hero):
                running1 = False
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
                running1 = False
            all_sprites1.update(event, [to_left, to_right, to_up], mobs1, Slime1)
            mobs1.update()
            # draw(screen)
        mobs1.update()
        screen.fill(pygame.Color('white'))

        all_sprites1.draw(screen)
        mobs1.draw(screen)
        # Добавлено Ксенией. Нужно для отображения итогового окна
        for fon in fons:
            fon.update(width, height)
        for text in texts:
            text.update()
        # -------------------
        # draw(screen)
        pygame.display.flip()
    if Hero.check_win(Hero):
        draw(screen)  # Функция отображает конец уровня и выводит экран окончания

    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    LevelChoiceWindow()


# Сделано Ксенией
# Данная функция загружает второй уровень игры
def uroven_2(personazh, ima):
    # Сделано Кириллом
    GameClear()

    pygame.init()

    size = width, height = 1060, 800
    screen = pygame.display.set_mode(size)

    # Небо
    sky = pygame.sprite.Sprite()
    sky.image = load_image("sky.png")
    sky.rect = sky.image.get_rect()
    sky.rect.x = 0
    sky.rect.y = 0
    all_sprites2.add(sky)

    # Лес

    forest = pygame.sprite.Sprite()
    forest.image = pygame.transform.scale(pygame.image.load("forest.png"), (916, 687))
    forest.rect = sky.image.get_rect()
    forest.rect.x = 0
    forest.rect.y = 0
    all_sprites2.add(forest)

    # Фаербол

    FireBall1 = FireBall
    FireBall1.rect = Slime.image.get_rect()
    FireBall1.rect.x = 0
    FireBall1.rect.y = 0
    FireBall1(mobs=mobs2)

    # Трава\Земля
    for j in range(3):
        for i in range(4 - j):
            grass = pygame.sprite.Sprite()
            grass.image = load_image("grass.png")
            grass.rect = grass.image.get_rect()
            grass.rect.x = j * 265 + i * 265
            grass.rect.y = 687 - i * 125
            all_sprites2.add(grass)

    # Герой

    Hero1 = Main_Hero2
    Hero1.rect = Hero1.image.get_rect()
    Hero1.rect.x = 0
    Hero1.rect.y = 490
    Hero1(all_sprites2)

    running1 = True
    N = 10
    to_left, to_right, to_up = False, False, False

    while running1:
        for event in pygame.event.get():
            if Hero1.check_win(Hero1):
                running1 = False
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
                running1 = False
            all_sprites2.update(event, [to_left, to_right, to_up], mobs2)
            mobs2.update()
            # draw(screen)
        mobs2.update()
        screen.fill(pygame.Color('white'))

        all_sprites2.draw(screen)
        mobs2.draw(screen)
        # draw(screen)
        # Добавлено Ксенией. Нужно для отображения итогового окна
        for fon in fons:
            fon.update(width, height)
        for text in texts:
            text.update()
        # -------------------
        pygame.display.flip()
    if Hero1.check_win(Hero1):
        draw(screen)  # Функция отображает конец уровня и выводит экран окончания

    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    LevelChoiceWindow()


# Сделано Ксенией
# Данная функция загружает третий уровень игры
def uroven_3(personazh, ima):
    # Сделано Кириллом
    GameClear()

    pygame.init()

    size = width, height = 1060, 800
    screen = pygame.display.set_mode(size)

    # Небо
    sky = pygame.sprite.Sprite()
    sky.image = load_image("sky.png")
    sky.rect = sky.image.get_rect()
    sky.rect.x = 0
    sky.rect.y = 0
    all_sprites3.add(sky)

    # Лес

    forest = pygame.sprite.Sprite()
    forest.image = pygame.transform.scale(pygame.image.load("forest.png"), (916, 687))
    forest.rect = sky.image.get_rect()
    forest.rect.x = 0
    forest.rect.y = 0
    all_sprites3.add(forest)

    # Фаербол

    FireBall1 = FireBall2
    FireBall1.rect = Slime.image.get_rect()
    FireBall1.rect.x = 360
    FireBall1.rect.y = 0
    FireBall1(mobs=mobs3, x=360)

    # Фаербол

    FireBall21 = FireBall2
    FireBall21.rect = Slime.image.get_rect()
    FireBall21.rect.x = 720
    FireBall21.rect.y = 0
    FireBall21(mobs=mobs3, x=720)

    # Посох(я так и не понял, что это и назвал посохом)

    Staff1 = Staff
    Staff1.rect = Staff.image.get_rect()
    Staff1.rect.y = 465
    Staff1.rect.x = 960
    Staff1(staff=Staff_U3)

    # Трава/Земля

    for i in range(4):
        grass = pygame.sprite.Sprite()
        grass.image = load_image("grass.png")
        grass.rect = grass.image.get_rect()
        grass.rect.x = i * 265
        grass.rect.y = 687
        all_sprites3.add(grass)

    # Герой

    Hero2 = Main_Hero3
    Hero2.rect = Hero2.image.get_rect()
    Hero2.rect.x = 0
    Hero2.rect.y = 465
    Hero2.staff = False
    Hero2(all_sprites3)

    running1 = True
    N = 10
    to_left, to_right, to_up = False, False, False

    while running1:
        for event in pygame.event.get():
            if Hero2.check_win(Hero2):
                running1 = False
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
                running1 = False
            all_sprites3.update(event, [to_left, to_right, to_up], mobs3)
            mobs3.update()
            Staff_U3.update()
            print(Hero2.staff)
            # draw(screen)
        mobs3.update()
        screen.fill(pygame.Color('white'))

        all_sprites3.draw(screen)
        Staff_U3.draw(screen)
        mobs3.draw(screen)
        # draw(screen)
        # Добавлено Ксенией. Нужно для отображения итогового окна
        for fon in fons:
            fon.update(width, height)
        for text in texts:
            text.update()
        # -------------------
        pygame.display.flip()
    if Hero2.check_win(Hero2):
        draw(screen)  # Функция отображает конец уровня и выводит экран окончания

    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    LevelChoiceWindow()


# Сделано Ксенией
# Данная функция загружает четвертый уровень игры
def uroven_4(personazh, ima):
    #
    # Ксения:
    # Здесь должна происходить загрузка уровня
    #
    #
    pass


# Сделано Ксенией
# Данная функция загружает пятый уровень игры
def uroven_5(personazh, ima):
    #
    # Ксения:
    # Здесь должна происходить загрузка уровня
    #
    #
    pass


# Сделано Ксенией
# Данная функция загружает шестой уровень игры
def uroven_6(personazh, ima):
    #
    # Ксения:
    # Здесь должна происходить загрузка уровня
    #
    #
    pass


# Сделано Ксенией
# Данная функция загружает окно статистики из бд
def statistika():
    GameClear()
    BackgroundLayer(load_image('Spisok_resultatov.png'), fons, screen)
    connection = qt.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM history')
    history = cursor.fetchall()

    i = 0
    for el in history:
        if i < 5:
            TextLabel(str(el[1]) + '  ' +
                      'Уровень - ' + str(el[3]) + '  ' +
                      'Время - ' + str(el[2]) + 'с.  ' +
                      'Скин - ' + str(el[4]),
                      150, 150 + i * 50, texts, screen, color=(0, 0, 150))
        i += 1

    connection.close()
    Button(10, 10, 100, 100, objects, screen, '<===', MainWindow)


# Сделано Ксенией
# Данная функция загружает окно с результатами пользователя о прохождении уровня, а также сохраняет их в бд
def LevelResultWindow(ima, vrema, skin, uroven):
    GameClear()
    BackgroundLayer(load_image('Vospominanie.png'), fons, screen)
    TextLabel(str(ima), width // 2, height // 2, texts, screen, color=(0, 0, 0))
    TextLabel('Время: ' + str(vrema), width // 2, height // 2 + 40, texts, screen, color=(0, 0, 0))
    connection = qt.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO history (name, time, skin, level) VALUES (?, ?, ?, ?)',
                   (ima, vrema, skin, uroven))
    connection.commit()
    connection.close()


# Сделано Ксенией
# Данная функция закрывает приложение
def GameCancel():
    pygame.quit()
    sys.exit()


# Сделано Ксенией
# Данная функция загружает все объекты стартового окна
def MainWindow():
    GameClear()
    BackgroundLayer(load_image('Start_window_fon.png'), fons, screen)
    Button((width - Params.WIDHT_MAIN_WINDOW) / 2, (height - Params.HEIGHT_MAIN_WINDOW) / 2 - 150,
           Params.WIDHT_MAIN_WINDOW, Params.HEIGHT_MAIN_WINDOW, objects, screen, 'Выбрать уровень', LevelChoiceWindow)
    Button((width - Params.WIDHT_MAIN_WINDOW) / 2, (height - Params.HEIGHT_MAIN_WINDOW) / 2,
           Params.WIDHT_MAIN_WINDOW, Params.HEIGHT_MAIN_WINDOW, objects, screen, 'Статистика', statistika)
    Button((width - Params.WIDHT_MAIN_WINDOW) / 2, (height - Params.HEIGHT_MAIN_WINDOW) / 2 + 150,
           Params.WIDHT_MAIN_WINDOW, Params.HEIGHT_MAIN_WINDOW, objects, screen, 'Выйти из игры', GameCancel)


# Сделано Ксенией
# Данная функция создает бд в случае ее отсутствия
def BDCreation():
    connection = qt.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY,
        name TEXT,
        time INTEGER,
        skin INTEGER, 
        level INTEGER
        )
        ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS levels (
        id INTEGER PRIMARY KEY,
        name TEXT
        )
        ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS skins (
        id INTEGER PRIMARY KEY,
        name TEXT
        )
        ''')
    connection.commit()
    connection.close()


# Сделано Ксенией
# Запуск программы
if __name__ == '__main__':
    BDCreation()
    pygame.init()

    size = width, height = Params.WIDTH, Params.HEIGHT
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()
    objects = []
    fons = []
    texts = []

    all_sprites1 = pygame.sprite.Group()
    mobs1 = pygame.sprite.Group()

    all_sprites2 = pygame.sprite.Group()
    mobs2 = pygame.sprite.Group()

    all_sprites3 = pygame.sprite.Group()
    mobs3 = pygame.sprite.Group()
    Staff_U3 = pygame.sprite.Group()

    MainWindow()

    running = True

    # Сделано Ксенией
    # Ядро программы
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # При изменении логики игры, основные изменения необходимо проводить тут!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Лучше не изменять здесь ничего, а только добавлять, иначе можно случайно все сломать!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    while running:
        pygame.time.Clock().tick(Params.TICKS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                for text in texts:
                    text.TextRedaction(event.dict)
        screen.fill(pygame.Color('white'))
        for fon in fons:
            fon.update()
        all_sprites.draw(screen)
        all_sprites.update()
        for object in objects:
            object.process()
        for text in texts:
            text.update()
        pygame.display.flip()
    pygame.quit()

