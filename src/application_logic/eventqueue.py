import pygame

class Eventqueue:
    """Pygamen tapahtumajono

    """
    def get_event(self):
        """Palauttaa eventsit eli käyttäjän syötteet

        Returns:
            eventsit eli käyttäjän syötteet
        """
        return pygame.event.get()
