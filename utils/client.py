from utils.tcpcom import TCPClient


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
            # print("DEBUG: Client:-- Message received: ", msg)
            x = 0
            y = 0
            throttle = None
            yaw = 0
            msg = msg.split('>')
            header = msg[0]
            value = float(msg[1])
            if header == 'x':
                x = value
            elif header == 'y':
                y = value
            elif header == 'throttle':
                throttle = value
            elif header == 'yaw':
                yaw = value
            # TODO: Some sort of processing on msg in order to satisfy parameter requirements of the callback function
            self.callback(x, y, throttle, yaw)