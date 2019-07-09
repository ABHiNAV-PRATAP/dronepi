from utils.tcpcom import TCPClient
import json


class Client:
    def __init__(self, port, ip, callback, path):
        self.client = TCPClient(ip, port, stateChanged=self.onStateChanged)
        self.isConnected = False
        self.callback = callback
        self.path = path

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
            with open(self.path) as f:
                data = json.load(f)

            x = data['x']
            y = data['y']
            throttle = data['throttle']
            yaw = data['yaw']

            message = msg.split('>')
            header = message[0]
            value = round(float(message[1]), 2)

            if header == 'x':
                x = value
                data['x'] = value
            elif header == 'y':
                y = value
                data['y'] = value
            elif header == 'throttle':
                throttle = value
                data['throttle'] = value
            elif header == 'yaw':
                yaw = value
                data['yaw'] = value
            elif header == 'ESTOP':
                throttle = 0

            with open(self.path, 'w') as f:
                json.dump(data, f)

            self.callback(x, y, throttle, yaw)