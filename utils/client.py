from utils.tcpcom import TCPClient
import json


class Client:
    def __init__(self, port, ip, callback):
        self.client = TCPClient(ip, port, stateChanged=self.onStateChanged)
        self.isConnected = False
        self.callback = callback

    def onStateChanged(self, state, msg):
        if state == "LISTENING":
            print("DEBUG: Client:-- Waiting...")
        elif state == "CONNECTED":
            self.isConnected = True
            print("DEBUG: Client:-- Connected to ", msg)
        elif state == "DISCONNECTED":
            self.isConnected = False
            print("DEBUG: Client:-- Connection lost.")
        elif state == "MESSAGE":
            message = msg.split('>')
            header = message[0]
            value = round(float(message[1]), 2)

            if header == 'x':
                x = value
            elif header == 'y':
                y = value
            elif header == 'throttle':
                throttle = value
            elif header == 'yaw':
                yaw = value
            elif header == 'ESTOP':
                throttle = 0

            self.callback(x, y, throttle, yaw)