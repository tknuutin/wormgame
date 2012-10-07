# -*- coding: utf-8 -*-

EAST = "east"
WEST = "west"
NORTHEAST = "northeast"
NORTHWEST = "northwest"
SOUTHEAST = "southeast"
SOUTHWEST = "southwest"

class Worm:
    
    def __init__(self, start_position, direction):
        """A new worm is created with starting coordinates (x, y) and direction string."""
        
        self.sections = [start_position]
        self.direction = direction
        self.grow_bool = True
        
    def move(self, direction):
        """Worm moves to the specified direction and grows 
        if self.grow() has been called. Worm grows until it 
        reaches the length of 3."""
        
        x, y = self.sections[0] 
        self.direction = direction
        
        if direction == NORTHEAST:
            head = x+1, y+1
        elif direction == EAST:
            head = x+1, y
        elif direction == SOUTHEAST:
            head = x+1, y-1
        elif direction == SOUTHWEST:
            head = x-1, y-1
        elif direction == WEST:
            head = x-1, y
        elif direction == NORTHWEST:
            head = x-1, y+1

        self.sections.insert(0, head)
        if not self.grow_bool:
            self.sections.pop(-1)
            
        if len(self.sections) > 3:
            self.grow_bool = False
            
    def turn_left(self):
        """Worm moves to a direction to the left from the previous direction."""
    
        if self.direction == NORTHEAST:
            self.direction = NORTHWEST
        elif self.direction == EAST:
            self.direction = NORTHEAST
        elif self.direction == SOUTHEAST:
            self.direction = EAST;
        elif self.direction == SOUTHWEST:
            self.direction = SOUTHEAST;
        elif self.direction == WEST:
            self.direction = SOUTHWEST
        elif self.direction == NORTHWEST:
            self.direction == WEST
        self.move(self.direction)
        
    def turn_right(self):
        """Worm moves to a direction to the right from the previous direction."""
        if self.direction == NORTHEAST:
            self.direction = EAST
        elif self.direction == EAST:
            self.direction = SOUTHEAST
        elif self.direction == SOUTHEAST:
            self.direction = SOUTHWEST
        elif self.direction == SOUTHWEST:
            self.direction = WEST
        elif self.direction == WEST:
            self.direction = NORTHWEST
        elif self.direction == NORTHWEST:
            self.direction = NORTHEAST
        self.move(self.direction)
        
    def forward(self):
        """Worm moves without changing direction."""
        self.move(self.direction)
        
    def grow(self):
        """Worm grows one unit in length time the worm moves."""
        self.grow_bool = True
        
    def get_sections(self):
        """Returns a list of the coordinates the worm occupies."""
        return self.sections
        
if __name__ == "__main__":
    wyrm = Worm((0, 20), SOUTHEAST)
    print wyrm.get_sections()
    wyrm.move(EAST)
    print wyrm.get_sections()
    wyrm.move(SOUTHEAST)
    print wyrm.get_sections()
    wyrm.move(SOUTHEAST)
    print wyrm.get_sections()
    wyrm.move(EAST)
    print wyrm.get_sections()
    wyrm.move(EAST)
    print wyrm.get_sections()
    wyrm.move(EAST)
    wyrm.grow()
    wyrm.move(SOUTHEAST)
    wyrm.forward()
    wyrm.turn_left()
    wyrm.turn_right
    print wyrm.get_sections()
    