import pygame
from setting import Setting
from ship import Ship
import gamefunctions as gf


def run_game():
    # Инициализирует игру и создает объект экрана.
    ai_setting = Setting()
    pygame.init()
    screen = pygame.display.set_mode(ai_setting.display_resolution)
    pygame.display.set_caption("Alien Invasion")
    # Создание корабля.
    starship = Ship(screen, ai_setting)

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(starship)
        starship.update()
        gf.update_screen(ai_setting, screen, starship)


run_game()
