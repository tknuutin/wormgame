"""
Player
"""
import pygame

class Player(object):
    def __init__(self, worm=None, name="", socket=None):
        self.worm = worm
        self.name = name
        self.socket = socket