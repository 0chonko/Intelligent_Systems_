'''FINAL ASSIGNMENT CREATIVE TECHNOLOGY 2020 MOD 6 '''
from Maze.src import Shapes_detector

'''German Savchenko s2185091'''
'''AI AND PROGRAMMING'''

import pygame
from Maze.helpers.constants import Constants

from Maze.src.Maze_gen import Maze


class shapes_dec_manager:
    #cls initialization in order to have access from the class method
    maze = Maze(40, 40, (Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))

    def __init__(self, size, window_width, window_height):
        pygame.init()

        self.size = size
        self.widthWindow = window_width
        self.heightWindow = window_height

        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.SysFont(pygame.font.get_fonts()[0], 64)
        self.time = pygame.time.get_ticks()
        self.maze.generate_room(self.widthWindow, self.heightWindow)
        self.opencv_contours = Shapes_detector.Shapes_Dec()

    def manager_update(self):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - self.time
        self.time = current_time
        self.update_game(delta_time)

        self.draw_components()
        self.maze.generate_room(self.widthWindow, self.heightWindow)

        self.shape_maze_w_contours()
        self.maze.a_star_search()



    def update_game(self, dt):
        pass

    def shape_maze_w_contours(self):
        for i in range( 0 , len(self.opencv_contours.xii)):
            j = self.opencv_contours.xii[i]
            k = self.opencv_contours.yii[i]
            self.maze.shape_space(int(j * Constants.GRID_SIZE / Constants.WINDOW_WIDTH + 5) , int(k * Constants.GRID_SIZE / Constants.WINDOW_HEIGHT - 5))


    def draw_components(self):
        #refresh screen
        self.screen.fill([255, 255, 255])

        #camera and detection draw
        frame = pygame.surfarray.make_surface(self.opencv_contours.generate_contour())

        self.screen.blit(frame, (0,0))

        #draw maze
        self.maze.draw_maze(self.screen)
        pygame.display.flip()


    def reset(self):
        pass

