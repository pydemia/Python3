#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 17:57:33 2017

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

# %% Class : Chat Client


class ChatClient(object):
    """ A command-line chat client using select"""

    def __init__(self, name, port, host=server_host):

        self.name = name
        self.connected_bool = False
        self.host = host
        self.port = port

        # Initial Prompt
        self.prompt = '[' + '@'.join((self.name, socket.gethostname().split('.')[0])) + ']> '

        # Connect to the server at port
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, self.port))
            print('Now connected to the chat server @ port %d' % self.port)

            self.connected_bool = True

            # Send my name
            send(self.sock, 'NAME: ' + self.name)
            data = receive(self.sock)

            # Contains client address, set it
            addr = data.split('CLIENT: ')[0]
            self.prompt = '[' + '@'.join((self.name, addr)) + ']> '

        except socket.error as err:
            print('Failed to connect to the chat server @ port %d' % self.port)
            sys.exit(1)


    def run(self):
        """Chat client main loop"""

        while self.connected_bool:
            try:
                sys.stdout.write(self.prompt)
                sys.stdout.flush()

                # Wait for the input from stdin and socket
                readable, writeable, exceptional = select.select([0, self.sock], [], [])

                for sock in readable:

                    if sock == 0:
                        data = sys.stdin.readline().strip()

                        if data:
                            send(self.sock, data)

                    elif sock == self.sock:
                        data = receive(self.sock)

                        if not data:
                            print('Client shutting down.')
                            self.connected_bool = False
                            break

                        else:
                            sys.stdout.write(data + '\n')
                            sys.stdout.flush()

            except KeyboardInterrupt:

                    print('Client Interrupted')
                    self.sock.close()
                    break

# %% Run Script

if __name__ == '__main__':
    
    arg_parser = argparse.ArgumentParser(description='Socket server example')
    arg_parser.add_argument('--name', action='store', dest='name', required=True)
    arg_parser.add_argument('--port', action='store', dest='port', type=int,
                            required=True)
    
    given_args = arg_parser.parse_args()
    name = given_args.name
    port = given_args.port
    
    client = ChatClient(name=name, port=port)
    client.run()