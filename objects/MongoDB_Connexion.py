import subprocess
from pymongo import MongoClient


class MongoDB_Connexion:
    """Object dealing with the connexion to the MongoDB database"""

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
        """Put an end to the mongoDB.bat process"""
        self.process.terminate()

    def close_mongodb(self):
        """Close the connexion with the database"""
        self.client.close()

    def set_database(self):
        """Open the database"""
        self.database = self.client["Nucleotide"]

    def set_collection(self):
        """Open the collection"""
        self.collection = self.database["Product"]

    def check_connexion_to_server(self):
        """Check if SeqMining is connected to the server"""
        try:
            self.client.server_info()
        except:
            return False
        else:
            return True

