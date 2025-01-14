class fonoviy_sloy():
    def __init__(self, puth_to_file):
        self.image = load_image(puth_to_file)
        fons.append(self)

    def zapusk(self):
        screen.blit(pygame.transform.scale(self.image, (width, height)), [0, 0])