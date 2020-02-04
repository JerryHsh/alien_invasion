import sys
import pygame
from bullet import Bullet
from alien import Alien
from random import randint
from time import sleep


def fire_bullet(ai_settings, screen, ship, bullets):
    # create a bullet
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # move the ship right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # move the ship left
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # create a bullet
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        # stop moving right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # stop moving right
        ship.moving_left = False


def check_events(ai_settings, screen, stats, play_button, ship, bullets):
    """respond to the event and the mouse action"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # every time we do something there would be an event registered in pygame as a KEYDOWN event
        # keydown is press the button keyup is released the button
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)


def check_play_button(stats, play_button, mouse_x, mouse_y):
    """start the game when the player click the button"""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """update the graph on the screen"""
    # fill the screen every time when looping
    screen.fill(ai_settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # let the recently draw screen visible
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    # check if there is any bullet collide with the alien
    # return a dictionary that key is a bullet and the value is the spaceship hit by it
    # true mean disappeat after collision false means not disappear
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # clear all the bullet in the Group and make a new fleet
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def update_bullet(ai_settings, screen, ship, aliens, bullets):
    bullets.update()
    # delete the disappear bullet
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def get_number_alien_x(ai_settings, alien_width):
    """calculate how many aliens  a line can hold"""
    available_space_x = ai_settings.screen_width-2*alien_width
    number_alien_x = int(available_space_x/(2*alien_width))
    return number_alien_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """calculate how many row can the screen hold"""
    available_space_y = ai_settings.screen_height-3*alien_height-ship_height
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """create an alien and put it on the current line"""
    # random_flag=randint(0,1)
    random_flag = 1
    if random_flag:
        alien = Alien(ai_settings, screen)
        alien_width = alien.rect.width
        alien.x = alien_width+2*alien_width*alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height+2*alien.rect.height*row_number
        aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """create a group of alien"""
    # create and calculate how many aliens  a line can hold
    # the gap width is the width of the alien
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)
    # create the first line alien
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            # create an alien
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """when alien reach the edge then take measure"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """update all the aliens in the alien group"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # check if alien is collided with ship
    # when there is no collision the function return None
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """respond to the ship hit event"""
    if stats.ships_left > 0:
        # ship left minus 1
        stats.ships_left -= 1
        # clear the aliens and the bullets
        aliens.empty()
        bullets.empty()
        # create  new aliens and put the ship back
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # pause
        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """check if there are aliens hit the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # do things just like ship got hit
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
