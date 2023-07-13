import json
import socket
import pymongo

class Server():

    def __init__(self):
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.PORT = 5050
        self.ADDR = (self.SERVER,self.PORT)
        self.JSON_FILE = "student_info.json"
        self.HEADER = 4096
        self.FORMAT : str = "utf-8"
        self.DISCONNECT_MESSAGE : str = "!DISCONNECT"

        # Start server
        self.__server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__server.bind(self.ADDR)

        # Connect to mongo database
        # Create assignment_5 database in mongo if there is not already have
        self.connection = pymongo.MongoClient("localhost",27017)
        self.database = self.connection["assignment_5"]
        
        collection_list = self.database.list_collection_names()
        if "student_info" in collection_list:
            self.collection = self.database["student_info"]
        else:
            self.store_json_data_in_db()

    def store_json_data_in_db(self):
        print("\n- [READING JSON] Read data from JSON...\n")
        with open(self.JSON_FILE,"r") as json_file:
            data = json.load(json_file)
            self.collection = self.database["student_info"]
            for i in data:
                self.collection.insert_one(i)

    def start(self):
        self.__server.listen()
        print("\n- [STARTING] Server is starting...\n")
        print(f"- [LISTENING] Server is listening on {self.__server}\n")
        
        while True:
            conn, addr = self.__server.accept()
            self.handle_client(conn, addr)

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
                elif msg == "GAD":
                    all_data_str = self.get_all_data()
                    all_data_json = json.dumps(all_data_str)
                    conn.send(bytes(all_data_json, self.FORMAT))
                    print(f"\n- [DATA SENT] All Data in Server database are sent to client.\n")

        print(f"\n- [CONNECTION CLOSED] Connection with {addr} closed.\n")
        conn.close()
                    
    def get_all_data(self):
        print(f"- [READING DATA] Reading all data in Server database.\n")
        data_list = {}
        id = 0
        for data_form in self.collection.find():
            #u_id = data_form["_id"]
            #u_name = data_form["username"]
            #u_email = data_form["email"]
            #u_phone = data_form["phone"]
            #print(f"- [ID {u_id}] {u_name} {u_email} {u_phone}")
            #data_list.update({id:{"ID":u_id,"Username":u_name,"Email":u_email,"Phone":u_phone}})
            data_list.update({id:data_form})
            id += 1

        return data_list

if __name__ == "__main__":
    server = Server()
    server.start()