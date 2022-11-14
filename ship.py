import pygame


class Ship(object):
    def __init__(self, screen, ai_setting):
        """Initializes the ship and sets its initial position."""
        self.screen = screen
        # Loading a ship image and getting a rectangle.
        self.image = pygame.image.load('data/images/Ship-2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_setting
        # Each new ship appears at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Saving the real coordinate of the center of the ship.
        self.center = float(self.rect.centerx)
        # Movement Flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ship's position based on the flag."""
        # Update attribute center, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        """Drawing starship in current position on screen"""
        self.screen.blit(self.image, self.rect)
