import pygame.font
import json
from pygame.sprite import Group
from ship import Ship


class Scoreboard(object):
    """Class for displaying game information."""

    def __init__(self, screen, ai_settings, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.high_score = 0
        self.read_high_score()

        # Font settings for invoice output.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare invoice images.
        self.prep_ships()
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def read_high_score(self):
        file = open('data/record.json', 'r')
        self.high_score = int(json.load(file))
        file.close()

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.ship_ico()
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_score(self):
        """Converts the current score to a graphic."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # Output of the account in the right upper part of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_level(self):
        """Converts the level to a graphic."""

        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color, self.ai_settings.bg_color)
        # The level is displayed under the current score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 60

    def prep_high_score(self):
        """Converts the record score to a graphic."""
        self.high_score = int(round(self.high_score, -1))
        high_score_str = "{:,}".format(self.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        # The record is centered on the top side.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def dump_high_record(self):
        file = open('data/record.json', 'w')
        json.dump(self.stats.high_score, file)
        file.close()

    def show_score(self):
        """Displays current score, record and number of remaining ships."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw ships.
        self.ships.draw(self.screen)
