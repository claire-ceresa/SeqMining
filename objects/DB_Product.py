from datetime import datetime
from pymongo.errors import *
from functions.NCBI_functions import *

class DB_Product:

    """Object representing a product available on the database"""

    def __init__(self, id=None, data=None):
        self.id = id
        self.data = data

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
        self.data["_id"] = self.id
        self.data["download_date"] = datetime.now()
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

    def get_id(self):
        return self.data["_id"]

    def get_description(self):
        return self.data["description"]

    def get_sequence(self):
        return self.data["seq"]["seq"]

    def get_length(self):
        return len(self.data["seq"]["seq"])

    def get_species(self):
        if "organism" in self.data["annotations"]:
            return self.data["annotations"]["organism"]
        else:
            return None
