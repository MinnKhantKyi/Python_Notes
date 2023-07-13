# As first, need to write some command in Terminal
# First, write pip install pymongo[srv]
# Second, write pip install python-dotenv

import pymongo
import random

# Create connection with local mongo database
connection = pymongo.MongoClient("localhost",27017)

# Create database
datatbase = connection["test1"]

# Create collection in database
collection = datatbase["user_info"]

if __name__ == "__main__":

    while True:
        user_id = random.randint(1,100)
    
        try:
            print("")
            username : str = str(input("Enter username     > "))
            email : str = str(input("Enter email        > "))
            phone : int = int(input("Enter phone number > "))

            data_form = {"_id":user_id, "username" : username, "email" : email,
                    "phone" : phone}
            
            # add a value to collection and return to ids
            ids = collection.insert_one(data_form)
            print(f"\n- [INSERTED DATA] {ids.inserted_id}")

            exit = int(input("\nEnter 1 to exit > "))
            if exit == 1:
                break
    
        except Exception as err:
            print(f"- [Error] {err}")

    print("\nRetreiving All Data in the Database")
    # "phone":0 means phone will not be shown.
    if collection.find():
        print("Data have.")
    for i in collection.find({},{"phone":0}):
        u_id = i["_id"]
        u_name = i["username"]
        u_email = i["email"]
        print(f"- [ID {u_id}] {u_name} {u_email}")