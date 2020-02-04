class Gamestats():
    """track the statistics of the game"""
    def __init__(self,ai_settings):
        """initialize the information"""
        self.ai_settings=ai_settings
        self.reset_stats()
        #make the game not active at first
        self.game_active=False
    
    def reset_stats(self):
        """reset the changable information when game is running"""
        self.ships_left=self.ai_settings.ship_limit
    
