import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """initialize the ship and its position"""
        self.screen = screen
        self.ai_settings = ai_settings
        # fetch the image of the ship and get it's out rectangle
        self.image = pygame.image.load("./images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # the sign to move
        self.moving_right = False
        self.moving_left = False

        # made every ship on the bottom and middle of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store the float  in attribute center
        self.center = float(self.rect.centerx)

    def blitme(self):
        """print ship in certain position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """using sign to move the ship"""
        # update the attribute 'center' but not rect.centerx
        if self.moving_right == True:
            self.center += self.ai_settings.speed_factor
        if self.moving_left == True:
            self.center -= self.ai_settings.speed_factor
        if self.center < self.screen_rect.left:
            self.center += self.ai_settings.screen_width
        if self.center > self.screen_rect.right:
            self.center -= self.ai_settings.screen_width
        # update the rect by self.center
        self.rect.centerx = self.center

    def center_ship(self):
        self.center=self.screen_rect.centerx