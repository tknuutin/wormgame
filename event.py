# -*- coding: utf-8 -*-

class Event:

    def __init__(self, type, address = None, port = None, socket = None, 
        added = None, error = None, removed = None, data = None):
    
        self.type = type
        self.address = address
        self.port = port
        self.socket = socket
        self.added = added
        self.error = error
        self.removed = removed
        self.data = data
