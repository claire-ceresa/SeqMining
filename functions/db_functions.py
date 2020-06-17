from objects.MongoDB_Connexion import MongoDB_Connexion


connexion = MongoDB_Connexion()
product_collection = connexion.get_collection("Products", "Nucleotide")
project_collection = connexion.get_collection("Projects", "Nucleotide")


def get_all_projects():
    return project_collection.find({})


def get_one_product(id):
    return product_collection.find_one({"_id": id})


def get_all_projects_for_a_product(id):
    query = {'ids_gb':{'$in':[id]}}
    commit = project_collection.find(query)
    return list(commit)


def get_not_project_for_a_product(id):
    query = {'ids_gb':{'$nin':[id]}}
    commit = project_collection.find(query)
    return list(commit)


def add_product_to_project(id, project):
    commit = project_collection.update({'name':project}, {'$addToSet':{'ids_gb':id}})
    print(commit)

