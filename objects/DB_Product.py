from datetime import datetime
from pymongo.errors import *

class DB_Product:

    def __init__(self, id=None, data=None):
        self.id = id
        self.data = data
        self.data["_id"] = id
        self.data["download_date"] = datetime.now()

    def existed_in_collection(self, collection):
        result = collection.find_one({"_id": self.id})
        return result

    def save_on_mongoDB(self, collection):
        try:
            insert = collection.insert_one(self.data)
        except DocumentTooLarge:
            error = " Document trop large"
        except DuplicateKeyError:
            error = "Produit déjà téléchargé"
        except Exception as e:
            error = "Impossible de télécharger le produit"
        else:
            error = None
        return error

