import sys
import pygame

from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, starship, bullets):
    """Handles button presses"""
    if event.key == pygame.K_RIGHT:
        starship.moving_right = True
    elif event.key == pygame.K_LEFT:
        starship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, starship, bullets)


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
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, starship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, starship)


def update_screen(ai_settings, screen, starship, bullets):
    """Refreshes the image on the screen and displays a new screen."""
    # The screen is redrawn on each iteration of the loop
    screen.fill(ai_settings.background_color)
    # All bullets are displayed behind the images of the ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    starship.blitme()
    # Display the last screen drawn.
    pygame.display.flip()


def remove_bullets(bullets):
    # Removal of bullets that have gone off the edge of the screen.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
