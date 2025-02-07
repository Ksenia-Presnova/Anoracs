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