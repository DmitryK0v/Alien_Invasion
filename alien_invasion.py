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
    screen = pygame.display.set_mode((ai_settings.display_width, ai_settings.display_height))
    pygame.display.set_caption("Alien Invasion")
    # Create ship.
    starship = Ship(screen, ai_settings)
    # Create a groups of bullets and Aliens.
    aliens = Group()
    bullets = Group()
    # Generate of an alien fleet
    gf.generate_fleet(ai_settings, screen, aliens)
    # Runs main cycle of game.
    while True:
        gf.check_events(ai_settings, screen, starship, bullets)
        starship.update()
        bullets.update()
        gf.update_aliens(aliens)
        gf.remove_bullets(bullets)
        gf.update_screen(ai_settings, screen, starship, aliens, bullets)


run_game()
