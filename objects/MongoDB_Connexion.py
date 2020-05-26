import subprocess
from pymongo import MongoClient

class MongoDB_Connexion:

    def __init__(self):
        self.process = subprocess.Popen("mongoDB.bat")
        self.client = MongoClient()
        self.connected_to_server = self.check_connexion_to_server()
        self.database = None
        self.collection = None

        if self.connected_to_server:
            self.set_database()
            self.set_collection()

    def terminate_process(self):
        self.process.terminate()

    def close_mongodb(self):
        self.client.close()

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

