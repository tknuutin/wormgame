# -*- coding: utf-8 -*-
"""
Module for communication from and to clients.
"""

import socket
import select
import event

class SelectServer:
    """
    Server implementation that uses the select system call in a non-blocking mode
    to read data from clients and to accept new clients.
    """

    def __init__(self, host="127.0.0.1", port=1337):
        """
        Initialize a listening socket server
        """
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        print "Listening on host %s port %s." % (host, port)
        self.server.listen(5)
        self.clients = []

    def get_updates(self):
        """
        Receives information about new incoming clients and incoming data from clients.
        Returns the received information as a list of events.
        """
        client_events = []

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

        # Receive data from sockets that are ready to be read
        for sock in rready:
            if sock == self.server:
                # A new client is connecting - accept the connection
                client, address = self.server.accept()
                self.clients.append(client)
                #event = {"type" : "new_connection", "address" : address[0], "port" : address[1], "socket" : client, "added" : True}
                client_event = event.Event("new_connection", address[0], address[1], client, True)
                
                client_events.append(client_event)
            else:
                try:
                    data = sock.recv(4096)
                    if data:
                        # Got data from a player
                        #event = {"type" : "received_data", "socket" : sock, "data" : data}
                        
                        client_event = event.Event("received_data", , , sock, , , , data)
                
                        client_events.append(client_event)
                        
                    else:
                        # The client hung up
                        self.clients.remove(sock)
                        #event = {"type" : "hang_up", "socket" : sock, "removed" : True}
                        
                        client_event = event.Event("hang_up", , , sock, , ,True)
                
                        client_events.append(client_event)
                        
                except socket.error, e:
                    # An error occured reading the client
                    self.clients.remove(sock)
                    #event = {"type" : "socket_error", "socket" : sock, "error" : e, "removed" : True}
                    
                    client_event = event.Event("socket_error", , , sock, , e, True)
                
                    client_events.append(client_event)
                    
        return client_events

if __name__ == "__main__":
    my_server = SelectServer()

    while True:
        updates = my_server.get_updates()
        if updates:
            print updates
