# -*- coding: utf-8 -*-

class Worm:
    
    def __init__(self, start_position, direction):
        self.sections = [start_position]
        self.direction = direction
        self.grow_bool = True
        
    def move(self, direction):
        x, y = self.sections[0] 
        
        if direction == "northeast":
            head = x+1, y-1
            self.sections.insert(0, head)
        if direction == "east":
            head = x+1, y
            self.sections.insert(0, head)
        if direction == "southeast":
            head = x+1, y+1
            self.sections.insert(0, head)
        if direction == "southwest":
            head = x-1, y+1
            self.sections.insert(0, head)
        if direction == "west":
            head = x-1, y
            self.sections.insert(0, head)
        if direction == "northwest":
            head = x-1, y-1
            self.sections.insert(0, head)
             
        if not self.grow_bool:
            self.sections.pop(-1)
            
        if len(self.sections) > 3:
            self.grow_bool = False
        
    def grow(self):
        self.grow_bool = True
        
    def get_sections(self):
        return self.sections
        
if __name__ == "__main__":
    wyrm = Worm((0,0), "southeast")
    print wyrm.get_sections()
    wyrm.move("east")
    print wyrm.get_sections()
    wyrm.move("southeast")
    print wyrm.get_sections()
    wyrm.move("southeast")
    print wyrm.get_sections()
    wyrm.move("east")
    print wyrm.get_sections()
    wyrm.move("east")
    print wyrm.get_sections()
    wyrm.move("east")
    wyrm.grow()
    wyrm.move("southeast")
    print wyrm.get_sections()
    