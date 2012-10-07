
import worm, player
import random

class Game(object):
    def __init__(self, grid_size=52):
        self.client_player = player.Player()
        self.players = [self.client_player]
        self.grid_size = grid_size

    def add_player(self, player):
        self.players.append(player)

    def start(self):
        """ Initiate all player and worm states """
        for player in self.players:
            #TODO: make this algorithm better
            pos = (random.randint(0, self.grid_size), random.randint(0, self.grid_size))
            player.worm = worm.Worm(pos, random.choice((worm.EAST, worm.NORTHEAST, worm.NORTHWEST, worm.SOUTHEAST, worm.SOUTHWEST, worm.WEST)))

