import pygame.font


class Scoreboard(object):
    """Class for displaying game information."""

    def __init__(self, screen, ai_settings, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for invoice output.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Preparing the original image.
        self.prep_score()

    def prep_score(self):
        """Converts the current score to a graphic."""
        store_str = str(self.stats.score)
        self.score_image = self.font.render(store_str, True, self.text_color, self.ai_settings.bg_color)

        # Output of the account in the right upper part of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Выводит счет на экран."""
        self.screen.blit(self.score_image, self.score_rect)
