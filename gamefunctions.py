import sys
import pygame


def check_events(starship):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                starship.moving_right = True
            elif event.key == pygame.K_LEFT:
                starship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                starship.moving_right = False
            elif event.key == pygame.K_LEFT:
                starship.moving_left = False


def update_screen(ai_settings, screen, starship):
    """Обновляет изображения на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(ai_settings.background_color)
    starship.blitme()
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
