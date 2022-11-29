import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A Class for controlling ship-launched bullets"""

    def __init__(self, ai_settings, screen, starship):
        """Creates a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet at position (0,0) and assign the correct position
        self.image_bullet = pygame.image.load("data/images/Laser_shot.png")
        self.image_laser = pygame.image.load('data/images/laser-beam.png')
        self.rect = self.image_bullet.get_rect()
        self.rect.centerx = starship.rect.centerx
        self.rect.top = starship.rect.top

        # Bullet position is stored in real format.
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self, ):
        """Moves the bullet up the screen"""
        # Update bullet position in real format
        self.y -= self.speed_factor
        # Update the position of the rectangle.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet on a screen"""
        self.screen.blit(self.image_bullet, self.rect)

    def draw_laser(self):
        """Draw laser on a screen"""
        self.screen.blit(self.image_laser, self.rect)
