import pygame
import os
import sys


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
#  Данный класс отвечает за фоновое изображение
class fonoviy_sloy():
    def __init__(self, puth_to_file):
        self.image = load_image(puth_to_file)
        fons.append(self)

    def zapusk(self):
        screen.blit(pygame.transform.scale(self.image, (width, height)), [0, 0])


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
    AnimatedSprite(pygame.transform.scale(load_image('Personazh2.png'), (shirina * 4, visota)), 4, 1, cord_x_2, cord_y_2)
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
    # 
    # Ксения:
    # Здесь должна происходить загрузка уровня
    # 
    # 
    pass


# Сделано Ксенией
# Данная функция загружает второй уровень игры
def uroven_2(personazh, ima):
    # 
    # Ксения:
    # Здесь должна происходить загрузка уровня
    # 
    # 
    pass


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
    # 
    # Ксения:
    # Доделаю после первого готового уровня. Сейчас не на чем тестировать данную функцию
    # 
    # 
    pass


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
# Запуск программы
if __name__ == '__main__':
    pygame.init()

    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()
    objects = []
    fons = []
    texts = []

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
