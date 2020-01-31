import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """a class manage the bullet which shut by the ship"""

    def __init__(self, ai_settings, screen, ship):
        """create a bullet object on ship position"""
        super().__init__()
        self.screen = screen
        # create a rectangle in(0,0) and then put it on the right position
        # using class pygame.Rect to create a rectangle object  and the 0,0 means the left top cordinate
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # store the position of the bullet by float
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """moving bullet upward"""
        # update the float position
        self.y -= self.speed_factor
        # update the position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
