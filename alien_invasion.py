import sys
from settings import Settings
from ship import Ship
import game_functions as gamef
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats

import pygame

def run_game():
    pygame.init() # Initializes pygame
    settings = Settings() # Utilizing settings class
    screen = pygame.display.set_mode((settings.width , settings.height)) # creates the screen 
    pygame.display.set_caption('Alien Invasion') # Caption for game
    stats = GameStats(settings)

    ship = Ship(settings , screen) # creating ship
    alien = Alien(settings , screen) # creating an alien
    

    background = (0 , 0 , 256) # Background color

    bullets = Group() # Storing bullets
    aliens = Group() # storing aliens

    gamef.create_fleet(settings , screen ,ship , aliens) # Creating fleet

    while True:
        gamef.check_events(settings , screen , ship , bullets)
        if stats.game_active:
            ship.update()
            gamef.update_bullets(settings , screen , ship , bullets , aliens)
            gamef.update_aliens(settings , screen , ship  , bullets , aliens , stats)
        gamef.update_screen(settings,screen,ship, bullets , aliens)
        


if __name__ == "__main__":
    run_game()