from datetime import datetime
from pymongo.errors import *


class DB_Product:

    """Object representing a product available on the database"""

    def __init__(self, id=None, data=None):
        self.id = id
        self.data = data
        self.data["_id"] = id
        self.data["download_date"] = datetime.now()

    def existed_in_collection(self, collection):
        """Check if the id existed in the collection"""
        result = collection.find_one({"_id": self.id})
        if result is None:
            return False
        else:
            return True

    def save_on_db(self, collection):
        """
        Save the product on the database
        :param collection: name of the collection where to save it
        :return: {'id':str, 'error':str or None}
        """
        try:
            insert = collection.insert_one(self.data)
        except DocumentTooLarge:
            return {"id":self.data["_id"], "error":"Document trop large"}
        except DuplicateKeyError:
            return {"id":self.data["_id"], "error":"Produit déjà téléchargé"}
        except Exception as e:
            return {"id":self.data["_id"], "error":"Impossible de télécharger le produit !\n" + str(e)}
        else:
            return {"id":insert.inserted_id, "error":None}

