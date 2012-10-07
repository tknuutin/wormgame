# -*- coding: utf-8 -*-
"""Contains a hexagonal grid class the game uses as a base for its levels."""


WALL = False
FLOOR = True

class HexGrid:
    """A class that acts as a hexagonal grid for the game to determine the dimensions of its levels."""
    
    def __init__(self, width, height):
        
        self.width = width
        self.height = height
        self.grid = self._create_grid()
        
    def _create_grid(self):
        """Creates a grid that gets its width and height from the corresponding attributes of the HexGrid instance.
        The borders of the grid are set as wall, rest is floor."""
        
        add_column = lambda: [WALL for y in range(0, self.height)]
        grid = [add_column() for x in range(0, self.width)]
        print grid
        for x in range(1, self.width - 1):
            for y in range(1, self.height - 1):
                grid[x][y] = FLOOR
            
        return grid
    
    def _check_coords(self, x, y):
        """Checks if the coordinates are outside the grid's bounds, and if they are, raises InvalidCoordsError."""
        
        if not 0 <= x < self.width or not 0 <= y < self.height:
            raise InvalidCoordsError("Coordinates out of grid:", x, y)
    
    def is_floor(self, x, y):
        """If the hexagon in the given coordinates is a floor hexagon, returns True, otherwise False. If the coordinates
        are outside the grid's bounds, raises InvalidCoordsError."""
        
        self._check_coords(x, y)
        return grid[x][y]
        
    def _get_prev_x(self, x, y):
        """If the given coordinates are inside the grid's bounds, returns the corresponding coordinates, where the x value
        has been decremented by one. Otherwise raises raises InvalidCoordsError."""
        
        self._check_coords(x - 1, y)
        return x - 1, y
        
    def _get_next_x(self, x, y):
        """If the given coordinates are inside the grid's bounds, returns the corresponding coordinates, where the x value
        has been incremented by one. Otherwise raises raises InvalidCoordsError."""
        
        self._check_coords(x + 1, y)
        return x + 1, y
        
    def get_southwest(self, x, y):
        """If the given coordinates are inside the grid's bounds, returns the coordinates that correspond to southwest
        direction in the hexagonal grid. Otherwise raises raises InvalidCoordsError."""
        
        if x % 2 == 0:    
            self._check_coords(x - 1, y + 1)
            return x - 1, y + 1
        else:
            return self._get_prev_x(x, y)
            
    def get_south(self, x, y):
        """If the given coordinates are inside the grid's bounds, returns the coordinates that correspond to south
        direction in the hexagonal grid. Otherwise raises raises InvalidCoordsError."""
        
        self._check_coords(x, y + 1)
        return x, y + 1
        
    def get_southeast(self, x, y):
        """If the given coordinates are inside the grid's bounds, returns the coordinates that correspond to southeast
        direction in the hexagonal grid. Otherwise raises raises InvalidCoordsError."""
        
        if x % 2 == 0:
            self._check_coords(x + 1, y + 1)
            return x + 1, y + 1
        else:
            return self._get_next_x(x, y)
    
    def get_northwest(self, x, y):
        """If the given coordinates are inside the grid's bounds, returns the coordinates that correspond to northwest
        direction in the hexagonal grid. Otherwise raises raises InvalidCoordsError."""
        
        if x % 2 == 0:
            return self._get_prev_x(x, y)
        else:
            self._check_coords(x - 1, y - 1)
            return x - 1, y - 1
    
    def get_north(self, x, y):
        """If the given coordinates are inside the grid's bounds, returns the coordinates that correspond to north
        direction in the hexagonal grid. Otherwise raises raises InvalidCoordsError."""
        
        self._check_coords(x, y - 1)
        return x, y - 1
        
    def get_northeast(self, x, y):
        """If the given coordinates are inside the grid's bounds, returns the coordinates that correspond to northeast
        direction in the hexagonal grid. Otherwise raises raises InvalidCoordsError."""
        
        if x % 2 == 0:    
            return self._get_next_x(x, y)
        else:
            self._check_coords(x + 1, y - 1)
            return x + 1, y - 1

    def print_grid(self):
        """Prints the hexagonal grid for debug purposes."""
        
        for y in range(0, self.height):
            for x in range(0, self.width):
                print self.grid[x][y],
            print ""
    
class InvalidCoordsError(Exception):
    
    def __init__(self, message, x, y):
        
        self.message = message
        self.x = x
        self.y = y
    
    def __str__(self):
        return message, str(x_direction), str(y_direction)
    
if __name__ == "__main__":
    hexgrid = HexGrid(15, 15)
    hexgrid.print_grid()
    hexgrid.grid[7][7] = False
    print ""
    hexgrid.print_grid()
    x, y = hexgrid.get_northeast(7, 7)
    hexgrid.grid[7][7] = True
    hexgrid.grid[x][y] = False
    print ""
    hexgrid.print_grid()
    hexgrid.grid[x][y] = True
    x, y = hexgrid.get_northwest(x, y)
    hexgrid.grid[x][y] = False
    print ""
    hexgrid.print_grid()
    hexgrid.grid[x][y] = True
    x, y = hexgrid.get_north(x, y)
    hexgrid.grid[x][y] = False
    print ""
    hexgrid.print_grid()
    hexgrid.grid[x][y] = True
    x, y = hexgrid.get_south(x, y)
    hexgrid.grid[x][y] = False
    print ""
    hexgrid.print_grid()
    hexgrid.grid[x][y] = True
    x, y = hexgrid.get_southeast(x, y)
    hexgrid.grid[x][y] = False
    print ""
    hexgrid.print_grid()
    hexgrid.grid[x][y] = True
    x, y = hexgrid.get_southwest(x, y)
    hexgrid.grid[x][y] = False
    print ""
    hexgrid.print_grid()
    
    