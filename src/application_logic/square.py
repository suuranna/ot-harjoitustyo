import os
import pygame

dirname1 = os.path.dirname(__file__)
dirname = dirname1.replace("application_logic","")

class Square(pygame.sprite.Sprite):
    """Luokka, joka kuvaa pelinäkymässä olevia neliöitä ja
       mitä tapahtuu, kun neliötä klikkaa

    Attributes:
         Neliön kuva ja miltä neliö näyttää käyttöliittymässä
         rect = Määrittelee neliön kuvan ulottovuuden
         x_coordinate: Neliön vasemman yläkulman x-koordinaatti
         y_coordinate: Neliön vasemman yläkulman y-koordinaatti

    """
    def __init__(self, number, x_coordinate, y_coordinate):
        """Luokan konstruktori, joka luo uuden neliön

        Args:
            number: Neliön "kääntöpuolella" oleva numero
            x_coordinate: Neliön vasemman yläkulman x-koordinaatti
            y_coordinate: Neliön vasemman yläkulman y-koordinaatti

        """
        super().__init__()
        self.number = number
        self.fliped = False
        self.image = pygame.image.load(os.path.join(dirname, "kuvat_peliin", "kuvake.png"))
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate

    def flip(self):
        """ "Kääntää" neliön, jolloin näkyviin tulee neliön numero

        """
        if not self.fliped:
            self.fliped = True
            filename = "kuvake"+str(self.number)+".png"
            self.image = pygame.image.load(os.path.join(dirname,
                                                        "kuvat_peliin", filename))
