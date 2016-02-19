#!/usr/bin/env python
# echoserver.py
# server that echoes stdin

from socket import *

def main():
    # create listening socket
    server = socket()
    server.bind(("localhost",8000))
    server.listen(0)

    print 'Waiting for client to connect...'
    (client, clientaddr) = server.accept()

    print 'Client connected: {}'.format(clientaddr)

    while True:
        try:
            echostr = raw_input()
            client.sendall(echostr)
        except EOFError:
            break

    client.close()
    server.close()
        
if __name__ == '__main__':
    main()
