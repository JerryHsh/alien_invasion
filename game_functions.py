import sys
import pygame
from bullet import Bullet
from alien import Alien
from random import randint


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


def check_events(ai_settings, screen, ship, bullets):
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


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """update the graph on the screen"""
    # fill the screen every time when looping
    screen.fill(ai_settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # let the recently draw screen visible
    pygame.display.flip()


def update_bullet(bullets):
    bullets.update()
    # delete the disappear bullet
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def get_number_alien_x(ai_settings,alien_width):
    """calculate how many aliens  a line can hold"""
    available_space_x = ai_settings.screen_width-2*alien_width
    number_alien_x = int(available_space_x/(2*alien_width))
    return number_alien_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """calculate how many row can the screen hold"""
    available_space_y=ai_settings.screen_height-3*alien_height-ship_height
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """create an alien and put it on the current line"""
    #random_flag=randint(0,1)
    random_flag=1
    if random_flag:
        alien=Alien(ai_settings,screen)
        alien_width = alien.rect.width
        alien.x=alien_width+2*alien_width*alien_number
        alien.rect.x=alien.x
        alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
        aliens.add(alien)


def create_fleet(ai_settings, screen, ship,aliens):
    """create a group of alien"""
    # create and calculate how many aliens  a line can hold
    # the gap width is the width of the alien
    alien = Alien(ai_settings, screen)
    number_alien_x=get_number_alien_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    #create the first line alien
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            #create an alien
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def update_aliens(aliens):
    """update all the aliens in the alien group"""
    aliens.update()
