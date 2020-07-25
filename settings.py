class Settings():

    def __init__(self):
        self.width = 1200
        self.height = 800
        self.background = (230,230,230) # Background color
        
        # Ship stuff
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60 , 60 , 60
        self.bullets_allowed = 5

        # Alien stuff
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1 for right , -1 for left