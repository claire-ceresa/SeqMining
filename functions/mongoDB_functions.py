def exist_on_db(id, collection):
    collection.find_one({"_id": id})