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
        gf.remove_bullets(bullets)
        gf.update_screen(ai_settings, screen, starship, bullets)


run_game()
