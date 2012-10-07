# -*- coding: utf-8 -*-

import socket

class Client:

    def __init__(self, host="127.0.0.1", port=1337):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        self.buffer_size = 1024
        
        print "Connected to host %s port %s." % (host, port)
        
    def close(self):
        self.client.close()
        
    def send_event(self, event):
        self.client.send(event)
        
    def listen(self):
        return self.client.recv(self.buffer_size)
        
if __name__ == "__main__":
    client = Client()
    
    client.send_event("herp derp")
    client.listen()