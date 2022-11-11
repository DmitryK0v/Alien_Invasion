import sys
import pygame
from setting import Setting
from ship import Ship


def run_game():
    # Инициализирует игру и создает объект экрана.
    ai_setting = Setting()
    pygame.init()
    screen = pygame.display.set_mode(ai_setting.display_resolution)
    pygame.display.set_caption("Alien Invasion")
    # Создание корабля.
    starship = Ship(screen)


    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # При каждом проходе цикла перерисовывается экран.
            screen.fill(ai_setting.background_color)
            starship.blitme()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


run_game()
