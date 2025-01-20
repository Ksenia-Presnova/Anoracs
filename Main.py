import os
import sqlite3 as qt
import sys

import pygame


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
            # ochistka()
            pygame.init()
            size = 1060, 800
            screen = pygame.display.set_mode(size)
            screen.fill(pygame.Color('black'))
            draw(screen)
            # Редактировано Ксенией
            # В функцию необходимо передать имя персонажа, затем время прохождения, выбранный скин (0 или 1), и номер уровня
            pamat('Имя персонажа', 0, 0, 1)


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
            # ochistka()
            pygame.init()
            size = 1060, 800
            screen = pygame.display.set_mode(size)
            screen.fill(pygame.Color('black'))
            draw(screen)
            # Редактировано Ксенией
            # В функцию необходимо передать имя персонажа, затем время прохождения, выбранный скин (0 или 1), и номер уровня
            pamat('Имя персонажа', 0, 0, 2)


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


# Сделано Ксенией
# Данный класс отвечает за анимацию персонажа
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.time = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.time += 1
        if self.time >= 10:
            self.time = 0
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]


# Сделано Ксенией
# Данный класс отвечает за кнопки в приложении
class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.alreadyPressed = True

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        font = pygame.font.SysFont('Arial', 40)
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


# Сделано Ксенией
#  Данный класс отвечает за фоновое изображение`
class fonoviy_sloy():
    def __init__(self, puth_to_file):
        self.image = load_image(puth_to_file)
        fons.append(self)

    def zapusk(self, shirina=0, visota=0):
        if shirina == 0 or visota == 0:
            screen.blit(pygame.transform.scale(self.image, (width, height)), [0, 0])
        else:
            screen.blit(pygame.transform.scale(self.image, (shirina, visota)), [0, 0])


# Сделано Ксенией
# Данный класс отвечает за дополнительный текст в приложении
class svoi_text():
    def __init__(self, stroka, x, y, redaction=False, color=(200, 100, 0)):
        self.stroka = stroka
        self.x = x
        self.y = y
        self.color = color
        self.redaction = redaction
        self.fontObj = pygame.font.Font(None, 32)

        texts.append(self)

    def otrisovka(self):
        textSufaceObj = self.fontObj.render(self.stroka, True, self.color, None)
        screen.blit(textSufaceObj, (self.x, self.y))

    def zamena(self, key):
        if self.redaction:
            if key['key'] == 8 and len(self.stroka) >= 1:
                self.stroka = self.stroka[:-1]
            else:
                self.stroka += key['unicode']


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
def ochistka():
    all_sprites.empty()
    # Спрайты уровень 1
    all_sprites1.empty()
    mobs1.empty()
    # Спрайты уровень 2
    all_sprites2.empty()
    mobs2.empty()
    objects.clear()
    fons.clear()
    texts.clear()


# Сделано Ксенией
# Данная функция загружает все объекты окна с выбором уровня
def vibor_urovna():
    ochistka()
    fonoviy_sloy('Level_window_fon.png')
    shirina = 100
    visota = 100
    Button((width - shirina) / 2 - 150, (height - visota) / 2 - 75, shirina, visota, '1', lambda: vibor_personazha(1))
    Button((width - shirina) / 2, (height - visota) / 2 - 75, shirina, visota, '2', lambda: vibor_personazha(2))
    Button((width - shirina) / 2 + 150, (height - visota) / 2 - 75, shirina, visota, '3', lambda: vibor_personazha(3))
    Button((width - shirina) / 2 - 150, (height - visota) / 2 + 75, shirina, visota, '4', lambda: vibor_personazha(4))
    Button((width - shirina) / 2, (height - visota) / 2 + 75, shirina, visota, '5', lambda: vibor_personazha(5))
    Button((width - shirina) / 2 + 150, (height - visota) / 2 + 75, shirina, visota, '6', lambda: vibor_personazha(6))
    Button(10, 10, 100, 100, '<===', startovoe_okno)


# Сделано Ксенией
# Данная функция загружает все объекты окна с выбором персонажа
def vibor_personazha(x):
    ochistka()
    fonoviy_sloy('Vibor_window_fon.png')
    shirina = 300
    visota = 300
    cord_x_1 = (width - shirina) / 2 - width / 4
    cord_y_1 = (height - visota) / 2 - height / 8
    cord_x_2 = (width - shirina) / 2 + width / 4
    cord_y_2 = (height - visota) / 2 + height / 8
    AnimatedSprite(pygame.transform.scale(load_image('Personazh.png'), (shirina * 4, visota)), 4, 1, cord_x_1, cord_y_1)
    AnimatedSprite(pygame.transform.scale(load_image('Personazh2.png'), (shirina * 4, visota)), 4, 1, cord_x_2,
                   cord_y_2)
    Button(10, 10, 100, 100, '<===', vibor_urovna)

    svoi_text('Просто нажимайте на клавиатуру!!!', 10, height - 90, color=(200, 200, 255))
    stroka = svoi_text('Персонаж', 10, height - 50, redaction=True)

    if x == 1:
        Button(cord_x_1 + shirina / 3.5, cord_y_1 - 50, 150, 50, 'Выбрать', lambda: uroven_1(1, stroka.stroka))
        Button(cord_x_2 + shirina / 3.5, cord_y_2 - 50, 150, 50, 'Выбрать', lambda: uroven_1(2, stroka.stroka))
    elif x == 2:
        Button(cord_x_1 + shirina / 3.5, cord_y_1 - 50, 150, 50, 'Выбрать', lambda: uroven_2(1, stroka.stroka))
        Button(cord_x_2 + shirina / 3.5, cord_y_2 - 50, 150, 50, 'Выбрать', lambda: uroven_2(2, stroka.stroka))
    elif x == 3:
        Button(cord_x_1 + shirina / 3.5, cord_y_1 - 50, 150, 50, 'Выбрать', lambda: uroven_3(1, stroka.stroka))
        Button(cord_x_2 + shirina / 3.5, cord_y_2 - 50, 150, 50, 'Выбрать', lambda: uroven_3(2, stroka.stroka))
    elif x == 4:
        Button(cord_x_1 + shirina / 3.5, cord_y_1 - 50, 150, 50, 'Выбрать', lambda: uroven_4(1, stroka.stroka))
        Button(cord_x_2 + shirina / 3.5, cord_y_2 - 50, 150, 50, 'Выбрать', lambda: uroven_4(2, stroka.stroka))
    elif x == 5:
        Button(cord_x_1 + shirina / 3.5, cord_y_1 - 50, 150, 50, 'Выбрать', lambda: uroven_5(1, stroka.stroka))
        Button(cord_x_2 + shirina / 3.5, cord_y_2 - 50, 150, 50, 'Выбрать', lambda: uroven_5(2, stroka.stroka))
    elif x == 6:
        Button(cord_x_1 + shirina / 3.5, cord_y_1 - 50, 150, 50, 'Выбрать', lambda: uroven_6(1, stroka.stroka))
        Button(cord_x_2 + shirina / 3.5, cord_y_2 - 50, 150, 50, 'Выбрать', lambda: uroven_6(2, stroka.stroka))


# Сделано Ксенией
# Данная функция загружает первый уровень игры
def uroven_1(personazh, ima):
    # Сделано Кириллом
    ochistka()

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
            fon.zapusk(width, height)
        for text in texts:
            text.otrisovka()
        # -------------------
        # draw(screen)
        pygame.display.flip()
    if Hero.check_win(Hero):
        draw(screen)  # Функция отображает конец уровня и выводит экран окончания

    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    vibor_urovna()


# Сделано Ксенией
# Данная функция загружает второй уровень игры
def uroven_2(personazh, ima):
    # Сделано Кириллом
    ochistka()

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

    # Слайм

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

    Hero = Main_Hero2
    Hero.rect = Hero.image.get_rect()
    Hero.rect.x = 0
    Hero.rect.y = 490
    Hero(all_sprites2)

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
            fon.zapusk(width, height)
        for text in texts:
            text.otrisovka()
        # -------------------
        pygame.display.flip()
    if Hero.check_win(Hero):
        draw(screen)  # Функция отображает конец уровня и выводит экран окончания

    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)
    vibor_urovna()


# Сделано Ксенией
# Данная функция загружает третий уровень игры
def uroven_3(personazh, ima):
    #
    # Ксения:
    # Здесь должна происходить загрузка уровня
    #
    #
    pass


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
    ochistka()
    fonoviy_sloy('Spisok_resultatov.png')
    connection = qt.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM history')
    history = cursor.fetchall()

    i = 0
    for el in history:
        if i < 5:
            svoi_text(str(el[1]) + '  ' +
                      'Уровень - ' + str(el[3]) + '  ' +
                      'Время - ' + str(el[2]) + 'с.  ' +
                      'Скин - ' + str(el[4]),
                      150, 150 + i * 50, color=(0, 0, 150))
        i += 1

    connection.close()
    Button(10, 10, 100, 100, '<===', startovoe_okno)


# Сделано Ксенией
# Данная функция загружает окно с результатами пользователя о прохождении уровня, а также сохраняет их в бд
def pamat(ima, vrema, skin, uroven):
    ochistka()
    fonoviy_sloy('Vospominanie.png')
    svoi_text(str(ima), width // 2, height // 2, color=(0, 0, 0))
    svoi_text('Время: ' + str(vrema), width // 2, height // 2 + 40, color=(0, 0, 0))
    connection = qt.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO history (name, time, skin, level) VALUES (?, ?, ?, ?)',
                   (ima, vrema, skin, uroven))
    connection.commit()
    connection.close()


# Сделано Ксенией
# Данная функция закрывает приложение
def vihod():
    pygame.quit()
    sys.exit()


# Сделано Ксенией
# Данная функция загружает все объекты стартового окна
def startovoe_okno():
    ochistka()
    fonoviy_sloy('Start_window_fon.png')
    shirina = 300
    visota = 100
    Button((width - shirina) / 2, (height - visota) / 2 - 150, shirina, visota, 'Выбрать уровень', vibor_urovna)
    Button((width - shirina) / 2, (height - visota) / 2, shirina, visota, 'Статистика', statistika)
    Button((width - shirina) / 2, (height - visota) / 2 + 150, shirina, visota, 'Выйти из игры', vihod)


# Сделано Ксенией
# Данная функция создает бд в случае ее отсутствия
def sozdanie_bd():
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
    connection.commit()
    connection.close()


# Сделано Ксенией
# Запуск программы
if __name__ == '__main__':
    sozdanie_bd()
    pygame.init()

    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()
    objects = []
    fons = []
    texts = []

    all_sprites1 = pygame.sprite.Group()
    mobs1 = pygame.sprite.Group()

    all_sprites2 = pygame.sprite.Group()
    mobs2 = pygame.sprite.Group()

    startovoe_okno()

    running = True

    # Сделано Ксенией
    # Ядро программы
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # При изменении логики игры, основные изменения необходимо проводить тут!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Лучше не изменять здесь ничего, а только добавлять, иначе можно случайно все сломать!!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    while running:
        pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                for text in texts:
                    text.zamena(event.dict)
        screen.fill(pygame.Color('white'))
        for fon in fons:
            fon.zapusk()
        all_sprites.draw(screen)
        all_sprites.update()
        for object in objects:
            object.process()
        for text in texts:
            text.otrisovka()
        pygame.display.flip()
    pygame.quit()
