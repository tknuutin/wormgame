# -*- coding: utf-8 -*-
"""
asdf
"""

import socket
import select

class SelectServer:
    """
    asdf
    """

    def __init__(self, host="127.0.0.1", port=1337):
        """
        asdf
        """
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        print "Listening on host %s port %s." % (host, port)
        self.server.listen(5)
        self.clients = []

    def get_updates(self):
        """
        select the socket to receive from
        """
        rlist = self.clients + [self.server]
        wlist = []
        xlist = []
        
        try:
            # A non-blocking select
            rready, wready, xready = select.select(rlist, wlist, xlist, 0)
        except select.error, e:
            pass # TODO!
        except socket.error, e:
            pass # TODO!

        for sock in rready:
            if sock == self.server:
                client, address = self.server.accept()
                print "New connection established with %s, port %d." % (address[0], address[1])
                self.clients.append(client)
                # TODO: Instantiate a new player
            else:
                try:
                    data = sock.recv(4096)
                    if data:
                        # Got data from a player
                        # TODO: Add this data to a command queue of
                        # the player in question
                        print "Data: %s" % (data)
                    else:
                        print "%s hung up" % (sock.fileno())
                        self.clients.remove(sock)
                except socket.error, e:
                    print "%s error'd" % (sock.fileno())
                    self.clients.remove(sock)

if __name__ == "__main__":
    my_server = SelectServer()

    while True:
        my_server.get_updates()

