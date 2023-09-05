class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialise the game's settings"""
        # Screem Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (173, 216, 230)

        # ship settings
        self.ship_speed = 2

        # bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
