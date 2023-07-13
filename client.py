import socket

DISCONNECT_MESSAGE : str = "!DISCONNECT"

class Client:
    
    def __init__(self):
        self.PORT = 5050
        self.SERVER = "192.168.161.194"
        self.ADDR = (self.SERVER,self.PORT)
        self.HEADER = 64
        self.FORMAT = "utf-8"

        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def send(self,msg:str):
        message = msg.encode(self.FORMAT)
        msg_length = len(msg)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)


if __name__ == "__main__":
    
    client = Client()
    client.send("Hello mfks...")
    client.send("Hello sotb...")
    client.send("Hello ud...")
    client.send(DISCONNECT_MESSAGE)