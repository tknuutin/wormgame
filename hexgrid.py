# -*- coding: utf-8 -*-

WALL = False
FLOOR = True

class HexGrid:
    
    def __init__(self, width, height):
        
        self.width = width
        self.height = height
        self.grid = self._create_grid()
        
    def _create_grid(self):
        
        add_column = lambda: [WALL for y in range(0, self.height)]
        grid = [add_column() for x in range(0, self.width)]
        for x in range(1, self.width - 1):
            for y in range(1, self.height - 1):
                grid[x][y] = FLOOR
            
        return grid
        
    def is_floor(self, x, y):
        
        self._check_coors(x, y)
        return grid[x][y]

    def _check_coords(self, x, y):
        
        if not 0 <= x <= self.width or not 0 <= y <= self.height:
            raise InvalidCoordsError("Coordinates out of grid:", x, y)
    
    def get_northwest(self, x, y):
        
        self._check_coords(x - 1, y + 1)
        return x - 1, y + 1
            
    def get_north(self, x, y):
        
        self._check_coords(x, y + 1)
        return x, y + 1
        
    def get_northeast(self, x, y):
        
        self._check_coords(x + 1, y + 1)
        return x + 1, y + 1
    
    def get_southwest(self, x, y):
        
        self._check_coords(x - 1, y)
        return x - 1, y
    
    def get_south(self, x, y):
        
        self._check_coords(x, y - 1)
        return x, y - 1
        
    def get_southeast(self, x, y):
        
        self._check_coords(x + 1, y)
        return x + 1, y

    def print_grid(self):
        
        for row in self.grid:
            for square in row:
                print square,
            print ""
    
class InvalidCoordsError:
    
    def __init__(self, message, x, y):
        
        self.message = message
        self.x = x
        self.y = y
    
    def __str__(self):
        return message, str(x_direction), str(y_direction)
    
if __name__ == "__main__":
    hexgrid = HexGrid(15, 15)
    hexgrid.print_grid()