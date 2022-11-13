"""Класс для хранения всех настроек игры Alien Invasion."""


class Setting(object):
    def __init__(self):
        self.display_resolution = (1200, 600)
        # Назначение цвета фона.
        self.background_color = (230, 230, 230)
        self.ship_speed_factor = 1.5




