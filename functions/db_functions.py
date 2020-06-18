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
        return project_collection.find({"id_": id})
    else:
        return project_collection.find({"name":name})


def get_all_projects():
    return project_collection.find({})


def get_all_projects_for_a_product(id):
    query = {'ids_gb': {'$in': [id]}}
    commit = project_collection.find(query)
    return list(commit)


def get_not_project_for_a_product(id):
    query = {'ids_gb': {'$nin': [id]}}
    commit = project_collection.find(query)
    return list(commit)


def add_product_to_project(id, project):
    commit = project_collection.update({'name':project}, {'$addToSet':{'ids_gb':id}})
    print(commit)


def update_project(where, set):
    return project_collection.update(where, set)


def save_project(query):
    return project_collection.insert_one(query)


def delete_project(id):
    return project_collection.delete_one({"_id": id})


def delete_product_from_project(id_project, id_product):
    return project_collection.update({"_id":id_project}, {"$pull":{"ids_gb":id_product}})


connexion.close()