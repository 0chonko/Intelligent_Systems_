'''FINAL ASSIGNMENT CREATIVE TECHNOLOGY 2020 MOD 6 '''
'''German Savchenko s2185091'''
'''AI AND PROGRAMMING'''

import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../..'))
import pygame

from Maze.helpers.keyboard_handler import KeyboardHandler
from Maze.helpers.constants import Constants
from Maze.src.Shapes_detector_features_manages import shapes_dec_manager as manager

class Game:

    """
    Initialize PyGame and create a graphical surface to write. Similar
    to void setup() in Processing
    """
    def __init__(self):
        self.size = (Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        self.man = manager(self.size, Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        self.keyboard_handler = KeyboardHandler()


    """
    Method 'game_loop' will be executed every frame to drive
    the display and handling of events in the background. 
    In Processing this is done behind the screen. Don't 
    change this, unless you know what you are doing.
    """

    def game_loop(self):
    #     current_time = pygame.time.get_ticks()
    #     delta_time = current_time - self.time
    #     self.time = current_time
        self.man.manager_update()

        self.handle_events()


    """
    Method 'handle_event' loop over all the event types and 
    handles them accordingly. 
    In Processing this is done behind the screen. Don't 
    change this, unless you know what you are doing.
    """
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.handle_key_down(event)
            if event.type == pygame.KEYUP:
                self.handle_key_up(event)


if __name__ == "__main__":
    game = Game()
    while True:
        game.game_loop()
