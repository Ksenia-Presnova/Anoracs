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
