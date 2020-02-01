class Gamestats():
    """track the statistics of the game"""
    def __init__(self,ai_settings):
        """initialize the information"""
        self.ai_settings=ai_settings
        self.reset_stats()
        self.game_active=True
    
    def reset_stats(self):
        """reset the changable information when game is running"""
        self.ships_left=self.ai_settings.ship_limit