"""Class for storing all game settings - Alien Invasion."""


class Setting(object):
    def __init__(self):
        # Setting of screen
        self.display_width = 1200
        self.display_height = 600
        self.background_color = (230, 230, 230)

        # Setting of starship
        self.ship_speed_factor = 1.5

        # Setting of bullets
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Setting of alien
