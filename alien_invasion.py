# The only file, that must be run.
import pygame
from pygame.sprite import Group

from setting import Setting
from ship import Ship
import gamefunctions as gf


def run_game():
    # Initializes the game and creates a screen object.
    ai_settings = Setting()
    pygame.init()
    screen = pygame.display.set_mode(ai_settings.display_resolution)
    pygame.display.set_caption("Alien Invasion")
    # Create ship.
    starship = Ship(screen, ai_settings)
    # Create a group to store bullets.
    bullets = Group()

    # Runs main cycle of game.
    while True:
        gf.check_events(ai_settings, screen, starship, bullets)
        starship.update()
        bullets.update()
        # Removal of bullets that have gone off the edge of the screen.
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        gf.update_screen(ai_settings, screen, starship, bullets)


run_game()
