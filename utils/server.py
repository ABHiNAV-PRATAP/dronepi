#!/usr/bin/env python3

from utils.tcpcom import TCPServer


class Server:
    def __init__(self, port):
        self.server = TCPServer(port, stateChanged=self.onStateChanged)
        self.isConnected = False

    def onStateChanged(self, state, msg):
        if state == "LISTENING":
            print("Server:-- Waiting...")
        elif state == "CONNECTED":
            self.isConnected = True
            print("Server:-- Connected to" + msg)

    def send(self, msg):
        self.server.sendMessage(msg)