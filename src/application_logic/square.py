import os
import pygame

dirname1 = os.path.dirname(__file__)
dirname = dirname1.replace("application_logic","")

class Square(pygame.sprite.Sprite):
    def __init__(self, number, x_coordinate, y_coordinate):
        super().__init__()
        self.number = number
        self.fliped = False

        self.image = pygame.image.load(os.path.join(dirname, "kuvat_peliin", "kuvake.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate

    def flip(self):
        if not self.fliped:
            self.fliped = True
            filename = "kuvake"+str(self.number)+".png"
            self.image = pygame.image.load(os.path.join(dirname,
                                                        "kuvat_peliin", filename))
