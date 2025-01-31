import pygame

from Params import WIDTH, HEIGHT


# Сделано Ксенией
#  Данный класс отвечает за фоновое изображение`
class BackgroundLayer():
    def __init__(self, image, massiv, screen):
        self.image = image
        self.screen = screen
        massiv.append(self)

    def update(self, shirina=0, visota=0):
        if shirina == 0 or visota == 0:
            self.screen.blit(pygame.transform.scale(self.image, (WIDTH, HEIGHT)), [0, 0])
        else:
            self.screen.blit(pygame.transform.scale(self.image, (shirina, visota)), [0, 0])