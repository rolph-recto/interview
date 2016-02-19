#!/usr/bin/env python
# echoclient.py
# client that listens to an echo server

from socket import *

def main():
    print "hello world!"

    client = socket()

    print 'Connecting to server at port 8000...'
    client.connect(("localhost",8000))
    print 'Connected to server!'

    while True:
        echostr = client.recv(4096)
        if echostr is None:
            break
        else:
            print echostr

    client.close()


if __name__ == "__main__":
    main()
