from pymongo.errors import *
from objects.MongoDB_Connexion import MongoDB_Connexion


connexion = MongoDB_Connexion()
product_collection = connexion.get_collection("Product", "Nucleotide")
project_collection = connexion.get_collection("Projects", "Nucleotide")

# DATABASE Product


def find_products(query):
    return list(product_collection.find(query))


def get_one_product(id):
    return product_collection.find_one({"_id": id})


def save_product(datas):
    try:
        insert = product_collection.insert_one(datas)
    except DocumentTooLarge:
        return {"id": datas["_id"], "error": "Document trop large"}
    except DuplicateKeyError:
        return {"id": datas["_id"], "error": "Produit déjà téléchargé"}
    except Exception as e:
        return {"id": datas["_id"], "error": "Impossible de télécharger le produit !\n" + str(e)}
    else:
        return {"id": insert.inserted_id, "error": None}


# DATABASE Project

def find_project(query):
    return list(project_collection.find(query))


def get_one_project(id=None, name=None):
    if id is not None:
        return project_collection.find_one({"_id": id})
    else:
        return project_collection.find_one({"name":name})


def get_all_projects():
    return list(project_collection.find({}))


def get_all_projects_for_a_product(id):
    query = {'ids_gb': {'$in': [id]}}
    result = project_collection.find(query)
    return list(result)


def get_not_project_for_a_product(id):
    query = {'ids_gb': {'$nin': [id]}}
    result = project_collection.find(query)
    return list(result)


def add_product_to_project(id, project):
    commit = project_collection.update({'name':project}, {'$addToSet':{'ids_gb':id}})
    return commit


def update_project(where, set):
    commit = project_collection.update(where, set)
    return commit


def save_project(query):
    commit = project_collection.insert_one(query)
    return commit


def delete_project(id):
    commit = project_collection.delete_one({"_id": id})
    return commit


def delete_product_from_project(id_project, id_product):
    commit = project_collection.update({"_id":id_project}, {"$pull":{"ids_gb":id_product}})
    return commit



connexion.close()