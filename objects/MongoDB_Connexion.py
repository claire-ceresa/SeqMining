import subprocess
from pymongo import MongoClient

class MongoDB_Connexion:

    def __init__(self):
        self.process = self.connect_to_mongodb()
        self.client = self.get_client()
        self.connected_to_server = self.check_connexion_to_server()
        self.database = None
        self.collection = None

        if self.connected_to_server:
            self.set_database()
            self.set_collection()

    def connect_to_mongodb(self):
        process = subprocess.Popen("mongoDB.bat")
        return process

    def terminate_process(self):
        self.process.terminate()

    def close_mongodb(self):
        self.client.close()

    def get_client(self):
        client = MongoClient()
        return client

    def set_database(self):
        self.database = self.client["Nucleotide"]

    def set_collection(self):
        self.collection = self.database["Product"]

    def check_connexion_to_server(self):
        try:
            self.client.server_info()
        except:
            return False
        else:
            return True

