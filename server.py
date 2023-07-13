import socket
import threading

class Server:

    def __init__(self):
        self.PORT = 5050
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER,self.PORT)
        self.HEADER = 64
        self.FORMAT : str = "utf-8"
        self.DISCONNECT_MESSAGE : str = "!DISCONNECT"

        self.__server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__server.bind(self.ADDR)

    def handle_client(self, conn, addr):
        print(f"- [NEW CONNECTION] {addr} connected.\n")
        connected = True

        while connected:
            msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
            
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(self.FORMAT)

                if msg == self.DISCONNECT_MESSAGE:
                    connected = False

                print(f"- [{addr}] {msg}")

        conn.close()

        print("\n")

    def start(self):
        self.__server.listen()
        print(f"- [LISTENING] Server is listening on {self.__server}\n")
        
        while True:
            conn , addr = self.__server.accept()
            thread = threading.Thread(target=self.handle_client,args=(conn, addr))
            thread.start()
            print(f"- [ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == '__main__':
    
    server = Server()
    print("\n- [STARTING] Server is starting...\n")
    server.start()