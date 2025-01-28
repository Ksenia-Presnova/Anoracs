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
