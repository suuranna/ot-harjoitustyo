import os
import pygame

dirname = os.path.dirname("/home/suuranna/Ohjelmistotekniikka_jutut/ot-harjoitustyo")

class Square(pygame.sprite.Sprite):
    def __init__(self, number, x_coordinate, y_coordinate):
        super().__init__()
        self.number = number
        self.fliped = False

        self.image = pygame.image.load(os.path.join(dirname, "ot-harjoitustyo",
                                                    "kuvake.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate

    def flip(self):
        if not self.fliped:
            print("Klikattu ruutua sijainnissa", self.rect.x, self.rect.y,
                  " ja jonka numero on ", self.number)
            self.fliped = True
            filename = "kuvake"+str(self.number)+".png"
            self.image = pygame.image.load(os.path.join(dirname,
                                                        "ot-harjoitustyo", filename))
        else:
            print("Ruutua on jo klikattu")
