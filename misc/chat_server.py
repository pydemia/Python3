#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 17:57:18 2017

@author: pydemia
"""


import sys
import socket
import select
import signal
import pickle
import struct
import argparse


server_host = 'localhost'
chat_server_name = 'chat_server'


# Some Utility Functions
def send(channel, *args):
    buffer = pickle.dumps(*args)
    value = socket.htonl(len(buffer))
    size = struct.pack('L', value)
    channel.send(size)
    channel.send(buffer)


def receive(channel):

    size = struct.calcsize('L')
    size = channel.recv(size)

    try:
        size = socket.ntohl(struct.unpack('L', size)[0])
    except struct.error as err:
        return ''

    buf = ''
    while len(buf) < size:
        buf = channel.recv(size - len(buf))

    return pickle.loads(buf, encoding='utf8')


# %% Class : Chat Server


class ChatServer(object):
    """A simple chat server using select"""

    def __init__(self, port, backlog=5):

        self.clients = 0
        self.clientmap = {}
        self.outputs = []  # List : output sockets

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server.bind((server_host, port))
        print('Server Listening to port : %s ...' % port)

        self.server.listen(backlog)

        # Catch Keyboard Interrupt
        signal.signal(signal.SIGINT, self.sighandler)


    def sighandler(self, signum, frame):
        """Clean up client outputs"""

        # Close the server
        print('Shutting down the server...')

        # Close existing client sockets
        for output in self.outputs:
            output.close()

        self.server.close()


    def get_client_name(self, client):
        """Return the name of the client"""

        info = self.clientmap[client]
        host, name = info[0][0], info[1]

        return '@'.join((name, host))


    def run(self):
        inputs = [self.server, sys.stdin]
        self.outputs = []
        running_bool = True

        while running_bool:
            try:
                readable, writeable, exceptional = select.select(inputs, self.outputs, [])
            except select.error as err:
                break

            for sock in readable:
                if sock == self.server:

                    # Handle the server socket
                    client, address = self.server.accept()
                    print('Chat Server: got connected %d from %s' % (client.fileno(), address))

                    # Read the login name
                    cname = receive(client).split('NAME: ')[1]
                    #cname = receive(client)

                    # Compute the client name and send it back
                    self.clients += 1
                    send(client, 'CLIENT: ' + str(address[0]))
                    inputs.append(client)
                    self.clientmap[client] = address, cname

                    # Send the joining info to other clients
                    msg = '\n(Connected: New client (%d) from %s)' % (self.clients, self.get_client_name(client))

                    for output in self.outputs:
                        send(output, msg)

                    self.outputs.append(client)

                elif sock == sys.stdin:

                    # Handle the standard input
                    junk = sys.stdin.readline()
                    running_bool = False

                else:

                    # Handle all other sockets
                    try:
                        data = receive(sock)

                        if data:

                            # Send as new client's message
                            msg = '\n' + self.get_client_name(sock) + ']>> ' + data

                            # Send data to all except ourself
                            for output in self.outputs:
                                if output != sock:
                                    send(output, msg)

                        else:
                            print('Chat server : %d hung up' % sock.fileno())
                            self.clients -= 1
                            sock.close()
                            inputs.remove(sock)
                            self.outputs.remove(sock)

                            # Sending client leaving info to others
                            msg = '\n(Now hung up : Client from %s)' % self.get_client_name(sock)

                            for output in self.outputs:
                                send(output, msg)

                    except socket.error as err:

                        # Remove
                        inputs.remove(sock)
                        self.outputs.remove(sock)

        # Run close
        self.server.close()

# %% Run Script : Server

if __name__ == '__main__':
    
    arg_parser = argparse.ArgumentParser(description='Socket server example')
    arg_parser.add_argument('--port', action='store', dest='port', type=int,
                            required=True)
    
    given_args = arg_parser.parse_args()
    port = given_args.port
    
    server = ChatServer(port)
    server.run()