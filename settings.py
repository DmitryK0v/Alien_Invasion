class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initializes static game settings."""
        # Screen settings.
        self.alien_points = None
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_limit = 3

        # Bullet settings.

        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings.
        self.fleet_drop_speed = 100

        # Speed up the game
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializes settings that change during the game"""
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1.5

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1.5

        # Scoring
        self.alien_points = 100

    def increase_speed(self):
        """Increases speed settings and cost aliens"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
