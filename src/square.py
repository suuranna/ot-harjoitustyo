import pygame
import os

dirname = os.path.dirname("/home/suuranna/Ohjelmistotekniikka_jutut/ot-harjoitustyo")

class Square(pygame.sprite.Sprite):
        def __init__(self, square_size, number, x, y):
                super().__init__()
                self.square_size = square_size
                #self.rect = pygame.Rect(x, y, self.square_size, self.square_size)
                self.number = number
                self.fliped = False

                self.image = pygame.image.load(os.path.join(dirname, "ot-harjoitustyo", "kuvake.png"))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                #self.image = pygame.Rect(x, y, 50, 50)
                #self.rect = pygame.Rect(x, y, 50, 50)

        def flip(self):
                if not self.fliped:
                        print("Klikattu ruutua sijainnissa", self.rect.x, self.rect.y, " ja jonka numero on ", self.number)
                        self.fliped = True
                else:
                        print("Ruutua on jo klikattu")
