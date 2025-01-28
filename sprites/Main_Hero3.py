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
            # ochistka()
            pygame.init()
            size = 1060, 800
            screen = pygame.display.set_mode(size)
            screen.fill(pygame.Color('black'))
            draw(screen)
            # Редактировано Ксенией
            # В функцию необходимо передать имя персонажа, затем время прохождения, выбранный скин (0 или 1), и номер уровня
            pamat('Имя персонажа', 0, 0, 2)
