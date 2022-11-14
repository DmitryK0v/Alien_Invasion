import sys
import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, starship, bullets):
    """Handles button presses"""
    if event.key == pygame.K_RIGHT:
        starship.moving_right = True
    elif event.key == pygame.K_LEFT:
        starship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, starship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, starship):
    """Handles button release"""
    if event.key == pygame.K_RIGHT:
        starship.moving_right = False
    elif event.key == pygame.K_LEFT:
        starship.moving_left = False


def fire_bullet(ai_settings, screen, starship, bullets):
    """Fires a bullet if the maximum has not yet been reached"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, starship)
        bullets.add(new_bullet)


def check_events(ai_settings, screen, starship, bullets):
    """Handles keystrokes and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.K_q:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, starship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, starship)


def generate_fleet(ai_settings, screen, aliens):
    # Create an alien and calculate the number of aliens in a row.
    # Spacing between adjacent aliens equals one alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.display_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (1.5 * alien_width))

    # Create the first row of aliens
    for alien_number in range(number_aliens_x):
        # Create an alien and place it in a row
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


def update_screen(ai_settings, screen, starship, aliens, bullets):
    """Refreshes the image on the screen and displays a new screen."""
    # The screen is redrawn on each iteration of the loop
    screen.fill(ai_settings.background_color)
    # All bullets are displayed behind the images of the ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    starship.blitme()
    aliens.draw(screen)
    # Display the last screen drawn.
    pygame.display.flip()


def remove_bullets(bullets):
    # Removal of bullets that have gone off the edge of the screen.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_aliens(aliens):
    """Обновляет позиции всех пришельцев во флоте."""
    aliens.update()
