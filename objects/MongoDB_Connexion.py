from pymongo import MongoClient


class MongoDB_Connexion:
    """Object dealing with the connexion to the MongoDB database"""

    def __init__(self):
        self.connexion = MongoClient()

    def close(self):
        """Close the connexion with the database"""
        self.connexion.close()

    def get_database(self, database_name):
        """Open the database"""
        return self.connexion[database_name]

    def get_collection(self, collection_name, database_name):
        """Open the collection"""
        database = self.get_database(database_name)
        return database[collection_name]

    def connected_to_server(self):
        """Check if SeqMining is connected to the server"""
        try:
            self.connexion.server_info()
        except:
            return False
        else:
            return True



