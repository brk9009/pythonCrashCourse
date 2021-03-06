import pygame
import sys

from settings import Settings
from rocket import Rocket
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.caption_name)
    
    # Make a rocket
    rocket = Rocket(settings, screen)
    
    # Start the main loop for the game
    while True:
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(settings, screen, rocket)
    
run_game()   