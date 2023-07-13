import socket
import json

class Client():

    def __init__(self):
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.PORT = 5050
        self.ADDR = (self.SERVER,self.PORT)
        self.HEADER = 4096
        self.FORMAT : str = "utf-8"

        # Connect with Server
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def send(self, msg:str):
        
        message = msg.encode(self.FORMAT)
        msg_length = len(msg)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)

        if msg == "GAD":
            received_json = self.client.recv(self.HEADER).decode(self.FORMAT)
            self.show_all_data(received_json)

    def show_all_data(self, data_json):
        data_dict:dict = json.loads(data_json)

        for i in range(len(data_dict)):
            user_id = data_dict[str(i)]['_id']
            user_name = data_dict[str(i)]['username']
            user_email = data_dict[str(i)]['email']
            user_phone = data_dict[str(i)]['phone']
            print(f"ID : {user_id}, Name : {user_name}, Email : {user_email}, Phone : {user_phone}\n")

if __name__ == "__main__":
    client = Client()
    GAD : str = "GAD"
    DISCONNECT_MESSAGE : str = "!DISCONNECT"

    while True:
        try:
            print("\nChoose one.")
            print("1> GAD (Get All Data)")
            print("2> Close connection.")
            option = int(input("Enter > "))

        except Exception as err:
            print(f"\n{err}")

        if option == 1:
            print("\nSend GAD\n")
            print("All Data in Database\n")
            client.send(GAD)

        elif option == 2:
            client.send(DISCONNECT_MESSAGE)
            print("\nSend DISCONNECT_MESSAGE\n")
            break