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
