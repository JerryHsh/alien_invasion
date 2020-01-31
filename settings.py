class Settings():
    """store all the settings in alien invasion"""

    def __init__(self):
        """initialize the game setting"""
        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # move 1.5 pixel every loop
        self.speed_factor = 1.5
        # the settings of the bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3
        # alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # alien direction  1 means right -1 means left
        self.fleet_direction = 1
