# -*- coding: utf-8 -*-

import random

class Level:
    
    def __init__(self, width, height):
        
        self.width = width
        self.height = height
        self.occupied_coors = [(height / 2, width / 2),
                               (height / 2 - 1, width / 2),
                               (height / 2, width / 2 - 1),
                               (height / 2 - 1, width / 2 - 1)]
        self.grid = self._create_grid()
        self._inflate_level()
        
    def _create_grid(self):
        
        add_row = lambda: ["o" for i in range(0, self.width)]
        grid = [add_row() for i in range(0, self.height)]
        for x, y in self.occupied_coors:
            grid[x][y] = "x"
            
        return grid
    
    def _get_inflatable_coors(self):
        
        inflatable_coors = []
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        
        for x, y in self.occupied_coors:
            for x_offset, y_offset in directions:
                try:    
                    if self.grid[x + x_offset][y + y_offset] != "x":
                        if x + x_offset >= 0 and y + y_offset >= 0:
                            inflatable_coors.append((x + x_offset, y + y_offset))
                except IndexError:
                    pass
                    
        return inflatable_coors
    
    def _inflate_square(self):
    
        inflatable_coors = self._get_inflatable_coors()
        x, y = random.choice(inflatable_coors)
        self.grid[x][y] = "x"
        self.occupied_coors.append((x, y))
    
    def _inflate_level(self):
       
        [self._inflate_square() for i in range(0, self.width * self.height / 3)]
        
    def print_grid(self):
        
        for row in self.grid:
            for square in row:
                print square,
            print ""
            
if __name__ == "__main__":
    level = Level(15, 15)
    level.print_grid()