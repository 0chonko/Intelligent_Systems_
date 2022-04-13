'''FINAL ASSIGNMENT CREATIVE TECHNOLOGY 2020 MOD 6 '''
'''German Savchenko s2185091'''
'''AI AND PROGRAMMING'''

from Maze.src.Grid_element import GridElement
from Maze.helpers.directions import Direction
import bisect
import math
from Maze.src.Shapes_detector import Shapes_Dec as sd

class Maze:
    """
    Generates a grid based maze based on GridElements
    This class also contains search algorithms for
    depth first, breath first, greedy and A* star search to
    solve the generated mazes
    """

    def __init__(self, grid_size_x, grid_size_y, screen_size):
        self.sd = sd()
        self.grid_size = (grid_size_x, grid_size_y)
        self.grid_size_x = grid_size_x
        self.grid_size_y = grid_size_y
        self.grid = [[GridElement(x, y, (screen_size[0] / grid_size_x, screen_size[1] / grid_size_y)) for y in
                      range(self.grid_size_y)] for x in range(self.grid_size_x)]
        self.init_grid()

        # Defines the final target of the search algorithm
        self.target = self.grid[-1][-1]
        for x in range(self.grid_size_x):
            for y in range(self.grid_size_y):
                self.grid[x][y].update_gscore(self.target)
        self.count = 0

    """
    Initializes the grid with which the maze will be generated
    and links the correct GridElement cells with each other  
    """

    def init_grid(self):
        for x in range(self.grid_size_x):
            for y in range(self.grid_size_y):
                self.grid[x][y].reset()
                if x > 0:
                    self.grid[x][y].neighbours[Direction.WEST] = self.grid[x - 1][y]
                if x < self.grid_size_x - 1:
                    self.grid[x][y].neighbours[Direction.EAST] = self.grid[x + 1][y]
                if y > 0:
                    self.grid[x][y].neighbours[Direction.NORTH] = self.grid[x][y - 1]
                if y < self.grid_size_y - 1:
                    self.grid[x][y].neighbours[Direction.SOUTH] = self.grid[x][y + 1]

    """
    Ajusts values to closest grid positions (center of a cell)
    """
    def snap(myGrid, myValue):
        ix = bisect.bisect_right(myGrid, myValue)
        if ix == 0:
            return myGrid[0]
        elif ix == len(myGrid):
            return myGrid[-1]
        else:
            return min(myGrid[ix - 1], myGrid[ix], key=lambda gridValue: abs(gridValue - myValue))

    """
    Resets the GridElements of the maze
    """

    def reset_maze(self):
        for x in range(self.grid_size_x):
            for y in range(self.grid_size_y):
                self.grid[x][y].reset()

    """
    Resets the state of the GridElements of the maze
    """

    def reset_grid_elements(self):
        for x in range(self.grid_size_x):
            for y in range(self.grid_size_y):
                self.grid[x][y].reset_state()

    """
    Draw every GridElement in the maze
    """

    def draw_maze(self, surface):
        for row in self.grid:
            for element in row:
                element.draw_grid_element(surface)

    """
    Perform A-star search from from predefined point A to predefined point B
    """

    def a_star_search(self):
        # set the starting point of the search
        start = self.grid[20][0]
        start.is_seen = True
        start.update_fscore(0)
        sorted_list = [start]

        while len(sorted_list) > 0:
            # the current element is the first element of the queue
            current_element = sorted_list.pop(0)
            # mark it as visited
            current_element.is_visited = True
            # if  you did not find the target
            if current_element != self.target:
                for next_element in current_element.unvisited_neighbours():
                    # if they have not been seen before , increment the fscore , set the parent , set the is_seen flag , and insert into queue
                    if not next_element.is_seen:
                        next_element.update_fscore(current_element.fscore + 1)
                        next_element.set_parent(current_element)
                        next_element.is_seen = True
                        bisect.insort_left(sorted_list, next_element)
                    else:
                        if next_element.score > current_element.score:
                            # if they are in the queue remove them first
                            if next_element in sorted_list:
                                sorted_list.remove(next_element)
                            # increment the fscore , set the parent , set the is_seen flag , and insert into queue
                            next_element.update_fscore(current_element.fscore + 1)
                            next_element.set_parent(current_element)
                            next_element.is_seen = True
                            bisect.insort_left(sorted_list, next_element)
            else:
                # otherwise (target was found), leave the loop
                break
        # If the target was found , compute the path , back to front .

        if current_element == self.target:
            length = 0
            while current_element is not None:
                current_element.is_marked = True
                current_element = current_element.parent
                length += 1
                print("Detected length of the path: " + str(length))



    def constrain(val, min_val, max_val):
        return min(max_val, max(min_val, val))


    def generate_room(self, x, y):
        """Generates rooms, with specific positions."""
        self.reset_maze()
        self.open_maze()

# -----------------------------------------------------------------------------------------#
    """ADDITIONAL POSSIBLE FEATURE FOR GENERATING OBSTACLES AND ALTERING SOUND"""

    def distance_element_from_cursor(self, x1, y1, x2,y2):
        dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return dist

    def open_maze(self):
        for x in range(0, self.grid_size_x):
            for y in range(0, self.grid_size_y):
                    for direction in Direction:
                        self.grid[x][y].remove_wall(direction)

    """GENERATE MAZE IN POINTS RESULTED POSITIVE IN POINT POLYGON TEST"""
    def shape_space(self, x, y):
        if 0 < x < 40 and 0 < y < 40:
            # print ("success")
            for direction in Direction:
                self.grid[y][x].add_wall(direction)



