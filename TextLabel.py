import pygame


# Сделано Ксенией
# Данный класс отвечает за дополнительный текст в приложении
class TextLabel():
    def __init__(self, stroka, x, y, massiv, screen, redaction=False, color=(200, 100, 0)):
        self.stroka = stroka
        self.x = x
        self.y = y
        self.color = color
        self.redaction = redaction
        self.fontObj = pygame.font.Font(None, 32)
        self.screen = screen

        massiv.append(self)

    def update(self):
        textSufaceObj = self.fontObj.render(self.stroka, True, self.color, None)
        self.screen.blit(textSufaceObj, (self.x, self.y))

    def TextRedaction(self, key):
        if self.redaction:
            if key['key'] == 8 and len(self.stroka) >= 1:
                self.stroka = self.stroka[:-1]
            else:
                self.stroka += key['unicode']