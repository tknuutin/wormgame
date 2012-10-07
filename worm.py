# -*- coding: utf-8 -*-

EAST = "east"
WEST = "west"
NORTHEAST = "northeast"
NORTHWEST = "northwest"
SOUTHEAST = "southeast"
SOUTHWEST = "southwest"

import pygame

class Worm:


    def __init__(self, start_position, direction):
        """A new worm is created with starting coordinates (x, y) and direction string."""

        self.sections = [start_position]
        self.direction = direction
        self.grow_bool = True

        #TODO: add some sort of worm picture
        self.image = None

        #instantiate the rectangle needed to draw the worm
        self.rect = pygame.Rect(0, 0, 50, 50)

    def update_draw_rects(self):
        #TODO: fix
        """ Update the position of the Rectangle to where the Worm is in the play field. This doesn't work right! """
        self.rect.top, self.rect.left = self.sections[0]


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
        """Worm changes it's direction."""
        directions = {NORTHEAST : NORTHWEST, EAST : NORTHEAST,
            SOUTHEAST : EAST, SOUTHWEST : SOUTHEAST,
            WEST : SOUTHWEST, NORTHWEST : WEST}

        self.direction = directions[self.direction]


    def turn_right(self):
        """Worm changes it's direction."""

        directions = {NORTHEAST : EAST, EAST : SOUTHEAST,
            SOUTHEAST : SOUTHWEST, SOUTHWEST : WEST,
            WEST : NORTHWEST, NORTHWEST : NORTHEAST}

        self.direction = directions[self.direction]


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
