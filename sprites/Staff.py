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
