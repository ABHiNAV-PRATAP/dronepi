from utils.tcpcom import TCPClient


class Client:
    def __init__(self, port, ip):
        self.client = TCPClient(ip, port, stateChanged=self.onStateChanged)
        self.isConnected = False

    def onStateChanged(self, state, msg):
        if state == "LISTENING":
            print("DEBUG: Client:-- Listening...")
        elif state == "CONNECTED":
            self.isConnected = True
            print("DEBUG: Client:-- Connected to ", msg)
        elif state == "DISCONNECTED":
            self.isConnected = False
            print("DEBUG: Client:-- Connection lost.")
        elif state == "MESSAGE":
            print("DEBUG: Client:-- Message received: ", msg)
            return msg