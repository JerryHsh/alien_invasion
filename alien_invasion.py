import sys
import pygame
from pygame.sprite import Group
from alien import Alien

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import Gamestats


def run_game():
    """initialize a screen object"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # create a ship
    ship = Ship(ai_settings, screen)
    # create a group to store the bullet
    bullets = Group()
    aliens=Group()
    #create a group of the alien
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #create an alien object
    alien=Alien(ai_settings,screen)
    #statistics
    stats=Gamestats(ai_settings)
    # begin the main loop
    while True:
        # survalence the keyboard and the mouse
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active==True:
            # remake the location
            ship.update()
            gf.update_bullet(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        # fill the screen with background color
        # let the recently draw screen visible
        gf.update_screen(ai_settings, screen, ship, aliens,bullets)


run_game()
