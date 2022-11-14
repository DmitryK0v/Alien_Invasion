import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class representing a single alien"""

    def __init__(self, screen, ai_settings):
        """Initializes the alien and sets its initial position"""
        super().__init__()
        self.screen = screen
        self.ai = ai_settings

        # Load the alien image and assign the rect attribute.
        self.image = pygame.image.load('data/images/Alien-1.png')
        self.rect = self.image.get_rect()

        # Each new alien appears in the upper left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save the exact position of the alien
        self.x = float(self.rect.x)
        self.alien_speed_factor = 1

    def update(self):
        """Moving alien to the right"""
        self.x += self.alien_speed_factor
        self.rect.x = self.x

    def blitme(self):
        """Displays the alien in its current position."""
        self.screen.blit(self.image, self.rect)
